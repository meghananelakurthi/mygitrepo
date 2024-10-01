# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 23:56:04 2024

@author: admin
"""

import numpy as np
import cv2
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras.applications import VGG16
from tensorflow.keras.models import Model

# Load VGG16 for feature extraction
base_model = VGG16(weights='imagenet', include_top=False)
feature_extractor = Model(inputs=base_model.input, outputs=base_model.output)

def extract_features(image):
    image_resized = cv2.resize(image, (224, 224))
    image_array = np.expand_dims(image_resized, axis=0)
    features = feature_extractor.predict(image_array)
    return features.flatten()

def selective_search(image):
    ss = cv2.ximgproc.segmentation.createSelectiveSearchSegmentation()
    ss.setBaseImage(image)
    ss.switchToSelectiveSearchFast()
    rects = ss.process()
    return rects

# Sample image from PASCAL VOC or any other dataset
image_path = 'i3.jpg'  # Replace with your image path
image = cv2.imread(image_path)

image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
regions = selective_search(image_rgb)

features = []
for rect in regions[:100]:  # Use top 100 regions
    x, y, w, h = rect
    roi = image_rgb[y:y+h, x:x+w]
    feature = extract_features(roi)
    features.append(feature)

# For this example, we will not train a classifier, just visualize
for i, rect in enumerate(regions[:100]):
    x, y, w, h = rect
    cv2.rectangle(image_rgb, (x, y), (x + w, y + h), (0, 255, 0), 2)

plt.imshow(image_rgb)
plt.axis('off')
plt.show()
