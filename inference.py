# ==============================================================================
# INFERENCE MODULE (inference.py)
# ==============================================================================
# This file contains the complete machine learning model pipeline.
#
# Supports TWO model architectures seamlessly:
# 1. Unified Backbone Architecture (from pet_classifier_retrain.ipynb):
#    - models/backbone.onnx (single shared ConvNeXt-Tiny feature extractor)
#    - models/heads.npz (linear classification heads: main_W/b, cat_W/b, dog_W/b)
#    - models/main_classes.json, cat_classes.json, dog_classes.json
#
# 2. Individual Specialists Architecture:
#    - models/main_model_int8.onnx, cat_specialist_int8.onnx, dog_specialist_int8.onnx
#
# Key Features:
# - Loads ONNX models using ONNX Runtime with CPU execution.
# - Uses Streamlit's @st.cache_resource to load models only once into memory.
# - Threading Semaphore(2) limits concurrent predictions to protect free cloud hosting.
# - Strict input preprocessing: 224x224 RGB float32 (raw 0-255 values, NHWC).
# - Exposes ONE clean function: classify(pil_image) -> dict
# ==============================================================================

import os
import json
import time
import threading
import numpy as np
from PIL import Image
import onnxruntime as ort
import streamlit as st

# Semaphore to limit concurrent inference requests to at most 2
CONCURRENCY_LIMIT = 2
SEMAPHORE = threading.Semaphore(CONCURRENCY_LIMIT)

# Model paths
MODEL_DIR = "models"

# 1. Unified Backbone setup
BACKBONE_PATH = os.path.join(MODEL_DIR, "backbone.onnx")
HEADS_PATH = os.path.join(MODEL_DIR, "heads.npz")

# 2. Individual models setup
MAIN_MODEL_PATH = os.path.join(MODEL_DIR, "main_model_int8.onnx")
CAT_MODEL_PATH = os.path.join(MODEL_DIR, "cat_specialist_int8.onnx")
DOG_MODEL_PATH = os.path.join(MODEL_DIR, "dog_specialist_int8.onnx")

# Common class files
MAIN_CLASSES_PATH = os.path.join(MODEL_DIR, "main_classes.json")
CAT_CLASSES_PATH = os.path.join(MODEL_DIR, "cat_classes.json")
DOG_CLASSES_PATH = os.path.join(MODEL_DIR, "dog_classes.json")


def format_breed_name(raw_name):
    """
    Cleans up raw breed names for display:
    Replaces underscores and hyphens with spaces, and applies title case.
    Example: 'maine_coon' -> 'Maine Coon'
    """
    if not raw_name:
        return "Unknown"
    return str(raw_name).replace("_", " ").replace("-", " ").strip().title()


def detect_model_architecture():
    """
    Detects which model format is present in the models/ folder:
    - 'backbone': backbone.onnx + heads.npz (Recommended, from retrain notebook)
    - 'separate': 3 distinct ONNX models
    - 'missing': required files not found
    """
    # Check classes first
    for f in [MAIN_CLASSES_PATH, CAT_CLASSES_PATH, DOG_CLASSES_PATH]:
        if not os.path.exists(f):
            return "missing", f

    # Check for unified backbone
    if os.path.exists(BACKBONE_PATH) and os.path.exists(HEADS_PATH):
        return "backbone", None

    # Check for separate models
    if os.path.exists(MAIN_MODEL_PATH) and os.path.exists(CAT_MODEL_PATH) and os.path.exists(DOG_MODEL_PATH):
        return "separate", None

    return "missing", BACKBONE_PATH


