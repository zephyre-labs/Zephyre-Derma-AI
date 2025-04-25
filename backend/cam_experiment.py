import cv2

# Try to open the webcam
cap = cv2.VideoCapture(0)

if cap.isOpened():
    print("✅ Webcam is available!")
else:
    print("❌ Webcam is not accessible or in use by another program.")

cap.release()

