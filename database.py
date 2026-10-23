# ==============================================================================
# DATABASE MODULE (database.py)
# ==============================================================================
# This file handles all SQLite database operations for the Pet Classifier app.
#
# Key Features:
# 1. Uses the standard library 'sqlite3' (no extra packages needed).
# 2. Stores data in 'pets.db'.
# 3. Uses parameterized queries (? placeholders) to prevent SQL injection.
# 4. Opens a fresh, short-lived connection per function call with a timeout.
# 5. Automatically creates tables and seeds breed information on first run.
# 6. Wrapped in try/except blocks so database errors never crash the Streamlit UI.
# ==============================================================================

import sqlite3
import datetime
import os
from breeds_seed import BREEDS_DATA

# Path to the SQLite database file
DB_NAME = "pets.db"


def get_db_connection():
    """
    Creates and returns a new database connection with a 10-second timeout.
    Enables dictionary-like row access so columns can be accessed by name.
    """
    conn = sqlite3.connect(DB_NAME, timeout=10.0)
    # This allows us to access columns using row["column_name"]
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    """
    Initializes the database:
    - Creates the 'predictions' table if it doesn't already exist.
    - Creates the 'breeds' table if it doesn't already exist.
    - Seeds the 'breeds' table from breeds_seed.py if it is empty.
    """
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        # 1. Create the predictions table
        # Stores every classification made by users
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS predictions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                created_at TEXT NOT NULL,
                filename TEXT NOT NULL,
                animal TEXT NOT NULL,
                animal_conf REAL NOT NULL,
                breed TEXT,
                breed_conf REAL,
                uncertain INTEGER NOT NULL,
                feedback TEXT
            );
        """)

        # 2. Create the breeds table
        # Stores educational information about cats and dogs
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS breeds (
                name TEXT PRIMARY KEY,
                animal TEXT NOT NULL,
                origin TEXT NOT NULL,
                lifespan TEXT NOT NULL,
                size TEXT NOT NULL,
                temperament TEXT NOT NULL,
                fun_fact TEXT NOT NULL
            );
        """)

        conn.commit()

        # 3. Check if the breeds table already has data
        cursor.execute("SELECT COUNT(*) AS total FROM breeds;")
        count = cursor.fetchone()["total"]

        # If empty, populate it with seed data from breeds_seed.py
        if count == 0:
            for item in BREEDS_DATA:
                cursor.execute("""
                    INSERT OR IGNORE INTO breeds (name, animal, origin, lifespan, size, temperament, fun_fact)
                    VALUES (?, ?, ?, ?, ?, ?, ?);
                """, (
                    item.get("name", "Unknown"),
                    item.get("animal", "Unknown"),
                    item.get("origin", "Unknown"),
                    item.get("lifespan", "Unknown"),
                    item.get("size", "Unknown"),
                    item.get("temperament", "Unknown"),
                    item.get("fun_fact", "Unknown")
                ))
            conn.commit()

        conn.close()
        return True

    except sqlite3.Error as e:
        print(f"Database initialization error: {e}")
        return False


def insert_prediction(filename, animal, animal_conf, breed, breed_conf, uncertain):
    """
    Inserts a new classification record into the 'predictions' table.
    
    Parameters:
    - filename: Name of the uploaded file or camera image
    - animal: "Cat", "Dog", or "Neither"
    - animal_conf: Confidence score for the animal (0.0 to 1.0)
    - breed: Predicted breed name or None
    - breed_conf: Confidence score for the breed or None
    - uncertain: 1 if confidence < 0.50, else 0
    
    Returns:
    - The integer ID of the newly inserted row (or None on failure).
    """
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        created_at = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        cursor.execute("""
            INSERT INTO predictions (
                created_at, filename, animal, animal_conf, breed, breed_conf, uncertain, feedback
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, NULL);
        """, (
            created_at,
            filename or "image.jpg",
            animal,
            float(animal_conf) if animal_conf is not None else 0.0,
            breed if breed else "",
            float(breed_conf) if breed_conf is not None else 0.0,
            1 if uncertain else 0
        ))

        new_id = cursor.lastrowid
        conn.commit()
        conn.close()
        return new_id

    except sqlite3.Error as e:
        print(f"Error inserting prediction: {e}")
        return None


