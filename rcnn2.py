import numpy as np
import cv2
import matplotlib.pyplot as plt
from tensorflow.keras.applications import VGG16
from tensorflow.keras.models import Model
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline

# Load a pre-trained VGG16 model for feature extraction
base_model = VGG16(weights='imagenet', include_top=False)
feature_extractor = Model(inputs=base_model.input, outputs=base_model.output)

def extract_features(image):
    # Resize and preprocess the image for VGG16
    image_resized = cv2.resize(image, (224, 224))
    image_array = np.expand_dims(image_resized, axis=0)
    features = feature_extractor.predict(image_array)
    return features.flatten()

# Selective Search for Region Proposals
def selective_search(image):
    ss = cv2.ximgproc.segmentation.createSelectiveSearchSegmentation()
    ss.setBaseImage(image)
    ss.switchToSelectiveSearchFast()
    rects = ss.process()
    return rects

# Sample image for demonstration
image_path = 'i3.jpg'  # Replace with your actual image path
image = cv2.imread(image_path)

if image is None:
    raise ValueError(f"Image not found or unable to read the image at {image_path}")

image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Get region proposals
regions = selective_search(image_rgb)

# Extract features for each region proposal
features = []
for rect in regions[:200]:  # Limit to top 200 proposals
    x, y, w, h = rect
    roi = image_rgb[y:y+h, x:x+w]
    feature = extract_features(roi)
    features.append(feature)

# Create dummy labels for SVM (you should have actual labels for training)
labels = np.random.randint(0, 2, len(features))  # Binary classification example

# Train SVM Classifier
svm_model = make_pipeline(StandardScaler(), SVC())
svm_model.fit(features, labels)

# Predict on new regions
predictions = []
for feature in features:
    pred = svm_model.predict([feature])
    predictions.append(pred[0])

# Map predictions to class labels
class_labels = {0: 'Class 0', 1: 'Class 1'}

# Visualize the results
for i, rect in enumerate(regions[:200]):
    x, y, w, h = rect
    color = (0, 255, 0) if predictions[i] == 1 else (255, 0, 0)
    label = class_labels[predictions[i]]
    cv2.rectangle(image_rgb, (x, y), (x + w, y + h), color, 2)
    cv2.putText(image_rgb, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

plt.imshow(image_rgb)
plt.axis('off')
plt.show()
