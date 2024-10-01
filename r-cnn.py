import cv2
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras.applications import VGG16

# Load a pre-trained VGG16 model (used in R-CNN for feature extraction)
model = VGG16(weights="imagenet", include_top=False)

# Load image
image = cv2.imread('i3.jpg')
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
plt.imshow(image_rgb)
plt.title("Original Image")
plt.axis('off')
plt.show()

# Generate region proposals using Selective Search
ss = cv2.ximgproc.segmentation.createSelectiveSearchSegmentation()
ss.setBaseImage(image)
ss.switchToSelectiveSearchFast()  # Use fast mode for faster processing
rects = ss.process()  # This gives us proposed regions (rectangles)

# Visualize some region proposals
image_copy = image_rgb.copy()
for (x, y, w, h) in rects[:50]:  # Let's visualize the first 50 proposals
    cv2.rectangle(image_copy, (x, y), (x + w, y + h), (0, 255, 0), 2)

plt.imshow(image_copy)
plt.title("Region Proposals using Selective Search")
plt.axis('off')
plt.show()

# You can now extract features for each region and apply a classifier
