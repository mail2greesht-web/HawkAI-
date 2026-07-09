import cv2
import os

# Define relative file paths
VIDEO_PATH = "videos/sample_video.mp4"
OUTPUT_DIR = "data/raw_frames"
FRAME_SAVING_INTERVAL = 5  # Save every 5th frame

# Create output folder if it doesn't exist
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Load the video
cap = cv2.VideoCapture(VIDEO_PATH)

if not cap.isOpened():
    print(f"Error: Could not open video file at '{VIDEO_PATH}'.")
    print("Please verify that 'videos' is a folder containing the 'sample_video.mp4' file.")
    exit()

print("Starting frame extraction...")

frame_count = 0
saved_count = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break  # End of video reached

    # Save frame at specified interval
    if frame_count % FRAME_SAVING_INTERVAL == 0:
        output_filename = os.path.join(OUTPUT_DIR, f"frame_{saved_count:04d}.jpg")
        cv2.imwrite(output_filename, frame)
        saved_count += 1

    frame_count += 1

# Release resources
cap.release()
print(f"Success! Extracted {saved_count} frames to '{OUTPUT_DIR}'.")