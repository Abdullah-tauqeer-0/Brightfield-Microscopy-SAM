import argparse
import os
import cv2
from brightfield_sam.models import build_sam
from brightfield_sam.inference import BrightfieldPredictor

def main():
    parser = argparse.ArgumentParser(description="Segment a folder of images")
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    
    os.makedirs(args.output, exist_ok=True)
    
    # Logic placeholder
    print(f"Segmenting from {args.input} to {args.output}")

if __name__ == "__main__":
    main()
