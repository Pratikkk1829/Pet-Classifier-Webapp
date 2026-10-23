# ==============================================================================
# PET CLASSIFIER - STREAMLIT WEB APPLICATION (app.py)
# ==============================================================================
# Class 12 Computer Science Project
# Author: Class 12 Student
#
# This application classifies images of domestic pets (Cats and Dogs) using a
# two-stage deep learning pipeline (ONNX Runtime) and stores records in SQLite.
#
# Pages:
# 1. Classify: Upload photo or use camera to predict animal and breed.
# 2. History: View past classifications with SQL-powered filters.
# 3. Stats: Statistical dashboard featuring "Show the SQL" for viva questions.
# 4. Breed Explorer: Searchable database of 130+ cat and dog breeds.
# 5. About: Project architecture, models, and limitations.
# ==============================================================================

import io
import os
import pandas as pd
import streamlit as st
from PIL import Image, ImageOps

# Import our custom modular components
import database
import inference
from styles import NEUMORPHIC_CSS

# ------------------------------------------------------------------------------
# 1. Page Configuration & Safety Settings
# ------------------------------------------------------------------------------
st.set_page_config(
    page_title="Pet Classifier",
    page_icon="🐾",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Protect against decompression bomb attacks by setting a strict pixel limit
Image.MAX_IMAGE_PIXELS = 10_000_000

# Inject our Neumorphic (Soft UI) CSS styling
st.markdown(NEUMORPHIC_CSS, unsafe_allow_html=True)

# Persistent limits banner — floating above the bottom on every page
st.markdown("""
    <div class="limits-footer">
        <div>
            <span>⚠️ System Limits:</span>
            <b>Upload Limit:</b> Max 5 MB per image (JPG/PNG/WEBP) &nbsp;·&nbsp;
            <b>Scope Limit:</b> Cats &amp; Dogs only across 132 breeds (others rejected) &nbsp;·&nbsp;
            <b>Server Limit:</b> Max 2 concurrent inferences to avoid CPU overload &nbsp;·&nbsp;
            <b>Storage Limit:</b> RAM-only (no images saved to disk)
        </div>
        <div class="limits-explain">
            (Why 132 breeds? Trained on 12 cat &amp; 120 dog breeds from the Oxford-IIIT Pet and Stanford Dogs datasets; wild felines/canines and unindexed breeds fall outside this vocabulary)
        </div>
    </div>
""", unsafe_allow_html=True)

# Initialize the SQLite database tables and seed data if not already done
database.init_db()


# ------------------------------------------------------------------------------
# 2. Helper Functions
# ------------------------------------------------------------------------------
def validate_and_load_image(uploaded_file):
    """
    Validates an uploaded image file:
    1. Checks file size (up to 5 MB limit).
    2. Verifies image integrity using PIL verify().
    3. Resets file pointer and reopens clean image.
    4. Downscales so the longest edge is at most 1024px to save memory.
    """
    try:
        # Check size in bytes (5 MB = 5 * 1024 * 1024)
        if uploaded_file.size > 5 * 1024 * 1024:
            st.error("⚠️ File size exceeds 5 MB. Please upload a smaller image.")
            return None

        # Read into memory
        image_bytes = uploaded_file.read()
        
        # Verify image integrity
        with Image.open(io.BytesIO(image_bytes)) as img_check:
            img_check.verify()

        # Reopen image after verify
        img = Image.open(io.BytesIO(image_bytes))
        img = ImageOps.exif_transpose(img)   

        # Downscale if the longest dimension is greater than 1024 pixels
        max_dimension = 1024
        width, height = img.size
        if max(width, height) > max_dimension:
            scale_ratio = max_dimension / max(width, height)
            new_width = int(width * scale_ratio)
            new_height = int(height * scale_ratio)
            img = img.resize((new_width, new_height), Image.Resampling.BILINEAR)

        return img

    except Exception as e:
        st.error(f"⚠️ Could not read image: {e}. Please ensure it is a valid JPG, PNG, or WEBP file.")
        return None


# ------------------------------------------------------------------------------
# 3. Sidebar Navigation
# ------------------------------------------------------------------------------
with st.sidebar:
    st.markdown("""
        <div style="text-align: center; padding: 10px 0 20px 0;">
            <h1 style="font-size: 2rem; margin: 0;">🐾</h1>
            <h2 style="font-size: 1.35rem; margin: 5px 0 0 0; font-weight: 800; color: #6c63ff;">Pet Classifier</h2>
            <p style="font-size: 0.85rem; color: #555e7d; margin: 0;">Class 12 AI & Database Project</p>
        </div>
    """, unsafe_allow_html=True)

    page = st.radio(
        label="Navigation Menu",
        options=["🐾 Classify", "📜 History", "📊 Stats", "📖 Breed Explorer", "ℹ️ About"],
        label_visibility="collapsed"
    )

    st.markdown("---")
    st.markdown("""
        <div style="font-size: 0.8rem; color: #717b9b; line-height: 1.4;">
            <b>Built with:</b><br>
            • Streamlit & Python 3.11<br>
            • ONNX Runtime (CPU)<br>
            • SQLite Database (pets.db)<br>
            • Neumorphic Design System
        </div>
    """, unsafe_allow_html=True)


# ------------------------------------------------------------------------------
# PAGE 1: CLASSIFY
# ------------------------------------------------------------------------------
if page == "🐾 Classify":
    st.markdown("""
        <div class="neu-card" style="margin-bottom: 20px;">
            <h2 style="margin: 0; font-size: 1.6rem; font-weight: 800; color: #2d3350;">Pet Image Classifier</h2>
            <p style="margin: 6px 0 0 0; color: #555e7d; font-size: 0.95rem;">
                Upload a pet photo or use your camera to identify cats and dogs and discover their breed!
            </p>
        </div>
    """, unsafe_allow_html=True)

    # Let user choose between file upload or camera capture
    input_method = st.radio("Choose Input Method:", ["📁 Upload File", "📷 Use Camera"], horizontal=True)

    pil_img = None
    file_name = "camera_snapshot.jpg"

    if input_method == "📁 Upload File":
        uploaded_file = st.file_uploader(
            label="Upload pet image (JPG, PNG, WEBP — Max 5MB)",
            type=["jpg", "jpeg", "png", "webp"],
            help="Upload a clear image of a cat or dog."
        )
        if uploaded_file is not None:
            file_name = uploaded_file.name
            pil_img = validate_and_load_image(uploaded_file)

    else:
        camera_file = st.camera_input("Take a photo of your pet:")
        if camera_file is not None:
            file_name = "camera_capture.jpg"
            pil_img = validate_and_load_image(camera_file)

    # Display image preview and classification actions
    if pil_img is not None:
        col_img, col_action = st.columns([1, 1], gap="medium")

        with col_img:
            with st.container(border=True):
                st.image(pil_img, caption="Image Preview", width=380)

        with col_action:
            with st.container(border=True):
                st.markdown("<h3 style='margin-top:0;'>Ready to Classify</h3>", unsafe_allow_html=True)
                st.markdown(f"<p style='color: #555e7d;'>Image Size: {pil_img.size[0]} × {pil_img.size[1]} pixels</p>", unsafe_allow_html=True)
                classify_clicked = st.button("🔍 Classify Pet", type="primary", use_container_width=True)

        # Execute classification when button is clicked
        if classify_clicked:
            try:
                with st.spinner("Analyzing image through two-stage neural network..."):
                    result = inference.classify(pil_img)

                # Save result to database
                pred_id = database.insert_prediction(
                    filename=file_name,
                    animal=result["animal"],
                    animal_conf=result["animal_conf"],
                    breed=result["breed"],
                    breed_conf=result["breed_conf"],
                    uncertain=result["uncertain"]
                )
                st.session_state["last_pred_id"] = pred_id
                st.session_state["last_result"] = result

            except Exception as e:
                st.error(f"⚠️ {str(e)}")

        # Display results if available in session_state
        if "last_result" in st.session_state:
            res = st.session_state["last_result"]
            pred_id = st.session_state.get("last_pred_id")

            st.markdown("---")
            animal = res["animal"]
            animal_conf = res["animal_conf"]
            breed = res["breed"]
            breed_conf = res["breed_conf"]
            uncertain = res["uncertain"]
            top3 = res.get("top3", [])
            seconds = res.get("seconds", 0.0)

            # CASE A: Neither Cat nor Dog (Rejection)
            if animal == "Neither":
                st.markdown(f"""
                    <div class="neu-card" style="border-left: 8px solid #f39c12;">
                        <h2 style="margin: 0; color: #d35400;">❓ Neither Cat nor Dog</h2>
                        <p style="font-size: 1.1rem; margin: 10px 0;"><b>This is neither a dog nor a cat.</b></p>
                        <p style="color: #555e7d;">The neural network detected that this image does not belong to domestic cats or dogs (Rejection confidence: {animal_conf * 100:.1f}%). Specialist breed models were not run.</p>
                        <div class="neu-badge">⚡ Analyzed in {seconds}s</div>
                    </div>
                """, unsafe_allow_html=True)

            # CASE B & C: Cat or Dog identified
            else:
                emoji = "🐱" if animal == "Cat" else "🐶"

                # If uncertain (< 50% top confidence)
                if uncertain:
                    st.markdown(f"""
                        <div class="neu-card" style="border-left: 8px solid #e67e22;">
                            <h2 style="margin: 0; color: #d35400;">⚠️ Not Sure - Best Guess: {breed}</h2>
                            <p style="margin: 8px 0; font-size: 1.05rem;">
                                Animal detected: <b>{emoji} {animal}</b> ({animal_conf * 100:.1f}% confidence)<br>
                                However, the specialist breed model has low certainty (<b>{breed_conf * 100:.1f}%</b>).
                            </p>
                            <p style="color: #555e7d; font-size: 0.9rem;">
                                💡 Tip: The pet might be a mixed breed or the photo might be taken from an unusual angle.
                            </p>
                            <div class="neu-badge">⚡ Analyzed in {seconds}s</div>
                        </div>
                    """, unsafe_allow_html=True)

                # Confident prediction
                else:
                    st.markdown(f"""
                        <div class="neu-card" style="border-left: 8px solid #2ecc71;">
                            <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap;">
                                <div>
                                    <span class="neu-badge">{emoji} {animal} ({animal_conf * 100:.1f}%)</span>
                                    <span class="neu-badge">⚡ {seconds}s latency</span>
                                </div>
                            </div>
                            <h1 style="margin: 10px 0 0 0; font-size: 2.4rem; color: #2d3350;">{breed}</h1>
                            <p style="color: #555e7d; font-size: 1.1rem; margin: 4px 0 16px 0;">
                                Top predicted breed with <b>{breed_conf * 100:.1f}%</b> confidence
                            </p>
                            <div class="neu-progress-track">
                                <div class="neu-progress-fill" style="width: {min(max(int(breed_conf * 100), 10), 100)}%;"></div>
                            </div>
                        </div>
                    """, unsafe_allow_html=True)

                # Show Top-3 predictions and Breed Info Card
                col_top3, col_info = st.columns([1, 1], gap="medium")

                with col_top3:
                    with st.container(border=True):
                        st.markdown("<h3 style='margin-top:0;'>📊 Top-3 Specialist Predictions</h3>", unsafe_allow_html=True)
                        for rank, (b_name, b_prob) in enumerate(top3, 1):
                            pct = b_prob * 100
                            st.markdown(f"""
                                <div style="margin-bottom: 12px;">
                                    <div style="display: flex; justify-content: space-between; font-weight: 600; font-size: 0.95rem;">
                                        <span>#{rank} {b_name}</span>
                                        <span>{pct:.1f}%</span>
                                    </div>
                                    <div class="neu-progress-track" style="height: 12px; margin: 4px 0;">
                                        <div class="neu-progress-fill" style="width: {pct}%;"></div>
                                    </div>
                                </div>
                            """, unsafe_allow_html=True)

                with col_info:
                    with st.container(border=True):
                        st.markdown(f"<h3 style='margin-top:0;'>📖 Breed Facts: {breed}</h3>", unsafe_allow_html=True)
                        breed_info = database.get_breed_info(breed)

                        st.markdown(f"""
                            <div class="neu-inset">
                                <p style="margin: 4px 0;"><b>🌍 Origin:</b> {breed_info.get('origin', 'Unknown')}</p>
                                <p style="margin: 4px 0;"><b>⏳ Typical Lifespan:</b> {breed_info.get('lifespan', 'Unknown')}</p>
                                <p style="margin: 4px 0;"><b>📏 Size Category:</b> {breed_info.get('size', 'Unknown')}</p>
                                <p style="margin: 4px 0;"><b>🎭 Temperament:</b> {breed_info.get('temperament', 'Unknown')}</p>
                                <hr style="border: none; border-top: 1px solid #c8d0de; margin: 10px 0;">
                                <p style="margin: 4px 0; font-style: italic; color: #434c6e;">
                                    <b>✨ Fun Fact:</b> {breed_info.get('fun_fact', 'Unknown')}
                                </p>
                            </div>
                        """, unsafe_allow_html=True)

            # User Feedback buttons (Updates the SQLite database)
            with st.container(border=True):
                st.markdown("<h4 style='margin: 0 0 10px 0; text-align: center;'>Was this classification correct?</h4>", unsafe_allow_html=True)
                col_fb1, col_fb2, col_spacer = st.columns([1, 1, 2])

                with col_fb1:
                    if st.button("👍 Correct", key="btn_correct", use_container_width=True):
                        database.update_feedback(pred_id, "Correct")
                        st.success("✅ Saved: Marked as Correct!")

                with col_fb2:
                    if st.button("👎 Wrong", key="btn_wrong", use_container_width=True):
                        database.update_feedback(pred_id, "Wrong")
                        st.warning("⚠️ Saved: Marked as Wrong!")


# ------------------------------------------------------------------------------
# PAGE 2: HISTORY
# ------------------------------------------------------------------------------
elif page == "📜 History":
    st.markdown("""
        <div class="neu-card">
            <h2 style="margin: 0; font-size: 1.6rem; font-weight: 800; color: #2d3350;">Prediction History</h2>
            <p style="margin: 6px 0 0 0; color: #555e7d; font-size: 0.95rem;">
                Browse past classifications stored in SQLite. Filter results using SQL WHERE clauses.
            </p>
        </div>
    """, unsafe_allow_html=True)

    # Filter controls
    col_f1, col_f2, col_f3 = st.columns([1, 1, 1], gap="medium")
    with col_f1:
        animal_filter = st.selectbox("Filter by Animal:", ["All", "Cat", "Dog", "Neither"])
    with col_f2:
        breed_search = st.text_input("Search Breed Name:", "")
    with col_f3:
        only_wrong = st.checkbox("Show Only 'Wrong' Feedback", value=False)

    # Fetch filtered history from database
    history_data = database.get_history(animal_filter, breed_search, only_wrong)

    # Show count of records
    st.markdown(f"<p style='color: #555e7d; font-weight: 600;'>Found {len(history_data)} matching record(s).</p>", unsafe_allow_html=True)

    if history_data:
        df = pd.DataFrame(history_data)
        # Reorder and rename columns for display
        display_df = df[[
            "id", "created_at", "filename", "animal", "animal_conf", "breed", "breed_conf", "feedback"
        ]].copy()

        # Format confidence numbers as percentages
        display_df["animal_conf"] = display_df["animal_conf"].apply(lambda x: f"{x * 100:.1f}%")
        display_df["breed_conf"] = display_df["breed_conf"].apply(lambda x: f"{x * 100:.1f}%" if pd.notnull(x) and x > 0 else "N/A")
        display_df.rename(columns={
            "id": "ID",
            "created_at": "Timestamp",
            "filename": "File Name",
            "animal": "Animal",
            "animal_conf": "Animal Conf",
            "breed": "Breed",
            "breed_conf": "Breed Conf",
            "feedback": "Feedback"
        }, inplace=True)

        st.dataframe(display_df, use_container_width=True, hide_index=True)

        # Download CSV button
        csv_bytes = df.to_csv(index=False).encode("utf-8")
        st.download_button(
            label="📥 Download History as CSV",
            data=csv_bytes,
            file_name="pet_predictions_history.csv",
            mime="text/csv"
        )
    else:
        st.info("No prediction history found matching the selected filters.")

    # Clear History section with confirmation
    st.markdown("---")
    with st.expander("🗑️ Clear Prediction History"):
        st.warning("Warning: This action will permanently delete all classification records from the database.")
        confirm_clear = st.checkbox("I confirm that I want to delete all history records.")
        if st.button("Delete All Records", type="secondary"):
            if confirm_clear:
                if database.clear_history():
                    st.success("History successfully cleared!")
                    st.rerun()
                else:
                    st.error("Could not clear history.")
            else:
                st.error("Please check the confirmation box before deleting.")


# ------------------------------------------------------------------------------
# PAGE 3: STATS
# ------------------------------------------------------------------------------
elif page == "📊 Stats":
    st.markdown("""
        <div class="neu-card">
            <h2 style="margin: 0; font-size: 1.6rem; font-weight: 800; color: #2d3350;">SQL-Powered Analytics</h2>
            <p style="margin: 6px 0 0 0; color: #555e7d; font-size: 0.95rem;">
                Real-time dashboard computed directly from SQLite aggregation queries. Click 'Show the SQL' to view the queries for viva examination.
            </p>
        </div>
    """, unsafe_allow_html=True)

    stats = database.get_stats()
    queries = stats.get("queries", {})

    # Top Metric Cards
    c1, c2, c3, c4 = st.columns(4, gap="medium")
    with c1:
        st.markdown(f"""
            <div class="neu-metric-card">
                <div class="neu-metric-value">{stats['total']}</div>
                <div class="neu-metric-label">Total Predictions</div>
            </div>
        """, unsafe_allow_html=True)
    with c2:
        st.markdown(f"""
            <div class="neu-metric-card">
                <div class="neu-metric-value">{stats['cats']}</div>
                <div class="neu-metric-label">Cats Identified</div>
            </div>
        """, unsafe_allow_html=True)
    with c3:
        st.markdown(f"""
            <div class="neu-metric-card">
                <div class="neu-metric-value">{stats['dogs']}</div>
                <div class="neu-metric-label">Dogs Identified</div>
            </div>
        """, unsafe_allow_html=True)
    with c4:
        st.markdown(f"""
            <div class="neu-metric-card">
                <div class="neu-metric-value">{stats['rejections']}</div>
                <div class="neu-metric-label">Rejections (Neither)</div>
            </div>
        """, unsafe_allow_html=True)

    with st.expander("🔍 Show the SQL: Total & Animal Counts"):
        st.code(f"-- 1. Total count query:\n{queries.get('total')}\n\n-- 2. Animal breakdown query:\n{queries.get('animal_counts')}\n\n-- 3. Rejections query:\n{queries.get('rejections')}", language="sql")

    # Detailed Charts and Analytics
    col_s1, col_s2 = st.columns([1, 1], gap="medium")

    with col_s1:
        with st.container(border=True):
            st.markdown("<h3 style='margin-top:0;'>🏆 Top 5 Most Predicted Breeds</h3>", unsafe_allow_html=True)
            top_breeds = stats.get("top_breeds", [])
            if top_breeds:
                top_df = pd.DataFrame(top_breeds, columns=["Breed", "Count"])
                st.bar_chart(data=top_df.set_index("Breed"), use_container_width=True, color="#6c63ff")
            else:
                st.info("No breed predictions recorded yet.")

        with st.expander("🔍 Show the SQL: Top 5 Breeds"):
            st.code(queries.get("top_breeds", "-- SQL query unavailable"), language="sql")

    with col_s2:
        with st.container(border=True):
            st.markdown("<h3 style='margin-top:0;'>🎯 User Feedback Accuracy</h3>", unsafe_allow_html=True)
            fb = stats.get("feedback_counts", {})
            correct = fb.get("Correct", 0)
            wrong = fb.get("Wrong", 0)
            unrated = fb.get("Unrated", 0)
            total_rated = correct + wrong

            acc_pct = (correct / total_rated * 100) if total_rated > 0 else 0.0

            st.markdown(f"""
                <div class="neu-inset" style="text-align: center;">
                    <h1 style="font-size: 2.8rem; color: #6c63ff; margin: 0;">{acc_pct:.1f}%</h1>
                    <p style="margin: 4px 0; color: #555e7d; font-weight: 600;">Accuracy on Rated Predictions</p>
                    <p style="font-size: 0.9rem; color: #717b9b; margin: 0;">
                        👍 {correct} Correct &nbsp;|&nbsp; 👎 {wrong} Wrong &nbsp;|&nbsp; ⏳ {unrated} Unrated
                    </p>
                </div>
            """, unsafe_allow_html=True)

            avg_conf = stats.get("avg_conf", {})
            if avg_conf:
                st.markdown("<p style='font-weight:600; margin-bottom: 4px;'>Average Confidence by Animal:</p>", unsafe_allow_html=True)
                for an, conf_val in avg_conf.items():
                    st.write(f"• **{an}**: {conf_val}%")

        with st.expander("🔍 Show the SQL: Feedback & Average Confidence"):
            st.code(f"-- Feedback query:\n{queries.get('feedback')}\n\n-- Average confidence query:\n{queries.get('avg_conf')}", language="sql")

    # Daily Predictions Timeline
    with st.container(border=True):
        st.markdown("<h3 style='margin-top:0;'>📅 Activity Over Time (Predictions per Day)</h3>", unsafe_allow_html=True)
        daily = stats.get("daily_counts", [])
        if daily:
            daily_df = pd.DataFrame(daily, columns=["Date", "Predictions"]).sort_values("Date")
            st.line_chart(data=daily_df.set_index("Date"), use_container_width=True, color="#6c63ff")
        else:
            st.info("No activity recorded yet.")

    with st.expander("🔍 Show the SQL: Daily Activity"):
        st.code(queries.get("daily", "-- SQL query unavailable"), language="sql")


# ------------------------------------------------------------------------------
# PAGE 4: BREED EXPLORER
# ------------------------------------------------------------------------------
elif page == "📖 Breed Explorer":
    st.markdown("""
        <div class="neu-card">
            <h2 style="margin: 0; font-size: 1.6rem; font-weight: 800; color: #2d3350;">Breed Explorer</h2>
            <p style="margin: 6px 0 0 0; color: #555e7d; font-size: 0.95rem;">
                Explore all 140+ cat and dog breeds registered in the SQLite database. Filter by animal species, size, or keywords.
            </p>
        </div>
    """, unsafe_allow_html=True)

    # Filters
    col_b1, col_b2, col_b3 = st.columns([1, 1, 2], gap="medium")
    with col_b1:
        an_sel = st.selectbox("Animal Species:", ["All", "Cat", "Dog"])
    with col_b2:
        size_sel = st.selectbox("Breed Size:", ["All", "Small", "Medium", "Large", "Giant"])
    with col_b3:
        search_kw = st.text_input("Search Breed or Origin:", "")

    breeds_list = database.get_all_breeds(an_sel, size_sel, search_kw)

    st.markdown(f"<p style='color: #555e7d; font-weight: 600;'>Showing {len(breeds_list)} breed(s):</p>", unsafe_allow_html=True)

    # Render breeds in a responsive 2-column grid
    col_left, col_right = st.columns(2, gap="medium")

    for i, b in enumerate(breeds_list):
        target_col = col_left if (i % 2 == 0) else col_right
        with target_col:
            emoji = "🐱" if b["animal"] == "Cat" else "🐶"
            st.markdown(f"""
                <div class="neu-card" style="margin-bottom: 16px;">
                    <div style="display: flex; justify-content: space-between; align-items: baseline;">
                        <h3 style="margin: 0; color: #2d3350;">{emoji} {b['name']}</h3>
                        <span class="neu-badge">{b['size']}</span>
                    </div>
                    <div class="neu-inset" style="margin-top: 10px; margin-bottom: 0;">
                        <p style="margin: 2px 0;"><b>🌍 Origin:</b> {b['origin']}</p>
                        <p style="margin: 2px 0;"><b>⏳ Lifespan:</b> {b['lifespan']}</p>
                        <p style="margin: 2px 0;"><b>🎭 Temperament:</b> {b['temperament']}</p>
                        <p style="margin: 6px 0 0 0; font-style: italic; color: #555e7d;">
                            <b>✨ Fact:</b> {b['fun_fact']}
                        </p>
                    </div>
                </div>
            """, unsafe_allow_html=True)


# ------------------------------------------------------------------------------
# PAGE 5: ABOUT
# ------------------------------------------------------------------------------
elif page == "ℹ️ About":
    st.markdown("""
        <div class="neu-card">
            <h2 style="margin: 0; font-size: 1.6rem; font-weight: 800; color: #2d3350;">About Pet Classifier</h2>
            <p style="margin: 6px 0 0 0; color: #555e7d; font-size: 0.95rem;">
                Class 12 Senior Secondary Computer Science Project demonstrating Deep Learning & Relational Database Integration.
            </p>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div class="neu-card">
            <h3 style="margin-top: 0; color: #6c63ff;">🚀 Shared Backbone + Linear Heads Pipeline</h3>
            <p style="color: #2d3350; line-height: 1.6;">
                Instead of running three separate ONNX sessions, this project implements a
                <b>shared-backbone architecture</b> that is faster and more memory-efficient:
            </p>
            <div class="neu-inset">
                <ol style="margin: 0; padding-left: 20px; line-height: 1.8;">
                    <li>
                        <b>Backbone: <code>models/backbone.onnx</code> (INT8, ~28 MB)</b><br>
                        A single <b>ConvNeXt-Tiny</b> ONNX session runs once per image and produces a
                        <b>768-dimensional feature vector</b>. This is the only neural-network forward pass —
                        loaded once at startup with <code>@st.cache_resource</code> and shared across all requests.
                    </li>
                    <li style="margin-top: 10px;">
                        <b>Linear Heads: <code>models/heads.npz</code> (three tiny weight matrices)</b><br>
                        Pure NumPy matrix multiplications applied to the feature vector — no extra ONNX sessions:<br>
                        • <b>Main head</b> (Cat, Dog + 3 rejection classes): rejection probabilities are summed to
                          decide <i>Neither</i>; otherwise the animal with the highest score advances.<br>
                        • <b>Cat head</b> (12 domestic breeds): runs only when the main head picks Cat.<br>
                        • <b>Dog head</b> (120 domestic breeds): runs only when the main head picks Dog.
                    </li>
                </ol>
            </div>
        </div>
    """, unsafe_allow_html=True)

    col_a1, col_a2 = st.columns([1, 1], gap="medium")

    with col_a1:
        st.markdown("""
            <div class="neu-card">
                <h3 style="margin-top: 0; color: #6c63ff;">⚙️ Model Optimization & Hosting</h3>
                <ul style="color: #2d3350; line-height: 1.7; padding-left: 20px;">
                    <li><b>Model Format:</b> ONNX (Open Neural Network Exchange).</li>
                    <li><b>Quantization:</b> INT8 precision (drastically reduces memory consumption and model file size below 30 MB).</li>
                    <li><b>Execution Engine:</b> ONNX Runtime with CPUExecutionProvider and graph optimization level <code>ORT_ENABLE_ALL</code>.</li>
                    <li><b>Concurrency Protection:</b> Python <code>threading.Semaphore(2)</code> prevents high traffic from overloading the free CPU cloud tier.</li>
                    <li><b>Caching:</b> Streamlit <code>@st.cache_resource</code> ensures neural network weights are parsed once on startup and reused for every user.</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)

    with col_a2:
        st.markdown("""
            <div class="neu-card">
                <h3 style="margin-top: 0; color: #6c63ff;">⚠️ Limitations & Project Scope</h3>
                <ul style="color: #2d3350; line-height: 1.7; padding-left: 20px;">
                    <li><b>Breed Vocabulary:</b> Trained strictly on 12 distinct cat breeds and 120 dog breeds from the Oxford-IIIT Pet and Stanford Dogs datasets.</li>
                    <li><b>Mixed Breeds:</b> Mixed-breed pets (mutts or crossbreeds) will be categorized towards their closest visual ancestor with reduced confidence.</li>
                    <li><b>Uncertainty Filter:</b> Any prediction with top-1 probability under 50% is automatically flagged with an "Uncertain" warning badge.</li>
                    <li><b>Database Privacy:</b> Images are processed entirely in volatile RAM and never written to disk; only classification metadata is logged in SQLite.</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)