@st.cache_resource(show_spinner="Loading machine learning models...")
def load_all_models():
    """
    Loads models and class labels once into memory with ONNX Runtime CPU session options.
    """
    arch_type, missing_file = detect_model_architecture()
    if arch_type == "missing":
        raise FileNotFoundError(f"Missing required model file: {missing_file}")

    # Configure ONNX Runtime session options
    opts = ort.SessionOptions()
    opts.intra_op_num_threads = 2
    opts.inter_op_num_threads = 1
    opts.graph_optimization_level = ort.GraphOptimizationLevel.ORT_ENABLE_ALL
    providers = ["CPUExecutionProvider"]

    # Load class labels
    with open(MAIN_CLASSES_PATH, "r", encoding="utf-8") as f:
        main_classes = json.load(f)
    with open(CAT_CLASSES_PATH, "r", encoding="utf-8") as f:
        cat_classes = json.load(f)
    with open(DOG_CLASSES_PATH, "r", encoding="utf-8") as f:
        dog_classes = json.load(f)

    # Load models based on architecture
    try:
        if arch_type == "backbone":
            backbone_session = ort.InferenceSession(BACKBONE_PATH, sess_options=opts, providers=providers)
            heads = np.load(HEADS_PATH)
            return {
                "arch": "backbone",
                "backbone_session": backbone_session,
                "heads": heads,
                "main_classes": main_classes,
                "cat_classes": cat_classes,
                "dog_classes": dog_classes,
                "is_dummy": False
            }
        else:
            main_session = ort.InferenceSession(MAIN_MODEL_PATH, sess_options=opts, providers=providers)
            cat_session = ort.InferenceSession(CAT_MODEL_PATH, sess_options=opts, providers=providers)
            dog_session = ort.InferenceSession(DOG_MODEL_PATH, sess_options=opts, providers=providers)
            return {
                "arch": "separate",
                "main_session": main_session,
                "cat_session": cat_session,
                "dog_session": dog_session,
                "main_classes": main_classes,
                "cat_classes": cat_classes,
                "dog_classes": dog_classes,
                "is_dummy": False
            }
    except Exception as e:
        raise RuntimeError(f"Could not load the ONNX models: {e}")


def preprocess_image(pil_img):
    """
    Preprocesses a PIL Image EXACTLY as specified in training:
    1. Converts image to RGB.
    2. Resizes to 224x224.
    3. Converts to float32 with raw pixel values 0-255 (NO /255, NO mean/std).
    4. Adds batch dimension -> Shape: (1, 224, 224, 3) with NHWC layout.
    """
    rgb_img = pil_img.convert("RGB")
    resized_img = rgb_img.resize((224, 224), Image.Resampling.BILINEAR)
    img_array = np.array(resized_img, dtype=np.float32)
    batch_img = np.expand_dims(img_array, axis=0)
    return batch_img


def softmax(x):
    """Computes numerically stable softmax over a 1D numpy array."""
    shift_x = x - np.max(x)
    exps = np.exp(shift_x)
    return exps / np.sum(exps)


def _simulate_preview_prediction(pil_img, main_classes, cat_classes, dog_classes):
    """Fallback classification when models are being trained or updated."""
    time.sleep(0.08)
    small = pil_img.resize((10, 10))
    pixels = np.array(small)
    avg_color = np.mean(pixels)

    if len(main_classes) == 2:
        is_dog = (avg_color % 2 > 0.8)
        animal = "Dog" if is_dog else "Cat"
        animal_conf = 0.88 + (avg_color % 10) / 100.0
    else:
        animal = "Dog" if avg_color > 120 else "Cat"
        animal_conf = 0.91

    classes = dog_classes if animal == "Dog" else cat_classes
    n_classes = len(classes)

    base_idx = int(avg_color * 7) % n_classes
    idx1 = base_idx
    idx2 = (base_idx + 3) % n_classes
    idx3 = (base_idx + 7) % n_classes

    breed_conf = 0.78 + (avg_color % 15) / 100.0
    conf2 = (1.0 - breed_conf) * 0.65
    conf3 = (1.0 - breed_conf) * 0.35

    top3 = [
        (format_breed_name(classes[idx1]), round(float(breed_conf), 4)),
        (format_breed_name(classes[idx2]), round(float(conf2), 4)),
        (format_breed_name(classes[idx3]), round(float(conf3), 4)),
    ]

    return {
        "animal": animal,
        "animal_conf": round(float(animal_conf), 4),
        "breed": top3[0][0],
        "breed_conf": top3[0][1],
        "top3": top3,
        "uncertain": False
    }


