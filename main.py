import subprocess
import os

def run_pipeline():
    print("====================================")
    print("   COMPUTER VISION PIPELINE START   ")
    print("====================================\n")

    # Step 1: Extract Frames from Video
    print("[STEP 1/2] Extracting raw frames from video...")
    subprocess.run(["python", "extract_frames.py"])

    print("\n------------------------------------\n")

    # Step 2: Filter Motion Frames using Background Subtraction
    print("[STEP 2/2] Filtering motion frames...")
    subprocess.run(["python", "motion_detection.py"])

    print("\n====================================")
    print("   PIPELINE COMPLETED SUCCESSFULLY  ")
    print("====================================")

    # Summary Check
    if os.path.exists("data/motion_frames"):
        count = len(os.listdir("data/motion_frames"))
        print(f"\nFinal Result: {count} motion frames ready in 'data/motion_frames/'.")

if __name__ == "__main__":
    run_pipeline()