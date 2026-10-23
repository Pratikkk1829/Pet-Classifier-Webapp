# 🐾 Pet Classifier - Class 12 Computer Science Project

An AI-powered web application built with **Streamlit**, **ONNX Runtime**, and **SQLite** that classifies domestic cats and dogs and predicts their exact breed using a shared-backbone deep learning pipeline.

---

## 🌟 Project Highlights

- **Shared Backbone + Linear Heads Architecture:**
  - **ONE ONNX Session** (`models/backbone.onnx`, INT8, ~28 MB): A ConvNeXt-Tiny backbone runs once per image and produces a 768-number feature vector.
  - **Three NumPy Heads** (`models/heads.npz`): Tiny linear classifiers applied to the feature vector — no extra ONNX overhead.
    - *Main head*: Cat vs Dog vs Neither (rejection); rejection probabilities are summed to decide "Neither".
    - *Cat head*: 12 domestic cat breeds.
    - *Dog head*: 120 domestic dog breeds.
- **Relational Database Integration:** Every prediction, confidence score, and user feedback is saved in a local SQLite database (`pets.db`) using standard SQL queries (`INSERT`, `SELECT`, `UPDATE`, `GROUP BY`, `AVG`).
- **Neumorphic (Soft UI) Design:** Elegant, modern raised and inset shadows, smooth transitions, mobile-responsive layout, and high contrast typography.
- **Production-Ready & Safe:** Upload validation (5 MB limit, PIL verification, decompression bomb prevention, auto-downscaling to 1024px), concurrency limiting with `threading.Semaphore(2)` to protect free cloud hosting, and `@st.cache_resource` memory caching.
- **Viva-Ready:** An interactive "Show the SQL" expander under every metric on the Stats page so the student can explain the exact queries during examination.

---

## 📂 Project Structure

```text
Pet Classifier Webapp/
├── .streamlit/
│   └── config.toml          # Forced light theme and 5 MB upload limit
├── models/
│   ├── backbone.onnx        # Shared ConvNeXt-Tiny backbone (INT8, ~28 MB) — ONE ONNX session
│   ├── heads.npz            # Three linear heads: main (Cat/Dog/Neither), cat (12 breeds), dog (120 breeds)
│   ├── main_classes.json    # Main head class labels
│   ├── cat_classes.json     # Cat breed names (12)
│   └── dog_classes.json     # Dog breed names (120)
├── app.py                   # Main Streamlit UI with 5 sidebar pages
├── inference.py             # Preprocessing, ONNX backbone session, NumPy head inference
├── database.py              # SQLite database creation, queries, and analytics
├── breeds_seed.py           # Educational dataset for 140+ cat and dog breeds
├── styles.py                # Neumorphic CSS design system
├── test_pipeline.py         # Standalone CLI test script
├── requirements.txt         # Pinned dependencies (streamlit, onnxruntime, numpy, pillow)
└── README.md                # Project documentation and viva guide
```

---

## 💻 How to Run Locally

### 1. Prerequisites
- Python 3.11 installed on your computer.
- Git (optional, for cloning).

### 2. Install Dependencies
Open your terminal or command prompt in the project folder and run:
```bash
pip install -r requirements.txt
```

### 3. Run the Self-Test Script
To test the machine learning pipeline from the command line:
```bash
python test_pipeline.py
```
Or test with any custom image file:
```bash
python test_pipeline.py path/to/pet_image.jpg
```

### 4. Launch the Web Application
Start the Streamlit application by running:
```bash
streamlit run app.py
```
The app will automatically open in your default web browser at `http://localhost:8501`.

---

## ☁️ How to Deploy on Streamlit Community Cloud (Free)

Streamlit Community Cloud allows you to host this web app completely free with a public URL:

1. **Commit Code and Models to GitHub:**
   - The backbone is quantized to INT8 (~28 MB) — well within GitHub's 100 MB file limit.
   - Commit and push all files to your GitHub repository:
     ```bash
     git add .
     git commit -m "Deploy Pet Classifier app"
     git push origin main
     ```

2. **Deploy on Streamlit Community Cloud:**
   - Go to [share.streamlit.io](https://share.streamlit.io) and sign in with your GitHub account.
   - Click **"New app"**.
   - Select your repository (`Pet Classifier Webapp`), branch (`main`), and set the main file path to:
     ```text
     app.py
     ```
   - Click **"Deploy"**!
   - Streamlit will automatically read `requirements.txt`, install dependencies, load the ONNX backbone, and launch the web app.

---

## 📖 Viva Voce & Presentation Guide

### 1. Why use a shared backbone instead of three separate ONNX models?
> **Answer:** Loading three separate ONNX sessions would triple the RAM usage and triple cold-start time. Instead, one ConvNeXt-Tiny ONNX session (`backbone.onnx`, ~28 MB, INT8) runs once per image and outputs a 768-dimensional feature vector. Three tiny NumPy linear heads (stored in `heads.npz`) then classify from that vector — no extra ONNX overhead. This saves ~56 MB of RAM and makes each request faster.

### 2. How does the application prevent server crashes on free hosting?
> **Answer:**
> 1. **Model Caching:** `@st.cache_resource` loads the ONNX backbone once when the app boots up, keeping it in RAM rather than reloading ~28 MB on every button click.
> 2. **Concurrency Limiting:** `threading.Semaphore(2)` limits simultaneous inferences to 2. If a third user tries to classify simultaneously, the app returns a friendly "server busy" message instead of crashing the CPU.
> 3. **Image Sanitization:** Upload size is capped at 5 MB, validated with PIL `verify()`, protected against decompression bombs, and downscaled to a maximum of 1024px before inference.

### 3. Key SQL Queries Used in the Project
- **Total Count:**
  ```sql
  SELECT COUNT(*) FROM predictions;
  ```
- **Predictions per Animal (GROUP BY):**
  ```sql
  SELECT animal, COUNT(*) FROM predictions GROUP BY animal;
  ```
- **Top 5 Predicted Breeds:**
  ```sql
  SELECT breed, COUNT(*) AS count 
  FROM predictions 
  WHERE breed IS NOT NULL AND breed != '' 
  GROUP BY breed 
  ORDER BY count DESC 
  LIMIT 5;
  ```
- **Average Confidence per Species (AVG):**
  ```sql
  SELECT animal, AVG(animal_conf) FROM predictions GROUP BY animal;
  ```
- **Filtering by Animal and Wrong Feedback (WHERE with Parameterized Query):**
  ```sql
  SELECT * FROM predictions WHERE animal = ? AND feedback = 'Wrong' ORDER BY id DESC;
  ```
- **Updating Feedback:**
  ```sql
  UPDATE predictions SET feedback = ? WHERE id = ?;
  ```

---

## 📄 License & Attribution
- Built for senior secondary school computer science curriculum.
- Free to modify and present for academic purposes.
