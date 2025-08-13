# computer_vision_Color_detection_using_open_cv

- This project uses OpenCV to detect multiple colors (e.g., Red, Green, Blue) in real-time using a webcam feed. It processes video frames, creates color masks based on HSV ranges, and tracks objects using contours.

# 📹 Steps Followed
✅ Step 1: Capture the Video using Webcam
Use cv2.VideoCapture(0) to start capturing video from the webcam.

✅ Step 2: Get the Image Frame from the Video Stream
Read each frame using ret, frame = cap.read().

✅ Step 3: Convert the Image Frame into HSV Color Space
Convert BGR to HSV using cv2.cvtColor() for better color filtering.

✅ Step 4: Define the HSV Range and Create a Mask for Each Color
Set HSV lower and upper bounds for each color (e.g., red, green, blue).
Use cv2.inRange() to create binary masks.

✅ Step 5: Apply Bitwise AND Operator Between Frame and Mask
Use cv2.bitwise_and() to extract parts of the image where the color is detected.

✅ Step 6: Create Contours to Track Each Color
Use cv2.findContours() to detect object boundaries.
Draw bounding boxes or circles using cv2.drawContours() or cv2.rectangle().

✅ Step 7: Display Detected Colors with Labels
Show real-time tracking with color names displayed on the detected objects.

#  Requirements
- Python 3.x
- OpenCV (pip install opencv-python)

# Sample Output
- A webcam window will open showing the video feed with detected red, green, and blue objects outlined and labeled in real time.

# To DO (Optional Enhancements)
- Add more colors
- Use trackbars to dynamically adjust HSV ranges
Save the video output with color tracking
