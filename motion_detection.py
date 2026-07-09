import cv2
import os

# Set relative directory paths
FRAMES_DIR = "data/raw_frames"
MOTION_OUT_DIR = "data/motion_frames"

# Create output folder for motion frames
os.makedirs(MOTION_OUT_DIR, exist_ok=True)

# Initialize MOG2 Background Subtractor
back_sub = cv2.createBackgroundSubtractorMOG2(history=500, varThreshold=50, detectShadows=True)

# Get sorted list of extracted frames
frame_files = sorted(os.listdir(FRAMES_DIR))

saved_motion_count = 0

print("Starting motion detection filtering...")

for file_name in frame_files:
    if not file_name.lower().endswith(('.jpg', '.png', '.jpeg')):
        continue

    frame_path = os.path.join(FRAMES_DIR, file_name)
    frame = cv2.imread(frame_path)

    if frame is None:
        continue

    # Apply background subtraction
    fg_mask = back_sub.apply(frame)

    # Count white pixels (indicates movement/motion)
    motion_pixels = cv2.countNonZero(fg_mask)

    # Save frame only if significant motion is detected
    if motion_pixels > 5000:
        out_path = os.path.join(MOTION_OUT_DIR, file_name)
        cv2.imwrite(out_path, frame)
        saved_motion_count += 1

print(f"Success! Processed all frames. Saved {saved_motion_count} motion frames to '{MOTION_OUT_DIR}'.")