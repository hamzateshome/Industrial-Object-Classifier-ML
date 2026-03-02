import tensorflow as tf
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input, decode_predictions
import numpy as np

def classify_component(img_path):
    # 1. Load the pre-trained MobileNetV2 model
    # In a real mechatronics setup, this would be deployed on an edge device
    model = MobileNetV2(weights='imagenet')

    # 2. Load and preprocess the image
    img = image.load_img(img_path, target_size=(224, 224))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)

    # 3. Perform Inference
    preds = model.predict(x)
    
    # 4. Output the results
    print('Predicted:', decode_predictions(preds, top=3)[0])

if __name__ == "__main__":
    print("Industrial Object Classifier Initialized...")
    # classify_component('sample_bolt.jpg') # Example usage