def update_feedback(prediction_id, feedback):
    """
    Updates the feedback column ('Correct' or 'Wrong') for a given prediction.
    """
    if not prediction_id:
        return False
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("""
            UPDATE predictions
            SET feedback = ?
            WHERE id = ?;
        """, (feedback, prediction_id))

        conn.commit()
        conn.close()
        return True

    except sqlite3.Error as e:
        print(f"Error updating feedback: {e}")
        return False


def normalize_breed_name(name):
    """
    Helper function to normalize breed names for comparison.
    Converts to lowercase, replaces underscores and dashes with spaces, and trims whitespace.
    Example: 'Maine_Coon' -> 'maine coon'
    """
    if not name:
        return ""
    return name.lower().replace("_", " ").replace("-", " ").strip()


def get_breed_info(breed_name):
    """
    Looks up a breed from the 'breeds' table using the name-normalizing rule.
    Returns a dictionary of breed details, or a safe default dictionary if not found.
    """
    fallback = {
        "name": breed_name or "Unknown Breed",
        "animal": "Unknown",
        "origin": "Unknown",
        "lifespan": "Unknown",
        "size": "Unknown",
        "temperament": "Unknown",
        "fun_fact": "No additional details available for this breed yet."
    }

    if not breed_name:
        return fallback

    norm_target = normalize_breed_name(breed_name)
    
    # Dataset names that differ from the names used in our breeds table
    BREED_ALIASES = {
        "japanese spaniel": "japanese chin",
        "staffordshire bullterrier": "staffordshire bull terrier",
        "german short haired pointer": "german shorthaired pointer",
        "wire haired fox terrier": "wire fox terrier",
    }
    norm_target = BREED_ALIASES.get(norm_target, norm_target)

    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        # Query all breeds to match using our Python normalizer
        # (This ensures 100% case-insensitivity and handles underscores/spaces)
        cursor.execute("SELECT name, animal, origin, lifespan, size, temperament, fun_fact FROM breeds;")
        rows = cursor.fetchall()
        conn.close()

        # 1. Try exact normalized match
        for r in rows:
            if normalize_breed_name(r["name"]) == norm_target:
                return dict(r)

        # 2. Try substring match (e.g. 'corgi' matches 'pembroke' or 'cardigan')
        for r in rows:
            clean_db_name = normalize_breed_name(r["name"])
            if norm_target in clean_db_name or clean_db_name in norm_target:
                return dict(r)

        return fallback

    except sqlite3.Error as e:
        print(f"Error fetching breed info: {e}")
        return fallback


def get_history(animal_filter="All", breed_search="", only_wrong=False):
    """
    Fetches prediction history with dynamic SQL filters.
    
    Filters:
    - animal_filter: 'All', 'Cat', 'Dog', or 'Neither'
    - breed_search: Substring search in breed column
    - only_wrong: If True, only returns rows where feedback = 'Wrong'
    """
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        # Build dynamic SQL query safely using parameterized conditions
        sql = "SELECT id, created_at, filename, animal, animal_conf, breed, breed_conf, uncertain, feedback FROM predictions WHERE 1=1"
        params = []

        if animal_filter and animal_filter != "All":
            sql += " AND animal = ?"
            params.append(animal_filter)

        if breed_search and breed_search.strip():
            sql += " AND breed LIKE ?"
            params.append(f"%{breed_search.strip()}%")

        if only_wrong:
            sql += " AND feedback = 'Wrong'"

        sql += " ORDER BY id DESC LIMIT 200;"

        cursor.execute(sql, params)
        rows = cursor.fetchall()
        conn.close()

        # Convert sqlite3.Row objects to list of standard Python dicts
        return [dict(r) for r in rows]

    except sqlite3.Error as e:
        print(f"Error fetching history: {e}")
        return []


def clear_history():
    """
    Deletes all records from the 'predictions' table.
    """
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM predictions;")
        conn.commit()
        conn.close()
        return True
    except sqlite3.Error as e:
        print(f"Error clearing history: {e}")
        return False


