
import cv2
import numpy as np

image = cv2.imread("download.jpeg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Noise reduction
blur = cv2.GaussianBlur(gray, (5,5), 0)

# Edge detection
edges = cv2.Canny(blur, 30, 100)

# Morphology to connect edges
kernel = np.ones((3,3), np.uint8)
dilated = cv2.dilate(edges, kernel, iterations=1)

# Find contours
contours, _ = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

for cnt in contours:
    area = cv2.contourArea(cnt)
    if area > 10:   # Adjust based on resolution
        x, y, w, h = cv2.boundingRect(cnt)
        cv2.rectangle(image, (x,y), (x+w,y+h), (0,255,0), 2)

cv2.imshow("Detected", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

