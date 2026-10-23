# ==============================================================================
# NEUMORPHIC STYLING MODULE (styles.py)
# ==============================================================================
# This file defines the Neumorphic (Soft UI) design system for the Pet Classifier.
#
# Design System Rules:
# - Background: #e0e5ec
# - Text: #2d3350 (Dark, high contrast, easy readability)
# - Accent: #6c63ff (Primary buttons, active highlights, confidence bar)
# - Raised Shadow: 9px 9px 16px #a3b1c6, -9px -9px 16px #ffffff (20px radius)
# - Inset Shadow: inset 5px 5px 10px #b8b9be, inset -5px -5px 10px #ffffff
# - No hard borders anywhere
# - Smooth 0.2s transitions
# ==============================================================================

NEUMORPHIC_CSS = """
<style>
/* 1. Global Font and Background Setup */
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');

/* Apply custom font ONLY to text elements — never to icon spans */
body,
p,
label,
input,
textarea,
button,
h1, h2, h3, h4, h5, h6,
.stMarkdown,
.stMarkdown *,
[data-testid="stSidebar"] *,
[data-testid="stHeader"] *,
[data-testid="stExpander"] summary,
.stButton > button,
.stTextInput > div > div > input,
.stTextArea > div > div > textarea,
.stSelectbox label,
.stSelectbox [data-baseweb="select"] [data-baseweb="value"],
.stSelectbox [data-baseweb="select"] span:not([data-testid="stIconMaterial"]),
.stRadio label,
.stCheckbox label {
    font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif !important;
    color: #2d3350;
}

/* Preserve Material Symbols icon font — must not be overridden */
[data-testid="stIconMaterial"],
span[class*="material-symbols"],
span[class*="material-icons"],
.stExpanderToggleIcon,
[data-testid="stFileUploaderDropzone"] span[aria-hidden="true"] {
    font-family: 'Material Symbols Rounded' !important;
    color: inherit;
}

/* Background for the entire page */
.stApp {
    background-color: #e0e5ec !important;
}

/* Sidebar background */
[data-testid="stSidebar"] {
    background-color: #e0e5ec !important;
    box-shadow: 5px 0 15px #c8d0de !important;
    border-right: none !important;
    z-index: 50 !important;
}

[data-testid="stAppViewContainer"] {
    z-index: 60 !important;
}

/* Header transparency */
header[data-testid="stHeader"] {
    background-color: transparent !important;
}

/* 2. Custom Neumorphic Component Classes */

/* Raised Card */
.neu-card {
    background: #e0e5ec;
    border-radius: 20px;
    box-shadow: 9px 9px 16px #a3b1c6, -9px -9px 16px #ffffff;
    padding: 24px;
    margin-bottom: 24px;
    border: none;
    transition: all 0.2s ease-in-out;
}

.neu-card:hover {
    box-shadow: 11px 11px 20px #98a6bb, -11px -11px 20px #ffffff;
}

/* Inset / Sunken Container (for inputs, stats inner panels, info blocks) */
.neu-inset {
    background: #e0e5ec;
    border-radius: 16px;
    box-shadow: inset 5px 5px 10px #b8b9be, inset -5px -5px 10px #ffffff;
    padding: 18px;
    margin-bottom: 16px;
    border: none;
}

/* Neumorphic Metric Box */
.neu-metric-card {
    background: #e0e5ec;
    border-radius: 20px;
    box-shadow: 8px 8px 15px #a3b1c6, -8px -8px 15px #ffffff;
    padding: 20px;
    text-align: center;
    margin-bottom: 18px;
    transition: transform 0.2s ease-in-out;
}

.neu-metric-card:hover {
    transform: translateY(-2px);
}

.neu-metric-value {
    font-size: 2.2rem;
    font-weight: 800;
    color: #6c63ff;
    margin-bottom: 4px;
}

.neu-metric-label {
    font-size: 0.95rem;
    font-weight: 600;
    color: #555e7d;
}

/* Neumorphic Badge / Pill */
.neu-badge {
    display: inline-block;
    padding: 6px 16px;
    border-radius: 50px;
    background: #e0e5ec;
    box-shadow: 4px 4px 8px #a3b1c6, -4px -4px 8px #ffffff;
    font-size: 0.85rem;
    font-weight: 700;
    color: #6c63ff;
    margin-right: 8px;
    margin-bottom: 8px;
}

/* Neumorphic Custom Progress Bar */
.neu-progress-track {
    background: #e0e5ec;
    border-radius: 14px;
    box-shadow: inset 4px 4px 8px #b8b9be, inset -4px -4px 8px #ffffff;
    height: 18px;
    width: 100%;
    overflow: hidden;
    margin: 8px 0 16px 0;
}

.neu-progress-fill {
    background: linear-gradient(90deg, #6c63ff, #8b83ff);
    height: 100%;
    border-radius: 14px;
    box-shadow: 2px 2px 5px rgba(108, 99, 255, 0.4);
    transition: width 0.5s ease-in-out;
}

/* 3. Styling Native Streamlit Elements */

/* Buttons */
.stButton > button {
    background: #e0e5ec !important;
    color: #2d3350 !important;
    border-radius: 16px !important;
    border: none !important;
    box-shadow: 6px 6px 12px #a3b1c6, -6px -6px 12px #ffffff !important;
    font-weight: 700 !important;
    padding: 10px 24px !important;
    transition: all 0.2s ease-in-out !important;
}

.stButton > button:hover {
    box-shadow: 3px 3px 6px #a3b1c6, -3px -3px 6px #ffffff !important;
    transform: translateY(1px);
    color: #6c63ff !important;
}

.stButton > button:active {
    box-shadow: inset 4px 4px 8px #b8b9be, inset -4px -4px 8px #ffffff !important;
}

/* Primary Button Accent */
.stButton > button[kind="primary"] {
    background: #6c63ff !important;
    color: #ffffff !important;
    box-shadow: 6px 6px 14px rgba(108, 99, 255, 0.4), -6px -6px 14px #ffffff !important;
}

.stButton > button[kind="primary"]:hover {
    background: #5b52f2 !important;
    color: #ffffff !important;
}

/* Text Inputs and Textareas — inset neumorphic, visible text */
.stTextInput > div > div > input,
.stTextArea > div > div > textarea {
    background: #e0e5ec !important;
    border-radius: 14px !important;
    border: none !important;
    box-shadow: inset 4px 4px 8px #b8b9be, inset -4px -4px 8px #ffffff !important;
    color: #2d3350 !important;
    padding: 10px 14px !important;
}

/* Selectbox — inset look, but DO NOT override padding so the selected value is visible */
.stSelectbox [data-baseweb="select"] > div:first-child {
    background: #e0e5ec !important;
    border-radius: 14px !important;
    border: none !important;
    box-shadow: inset 4px 4px 8px #b8b9be, inset -4px -4px 8px #ffffff !important;
    color: #2d3350 !important;
    min-height: 44px !important;
}

/* File Uploader and Camera Dropzones */
[data-testid="stFileUploader"] section {
    background: #e0e5ec !important;
    border-radius: 20px !important;
    border: none !important;
    box-shadow: inset 5px 5px 10px #b8b9be, inset -5px -5px 10px #ffffff !important;
    padding: 24px !important;
}

/* Streamlit Native Progress Bar Track */
.stProgress > div > div > div > div {
    background: linear-gradient(90deg, #6c63ff, #8a83ff) !important;
    border-radius: 12px !important;
}

.stProgress > div > div > div {
    background: #e0e5ec !important;
    box-shadow: inset 3px 3px 6px #b8b9be, inset -3px -3px 6px #ffffff !important;
    border-radius: 12px !important;
    height: 14px !important;
}

/* Expanders */
[data-testid="stExpander"] {
    background: #e0e5ec !important;
    border-radius: 16px !important;
    border: none !important;
    box-shadow: 6px 6px 12px #a3b1c6, -6px -6px 12px #ffffff !important;
    margin-top: 12px !important;
    margin-bottom: 12px !important;
}

[data-testid="stExpander"] summary {
    font-weight: 700 !important;
    color: #2d3350 !important;
}

/* Code Blocks */
.stCodeBlock, code, pre {
    background: #d8dee8 !important;
    color: #2d3350 !important;
    border-radius: 12px !important;
    border: none !important;
    box-shadow: inset 3px 3px 6px #b8b9be, inset -3px -3px 6px #ffffff !important;
    font-family: 'Consolas', 'Courier New', monospace !important;
}

/* 4. st.container(border=True) — styled as neu-card */
/* Streamlit wraps bordered containers in a div with data-testid="stVerticalBlockBorderWrapper" */
[data-testid="stVerticalBlockBorderWrapper"] {
    background: #e0e5ec !important;
    border-radius: 20px !important;
    border: none !important;
    box-shadow: 9px 9px 16px #a3b1c6, -9px -9px 16px #ffffff !important;
    padding: 20px !important;
    margin-bottom: 20px !important;
    transition: all 0.2s ease-in-out !important;
    overflow: hidden !important;
}

[data-testid="stVerticalBlockBorderWrapper"]:hover {
    box-shadow: 11px 11px 20px #98a6bb, -11px -11px 20px #ffffff !important;
}

/* Image Preview: natural aspect ratio, centered, max-height 380px, never overflows box */
[data-testid="stImage"] {
    display: flex !important;
    justify-content: center !important;
    align-items: center !important;
    width: 100% !important;
    overflow: hidden !important;
}

[data-testid="stImage"] > img,
[data-testid="stImage"] img {
    max-width: 100% !important;
    max-height: 380px !important;
    width: auto !important;
    height: auto !important;
    object-fit: contain !important;
    border-radius: 12px !important;
    display: block !important;
    margin: 0 auto !important;
}

/* Sidebar collapse & expand toggle buttons — larger and touch-friendly */
[data-testid="collapsedControl"],
[data-testid="stSidebarCollapseButton"] {
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
}

[data-testid="collapsedControl"] button,
[data-testid="stSidebarCollapseButton"] button {
    background: #e0e5ec !important;
    border-radius: 12px !important;
    box-shadow: 3px 3px 7px #a3b1c6, -3px -3px 7px #ffffff !important;
    min-width: 44px !important;
    min-height: 44px !important;
    width: 44px !important;
    height: 44px !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    border: none !important;
    color: #6c63ff !important;
    padding: 0 !important;
    margin: 4px !important;
}

[data-testid="collapsedControl"] button:hover,
[data-testid="stSidebarCollapseButton"] button:hover {
    box-shadow: inset 2px 2px 5px #b8b9be, inset -2px -2px 5px #ffffff !important;
}

[data-testid="collapsedControl"] svg,
[data-testid="stSidebarCollapseButton"] svg {
    width: 24px !important;
    height: 24px !important;
}

/* Sidebar responsive mobile width */
@media (max-width: 768px) {
    [data-testid="stSidebar"] {
        max-width: 82vw !important;
    }
}

/* Responsive Columns: Stacks nicely on smaller screens */
@media (max-width: 768px) {
    .neu-card {
        padding: 16px;
    }
    .neu-metric-value {
        font-size: 1.8rem;
    }
}

/* ===== Sidebar navigation as neumorphic buttons ===== */
[data-testid="stSidebar"] div[role="radiogroup"] {
    gap: 14px !important;
    width: 100%;
}

[data-testid="stSidebar"] div[role="radiogroup"] > label {
    position: relative;
    width: 100%;
    margin: 0 !important;
    padding: 12px 16px !important;
    background: #e0e5ec;
    border-radius: 14px;
    box-shadow: 6px 6px 12px #a3b1c6, -6px -6px 12px #ffffff;
    cursor: pointer;
    transition: all 0.2s ease-in-out;
}

/* hide the round radio dot */
[data-testid="stSidebar"] div[role="radiogroup"] > label > div:first-child {
    display: none !important;
}

[data-testid="stSidebar"] div[role="radiogroup"] > label p {
    margin: 0;
    font-size: 0.95rem;
    font-weight: 700;
    color: #2d3350 !important;
}

[data-testid="stSidebar"] div[role="radiogroup"] > label:hover {
    box-shadow: 3px 3px 6px #a3b1c6, -3px -3px 6px #ffffff;
    transform: translateY(1px);
}

/* selected page: pressed in, accent text, glowing line at the bottom */
[data-testid="stSidebar"] div[role="radiogroup"] > label:has(input:checked) {
    box-shadow: inset 4px 4px 8px #b8b9be, inset -4px -4px 8px #ffffff;
}

[data-testid="stSidebar"] div[role="radiogroup"] > label:has(input:checked) p {
    color: #6c63ff !important;
    font-weight: 800;
}

[data-testid="stSidebar"] div[role="radiogroup"] > label:has(input:checked)::after {
    content: "";
    position: absolute;
    left: 20%;
    right: 20%;
    bottom: 5px;
    height: 3px;
    border-radius: 3px;
    background: #6c63ff;
    box-shadow: 0 0 8px 2px rgba(108, 99, 255, 0.65);
}

/* ===== Limits footer — displays cleanly at bottom of page content ===== */
.limits-footer {
    position: relative !important;
    margin: 48px auto 24px auto !important;
    background: #e0e5ec;
    border-radius: 20px;
    box-shadow: 6px 6px 16px #a3b1c6, -6px -6px 16px #ffffff;
    border: 1px solid rgba(255, 255, 255, 0.7);
    padding: 14px 24px;
    text-align: center;
    font-size: 0.8rem;
    font-weight: 600;
    color: #434c6e;
    letter-spacing: 0.01em;
    width: fit-content;
    max-width: 95%;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    gap: 4px;
    clear: both !important;
}

.limits-footer b {
    color: #2d3350;
    font-weight: 700;
}

.limits-footer span {
    color: #6c63ff;
    font-weight: 700;
}

.limits-footer .limits-explain {
    font-size: 0.72rem;
    font-weight: 500;
    color: #636d8d;
}
</style>
"""