def get_stats():
    """
    Calculates aggregated statistics for the Stats page using SQL queries.
    Returns a dictionary with metric values and the exact SQL queries used.
    """
    data = {
        "total": 0,
        "cats": 0,
        "dogs": 0,
        "neither": 0,
        "top_breeds": [],
        "avg_conf": {},
        "rejections": 0,
        "daily_counts": [],
        "feedback_counts": {"Correct": 0, "Wrong": 0, "Unrated": 0},
        "queries": {}
    }

    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        # 1. Total predictions
        q_total = "SELECT COUNT(*) AS total FROM predictions;"
        cursor.execute(q_total)
        data["total"] = cursor.fetchone()["total"]
        data["queries"]["total"] = q_total

        # 2. Count per animal
        q_animal = "SELECT animal, COUNT(*) AS count FROM predictions GROUP BY animal;"
        cursor.execute(q_animal)
        for r in cursor.fetchall():
            an = r["animal"]
            if an == "Cat":
                data["cats"] = r["count"]
            elif an == "Dog":
                data["dogs"] = r["count"]
            elif an == "Neither":
                data["neither"] = r["count"]
        data["queries"]["animal_counts"] = q_animal

        # 3. Top 5 breeds predicted
        q_top = """
            SELECT breed, COUNT(*) AS count 
            FROM predictions 
            WHERE breed IS NOT NULL AND breed != '' 
            GROUP BY breed 
            ORDER BY count DESC 
            LIMIT 5;
        """
        cursor.execute(q_top)
        data["top_breeds"] = [(r["breed"], r["count"]) for r in cursor.fetchall()]
        data["queries"]["top_breeds"] = q_top.strip()

        # 4. Average confidence per animal
        q_avg = "SELECT animal, AVG(animal_conf) AS avg_conf FROM predictions GROUP BY animal;"
        cursor.execute(q_avg)
        for r in cursor.fetchall():
            data["avg_conf"][r["animal"]] = round(float(r["avg_conf"] or 0.0) * 100, 1)
        data["queries"]["avg_conf"] = q_avg

        # 5. Rejections count (Neither Cat nor Dog)
        q_reject = "SELECT COUNT(*) AS rejections FROM predictions WHERE animal = 'Neither';"
        cursor.execute(q_reject)
        data["rejections"] = cursor.fetchone()["rejections"]
        data["queries"]["rejections"] = q_reject

        # 6. Predictions per day (last 7 days)
        q_daily = """
            SELECT SUBSTR(created_at, 1, 10) AS day, COUNT(*) AS count 
            FROM predictions 
            GROUP BY SUBSTR(created_at, 1, 10) 
            ORDER BY day DESC 
            LIMIT 7;
        """
        cursor.execute(q_daily)
        data["daily_counts"] = [(r["day"], r["count"]) for r in cursor.fetchall()]
        data["queries"]["daily"] = q_daily.strip()

        # 7. Feedback accuracy (Correct vs Wrong)
        q_feedback = """
            SELECT 
                COALESCE(feedback, 'Unrated') AS fb_status, 
                COUNT(*) AS count 
            FROM predictions 
            GROUP BY fb_status;
        """
        cursor.execute(q_feedback)
        for r in cursor.fetchall():
            status = r["fb_status"]
            if status in data["feedback_counts"]:
                data["feedback_counts"][status] = r["count"]
        data["queries"]["feedback"] = q_feedback.strip()

        conn.close()
        return data

    except sqlite3.Error as e:
        print(f"Error computing stats: {e}")
        return data


def get_all_breeds(animal_filter="All", size_filter="All", search_query=""):
    """
    Fetches breeds for the Breed Explorer page with optional filtering by:
    - animal ('All', 'Cat', 'Dog')
    - size ('All', 'Small', 'Medium', 'Large', 'Giant')
    - search_query (matches breed name or origin)
    """
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        sql = "SELECT name, animal, origin, lifespan, size, temperament, fun_fact FROM breeds WHERE 1=1"
        params = []

        if animal_filter and animal_filter != "All":
            sql += " AND animal = ?"
            params.append(animal_filter)

        if size_filter and size_filter != "All":
            sql += " AND size = ?"
            params.append(size_filter)

        if search_query and search_query.strip():
            sql += " AND (name LIKE ? OR origin LIKE ?)"
            term = f"%{search_query.strip()}%"
            params.extend([term, term])

        sql += " ORDER BY name ASC;"

        cursor.execute(sql, params)
        rows = cursor.fetchall()
        conn.close()

        return [dict(r) for r in rows]

    except sqlite3.Error as e:
        print(f"Error fetching breeds: {e}")
        return []
