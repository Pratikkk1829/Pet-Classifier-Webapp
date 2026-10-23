# ==============================================================================
# PIPELINE SELF-TEST SCRIPT (test_pipeline.py)
# ==============================================================================
# This script tests the inference pipeline from the command line.
#
# Usage:
#   python test_pipeline.py <path_to_image>
# Example:
#   python test_pipeline.py sample.jpg
# ==============================================================================

import sys
import os
from PIL import Image
import inference

def main():
    # 1. Check if image path argument is provided
    if len(sys.argv) < 2:
        print("=" * 60)
        print("Pet Classifier Pipeline Self-Test")
        print("=" * 60)
        print("Usage: python test_pipeline.py <path_to_image>")
        print("No image path provided. Creating a temporary test image...")
        
        test_path = "temp_test_image.jpg"
        # Create a 300x300 RGB test image
        test_img = Image.new("RGB", (300, 300), color=(200, 150, 100))
        test_img.save(test_path)
        image_path = test_path
        cleanup_temp = True
    else:
        image_path = sys.argv[1]
        cleanup_temp = False

    # 2. Check that the file exists
    if not os.path.exists(image_path):
        print(f"Error: File '{image_path}' not found.")
        sys.exit(1)

    print(f"\n[1/3] Loading image: {image_path}")
    try:
        # Validate image with PIL
        with Image.open(image_path) as img:
            img.verify()
        # Reopen after verify
        pil_img = Image.open(image_path)
        print(f"      Image format: {pil_img.format}, Size: {pil_img.size}, Mode: {pil_img.mode}")
    except Exception as e:
        print(f"Error: Invalid or corrupt image file ({e}).")
        sys.exit(1)

    # 3. Run classification
    print("\n[2/3] Running two-stage classification...")
    try:
        result = inference.classify(pil_img)
    except Exception as e:
        print(f"Classification failed: {e}")
        sys.exit(1)

    # 4. Print results
    print("\n[3/3] Classification Results:")
    print("-" * 40)
    print(f"Animal:        {result.get('animal')}")
    print(f"Confidence:    {result.get('animal_conf') * 100:.2f}%")
    print(f"Breed:         {result.get('breed') or 'N/A'}")
    if result.get('breed_conf') is not None:
        print(f"Breed Conf:    {result.get('breed_conf') * 100:.2f}%")
    print(f"Uncertain:     {result.get('uncertain')}")
    print(f"Latency:       {result.get('seconds')} seconds")
    
    top3 = result.get("top3", [])
    if top3:
        print("\nTop-3 Predictions:")
        for rank, (name, prob) in enumerate(top3, 1):
            print(f"  {rank}. {name:<25} ({prob * 100:.2f}%)")
    print("-" * 40)

    # Clean up temporary test file if created
    if cleanup_temp and os.path.exists(test_path):
        os.remove(test_path)

if __name__ == "__main__":
    main()
