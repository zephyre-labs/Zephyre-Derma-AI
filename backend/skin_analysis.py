import os
import numpy as np
from PIL import Image
from tensorflow.keras.models import load_model
import warnings

# ✅ Suppress TensorFlow and Keras info logs
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'  # Only show real errors
warnings.filterwarnings("ignore", category=UserWarning, module="keras")

# ✅ MongoDB utility functions
from mongo_handler import (
    upload_images_from_folder,
    retrieve_images_by_label,
    upload_prediction_result,
)

# ✅ Load the trained CNN model
model = load_model("skin_type_model.keras", compile=False)

# ✅ Attempt dataset upload to MongoDB (if folder exists)
base_folder = os.path.join(os.path.dirname(__file__), "dataset")
if os.path.exists(base_folder):
    print("📤 Uploading dataset images to MongoDB Atlas...")
    for label in os.listdir(base_folder):
        label_folder_path = os.path.join(base_folder, label)
        if os.path.isdir(label_folder_path):
            upload_images_from_folder(label_folder_path, label)
else:
    print("ℹ️ 'dataset' folder not found. Skipping MongoDB upload.")

# ✅ Image preprocessing for prediction
def preprocess_image(image_path):
    try:
        image = Image.open(image_path).resize((224, 224))
        image = np.array(image) / 255.0
        return np.expand_dims(image, axis=0)
    except Exception as e:
        print(f"❌ Error processing image: {e}")
        return None

# ✅ Predict skin type from image
def predict_skin_type(image_path):
    image = preprocess_image(image_path)
    if image is None:
        print("❌ Failed to preprocess image.")
        return

    prediction = model.predict(image)
    predicted_index = int(np.argmax(prediction))
    confidence = float(np.max(prediction))

    labels = [
        'normal', 'oily', 'dry', 'combination', 'sensitive',
        'acne_prone', 'dehydrated', 'mature_skin', 'hyperpigmented_skin',
        'redness_rosacea', 'textured', 'dull_skin', 'eczema', 'allergy_prone',
        'sun_damaged', 'uneven_tone', 'pimple_prone', 'open_pores', 'healthy_skin'
    ]

    predicted_label = labels[predicted_index]

    print("\n🔍 Confidence scores for all classes:")
    confidence_dict = {}
    for i, score in enumerate(prediction[0]):
        print(f"{labels[i]}: {score:.2f}")
        confidence_dict[labels[i]] = float(score)

    if confidence > 0.5:
        print(f"\n✅ Predicted skin type: {predicted_label} (Confidence: {confidence:.2f})")
        upload_prediction_result(predicted_label, confidence, confidence_dict)
    else:
        print("\n⚠️ Low confidence in prediction. Try again with a clearer image.")

# ✅ Test with an image named 'test.jpg'
test_image_path = "test.jpg"
if os.path.exists(test_image_path):
    predict_skin_type(test_image_path)
else:
    print(f"❌ Test image '{test_image_path}' not found. Place it next to this script.")