def classify(pil_image):
    """
    Classifies a pet image using the two-stage ONNX pipeline.
    
    Returns:
        dict: {
            "animal": "Cat" | "Dog" | "Neither",
            "animal_conf": float,
            "breed": str | None,
            "breed_conf": float | None,
            "top3": list of (name, prob),
            "uncertain": bool,
            "seconds": float
        }
    """
    acquired = SEMAPHORE.acquire(blocking=False)
    if not acquired:
        raise RuntimeError("The classifier is busy processing other requests right now. Please try again in a moment!")

    start_time = time.time()

    try:
        models = load_all_models()
        main_classes = models["main_classes"]
        cat_classes = models["cat_classes"]
        dog_classes = models["dog_classes"]

        if models["is_dummy"]:
            result = _simulate_preview_prediction(pil_image, main_classes, cat_classes, dog_classes)
            result["seconds"] = round(time.time() - start_time, 3)
            return result

        input_data = preprocess_image(pil_image)

        # ======================================================================
        # PIPELINE A: Unified Backbone Architecture (from retrain notebook)
        # ======================================================================
        if models["arch"] == "backbone":
            sess = models["backbone_session"]
            heads = models["heads"]
            in_name = sess.get_inputs()[0].name

            # Extract 768-dim feature vector once
            feat = sess.run(None, {in_name: input_data})[0].flatten()

            # Main model prediction
            pm = softmax(feat @ heads["main_W"] + heads["main_b"])

            # Detect rejection classes
            reject_cols = [i for i, c in enumerate(main_classes) if str(c).lower().startswith(("rejection", "other"))]

            p_cat = float(pm[0])
            p_dog = float(pm[1])
            p_rej = float(pm[reject_cols].sum()) if reject_cols else 0.0

            if reject_cols and p_rej >= p_cat and p_rej >= p_dog:
                return {
                    "animal": "Neither",
                    "animal_conf": round(p_rej, 4),
                    "breed": None,
                    "breed_conf": None,
                    "top3": [],
                    "uncertain": False,
                    "seconds": round(time.time() - start_time, 3)
                }

            if p_cat >= p_dog:
                animal = "Cat"
                animal_conf = p_cat
                spec_probs = softmax(feat @ heads["cat_W"] + heads["cat_b"])
                spec_classes = cat_classes
            else:
                animal = "Dog"
                animal_conf = p_dog
                spec_probs = softmax(feat @ heads["dog_W"] + heads["dog_b"])
                spec_classes = dog_classes

        # ======================================================================
        # PIPELINE B: Separate Specialist Models Architecture
        # ======================================================================
        else:
            main_sess = models["main_session"]
            main_in_name = main_sess.get_inputs()[0].name
            main_out = np.array(main_sess.run(None, {main_in_name: input_data})[0]).flatten()

            if len(main_classes) == 2:
                score = float(main_out[0])
                if score > 0.5:
                    animal, animal_conf = "Dog", score
                else:
                    animal, animal_conf = "Cat", 1.0 - score
            else:
                main_probs = softmax(main_out)
                p_reject = sum(main_probs[i] for i, name in enumerate(main_classes) if str(name).lower().startswith(("rejection", "other")))
                p_cat = sum(main_probs[i] for i, name in enumerate(main_classes) if str(name).lower() == "cat")
                p_dog = sum(main_probs[i] for i, name in enumerate(main_classes) if str(name).lower() == "dog")

                if p_reject >= p_cat and p_reject >= p_dog:
                    return {
                        "animal": "Neither",
                        "animal_conf": round(float(p_reject), 4),
                        "breed": None,
                        "breed_conf": None,
                        "top3": [],
                        "uncertain": False,
                        "seconds": round(time.time() - start_time, 3)
                    }
                elif p_cat >= p_dog:
                    animal, animal_conf = "Cat", p_cat
                else:
                    animal, animal_conf = "Dog", p_dog

            spec_session = models["cat_session"] if animal == "Cat" else models["dog_session"]
            spec_classes = cat_classes if animal == "Cat" else dog_classes
            spec_in_name = spec_session.get_inputs()[0].name
            spec_out = np.array(spec_session.run(None, {spec_in_name: input_data})[0]).flatten()
            spec_probs = softmax(spec_out)

        # Common Top-3 breed processing
        top3_indices = np.argsort(spec_probs)[-3:][::-1]
        top3 = []
        for idx in top3_indices:
            name = format_breed_name(spec_classes[idx])
            prob = round(float(spec_probs[idx]), 4)
            top3.append((name, prob))

        top_breed = top3[0][0]
        top_conf = top3[0][1]
        uncertain = bool(top_conf < 0.50)

        return {
            "animal": animal,
            "animal_conf": round(float(animal_conf), 4),
            "breed": top_breed,
            "breed_conf": top_conf,
            "top3": top3,
            "uncertain": uncertain,
            "seconds": round(time.time() - start_time, 3)
        }

    finally:
        SEMAPHORE.release()
