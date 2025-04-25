import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

# Disable stdout/stderr spam
import sys
import logging
tf_logger = logging.getLogger('tensorflow')
tf_logger.setLevel(logging.ERROR)
sys.stderr = open(os.devnull, 'w')

import warnings
import cv2
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array

# Suppress TensorFlow logging

# Suppress OpenCV warnings by redirecting stderr
warnings.filterwarnings("ignore", category=UserWarning, module='cv2')


# Load model without the optimizer (skip optimizer loading)
try:
    model_path = os.path.join(os.path.dirname(__file__), "skin_type_model.keras")
    model = load_model(model_path)   
    print("✅ Model loaded successfully.")
except Exception as e:
    print(f"❌ Error loading model: {e}")
    exit()

# Define labels based on your dataset folders (update to match the 19 types)
labels = [
    'normal', 'oily', 'dry', 'combination', 'sensitive', 'acne_prone', 
    'dehydrated', 'mature_skin', 'hyperpigmented_skin', 'redness_rosacea', 
    'textured', 'dull_skin', 'eczema', 'allergy_prone', 'sun_damaged', 
    'uneven_tone', 'pimple_prone', 'open_pores', 'healthy_skin'
]  # Ensure this matches the actual class names in your dataset

# Image dimensions (adjust to match model input size)
IMAGE_SIZE = (224, 224)

def capture_and_predict():
    # Start webcam
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("❌ Failed to access webcam. Ensure the camera is connected.")
        exit()

    print("📸 Webcam is open. Starting the feed...")

    print("📸 Starting camera... press 's' to predict ")
    print("Press 'q' to quit ")

    skin_type = "Unknown"
    while True:
        ret, frame = cap.read()
        if not ret:
            print("❌ Failed to grab frame.")
            break

        # Display the frame
        cv2.imshow("Live Feed - Press 's' to Predict", frame)

        key = cv2.waitKey(1)

        if key == ord('s'):
            # Resize + preprocess the image
            img = cv2.resize(frame, IMAGE_SIZE)
            img = img_to_array(img)
            img = img / 255.0  # Normalize
            img = np.expand_dims(img, axis=0)

            # Predict skin type
            try:
                prediction = model.predict(img)
                class_index = np.argmax(prediction)
                confidence = prediction[0][class_index]

                skin_type = labels[class_index] if class_index < len(labels) else "Unknown"
                print(f"🧠 Predicted Skin Type: {skin_type} ({confidence * 100:.2f}% confidence)")

                # Overlay result on screen
                result_text = f"{skin_type} ({confidence * 100:.1f}%)"
                cv2.putText(frame, result_text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                cv2.imshow("Prediction", frame)

            except Exception as e:
                print(f"❌ Error during prediction: {e}")

        elif key == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

    return skin_type

# Call the function to start the process
if __name__ == "__main__":
    capture_and_predict()