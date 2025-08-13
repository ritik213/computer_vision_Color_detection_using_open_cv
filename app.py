import streamlit as st
import cv2
import numpy as np
from PIL import Image

st.title("Color Detection using Webcam")

# Start camera
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    st.error("Could not access the camera.")
else:
    # Capture a single frame
    ret, frame = cap.read()
    cap.release()

    if ret:
        # Convert frame to HSV
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # Red mask (using dual range for better detection)
        low_red1 = np.array([0, 120, 70])
        high_red1 = np.array([10, 255, 255])
        low_red2 = np.array([170, 120, 70])
        high_red2 = np.array([180, 255, 255])
        red_mask1 = cv2.inRange(hsv, low_red1, high_red1)
        red_mask2 = cv2.inRange(hsv, low_red2, high_red2)
        red_mask = red_mask1 | red_mask2
        red = cv2.bitwise_and(frame, frame, mask=red_mask)

        # Blue mask
        low_blue = np.array([94, 80, 2])
        high_blue = np.array([126, 255, 255])
        blue_mask = cv2.inRange(hsv, low_blue, high_blue)
        blue = cv2.bitwise_and(frame, frame, mask=blue_mask)

        # Green mask
        low_green = np.array([40, 100, 100])
        high_green = np.array([102, 255, 255])
        green_mask = cv2.inRange(hsv, low_green, high_green)
        green = cv2.bitwise_and(frame, frame, mask=green_mask)

        # Every color except white
        low = np.array([0, 42, 0])
        high = np.array([179, 255, 255])
        mask = cv2.inRange(hsv, low, high)
        result = cv2.bitwise_and(frame, frame, mask=mask)

        # Convert images from BGR to RGB for Streamlit
        def convert(img): return Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

        # Display frames
        st.image(convert(frame), caption="Original Frame")
        st.image(convert(red), caption="Red Detected")
        st.image(convert(blue), caption="Blue Detected")
        st.image(convert(green), caption="Green Detected")
        st.image(convert(result), caption="Non-White Colors")
    else:
        st.error("Failed to capture frame from webcam.")
