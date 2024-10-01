# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 22:56:32 2024

@author: admin
"""

# First, install the required library
#!pip install -U torch torchvision yolov5

import torch
import cv2
import matplotlib.pyplot as plt

# Load a pre-trained YOLOv5 model (use 'yolov5s', 'yolov5m', 'yolov5l', 'yolov5x' for different sizes)
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')

# Load an image
image_path = 'i3.jpg'
image = cv2.imread(image_path)

# Perform object detection
results = model(image)

# Print detected labels and bounding boxes
results.print()

# Visualize detected objects
results.show()

# You can also plot the bounding boxes on the image
plt.imshow(results.imgs[0])
plt.title("YOLOv5 Detected Objects")
plt.axis('off')
plt.show()
