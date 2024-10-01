import cv2
import matplotlib.pyplot as plt

# Read an image from file
image = cv2.imread('i3.jpg')  

# Convert BGR to RGB for Matplotlib
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Display the image using Matplotlib
plt.imshow(image_rgb)
plt.axis('off')  # Turn off axis numbers and ticks
plt.show()

#Opencv
# cv2.imshow('Image', image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
help(cv2.COLOR_BAYER_BG2GRAY)

# Display the grayscale image using Matplotlib
plt.imshow(gray_image, cmap='gray')
plt.axis('off')
plt.show()

# cv2.imshow('Grayscale Image', gray_image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# Draw a rectangle on the original image
cv2.rectangle(image, (50, 50), (200, 200), (0, 255, 0), 2)  # Green rectangle

# Draw a circle on the original image
cv2.circle(image, (300, 300), 50, (255, 0, 0), -1)  # Filled blue circle

# Display the image with shapes using Matplotlib
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
plt.imshow(image_rgb)
#plt.axis('off')
plt.show()

# cv2.imshow('Image with Shapes', image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# Resize the image to half its original size
resized_image = cv2.resize(image, (image.shape[1]//2, image.shape[0]//2))

# Display the resized image using Matplotlib
image_rgb = cv2.cvtColor(resized_image, cv2.COLOR_BGR2RGB)
plt.imshow(image_rgb)
#plt.axis('off')
plt.show()

# cv2.imshow('Resized Image', resized_image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# Apply Gaussian blur to the image
blurred_image = cv2.GaussianBlur(image, (15, 15), 0)

# Display the blurred image using Matplotlib
image_rgb = cv2.cvtColor(blurred_image, cv2.COLOR_BGR2RGB)
plt.imshow(image_rgb)
plt.axis('off')
plt.show()

# cv2.imshow('Blurred Image', blurred_image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# Perform edge detection using Canny
edges = cv2.Canny(gray_image, 100, 200)

# Display the edges using Matplotlib
plt.imshow(edges, cmap='gray')
#plt.axis('off')
plt.show()

# cv2.imshow('Edges', edges)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# Apply binary thresholding to the grayscale image
_, thresh_image = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY)

# Display the thresholded image using Matplotlib
plt.imshow(thresh_image, cmap='gray')
plt.axis('off')
plt.show()

cv2.imshow('Thresholded Image', thresh_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Flip the image horizontally
flipped_image = cv2.flip(image, 1)

# Display the flipped image using Matplotlib
image_rgb = cv2.cvtColor(flipped_image, cv2.COLOR_BGR2RGB)
plt.imshow(image_rgb)
#plt.axis('off')
plt.show()

# cv2.imshow('Flipped Image', flipped_image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# Find contours in the binary image
contours, _ = cv2.findContours(thresh_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Draw contours on a blank image
contour_image = image.copy()
cv2.drawContours(contour_image, contours, -1, (255, 0, 0), 2)  # Blue contours

# Display the image with contours using Matplotlib
image_rgb = cv2.cvtColor(contour_image, cv2.COLOR_BGR2RGB)
plt.imshow(image_rgb)
#plt.axis('off')
plt.show()

# cv2.imshow('Contours', contour_image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# Cropping an image

cropped_image = image[80:280, 150:330] # Slicing to crop the image
 
# Display the cropped image
cv2.imshow("cropped", cropped_image)
cv2.waitKey(0)
cv2.destroyAllWindows() 

# Face detection using Haar cascade
# Load Haar Cascade for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Convert to grayscale for detection
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect faces
faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5)

# Draw rectangles around detected faces
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)

# Display the image with detected faces
cv2.imshow('Faces Detected', image)
cv2.waitKey(0)
cv2.destroyAllWindows()





