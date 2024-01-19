import cv2
import numpy as np

image = cv2.imread("./houghimage.jpg")

lower_green = np.array([100, 100, 200])  # Define lower bound of ball color
upper_green = np.array([255, 150, 150])  # Define upper bound of ball color

hsv_frame = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

mask = cv2.inRange(hsv_frame, lower_green, upper_green)
detected_output = cv2.bitwise_and(hsv_frame, hsv_frame, mask = mask)

gray = cv2.cvtColor(hsv_frame, cv2.COLOR_BGR2GRAY)
circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, dp=1, minDist=100, param1=50, param2=30, minRadius=3, maxRadius=10)

if circles is not None:
    circles = np.uint16(np.around(circles))
    for i in circles[0, :]:
        print(i)
        cv2.circle(image, (i[0], i[1]), 10, (0, 255, 0), 2)

cv2.imwrite("houghimage_hsv.jpg", hsv_frame)
cv2.imwrite("houghimage_hsv_detection.jpg", image)
