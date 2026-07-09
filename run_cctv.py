from ultralytics import YOLO
import cv2
import winsound

# 1. Model Load karein
model = YOLO('runs/detect/train/weights/best.pt')

# 2. Label ka naam change karein
# Aap 'Theft Detected' ki jagah kuch bhi likh sakte hain
model.names[0] = 'Theft Detected'

# Video path
cap = cv2.VideoCapture("videos/sample_video.mp4")

print("System Started... Press 'q' to exit.")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Prediction
    results = model.predict(frame, conf=0.5, verbose=False)

    # Drawing logic: Red Box aur Label ke liye
    for result in results:
        boxes = result.boxes
        for box in boxes:
            # Box
            x1, y1, x2, y2 = map(int, box.xyxy[0])

# Red Rectangle (BGR format: 0, 0, 255)
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 3)

            # Label Text
            label = model.names[0]
            cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)

    # Detection logic: Alert Sound (Siren)
    if len(results[0].boxes) > 0:
        # Beep(Frequency, Duration in ms) -> 1000Hz, 500ms
        winsound.Beep(1000, 500)
        print("ALERT: Activity Detected!")

    # Display
    cv2.imshow('AI CCTV Surveillance', frame)

    # 'q' dabane par band hoga
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()