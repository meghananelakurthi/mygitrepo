# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 11:38:04 2024

@author: admin
"""

import cv2

# Open webcam
cap = cv2.VideoCapture(0)

# Check if the webcam is opened correctly
if not cap.isOpened():
    print("Error: Could not open video stream from webcam.")
    exit()

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    if not ret:
        print("Error: Failed to capture video frame.")
        break

    # Apply a filter: Convert the frame to grayscale
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the original and filtered frames
    cv2.imshow('Original Video', frame)
    cv2.imshow('Grayscale Video', gray_frame)

    # Press 'q' to quit the video stream
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture and close the windows
cap.release()
cv2.destroyAllWindows()