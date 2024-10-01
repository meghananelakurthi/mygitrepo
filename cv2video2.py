# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 11:44:28 2024

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
    ret, frame = cap.read()

    if not ret:
        break

    # Apply filters
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    edge_frame = cv2.Canny(gray_frame, 100, 200)  # Canny edge detection

    # Display the original and filtered frames
    cv2.imshow('Original Video', frame)
    cv2.imshow('Edge Detection', edge_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break