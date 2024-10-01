# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 22:54:42 2024

@author: admin
"""

import tensorflow_hub as hub
import tensorflow as tf
import cv2
import matplotlib.pyplot as plt

# Load SSD model from TensorFlow Hub
model = hub.load("https://tfhub.dev/tensorflow/ssd_mobilenet_v2/2")

# Load the image
image = cv2.imread('i3.jpg')
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
input_tensor = tf.convert_to_tensor(image_rgb)
input_tensor = input_tensor[tf.newaxis, ...]

# Perform object detection
detections = model(input_tensor)

# Extract bounding boxes and scores
boxes = detections['detection_boxes'][0].numpy()
scores = detections['detection_scores'][0].numpy()
classes = detections['detection_classes'][0].numpy()

# Filter and visualize detections
image_with_boxes = image_rgb.copy()
height, width, _ = image_rgb.shape

for i, score in enumerate(scores):
    if score > 0.5:  # Only consider objects with score > 0.5
        box = boxes[i]
        y1, x1, y2, x2 = box
        (x1, y1, x2, y2) = (int(x1 * width), int(y1 * height), int(x2 * width), int(y2 * height))
        cv2.rectangle(image_with_boxes, (x1, y1), (x2, y2), (255, 0, 0), 2)

# Visualize the detected objects
plt.imshow(image_with_boxes)
plt.title("SSD Detected Objects")
plt.axis('off')
plt.show()
