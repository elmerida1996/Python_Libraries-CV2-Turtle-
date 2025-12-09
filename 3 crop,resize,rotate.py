import cv2
img = cv2.imread("C:/Users/aa/Desktop/my catt.JPG")

cropped = img[50:200 , 100:300]   # (y1:y2 , x1,x2)
resized = cv2.resize(img , (200 , 200))
rotated = cv2.rotate(img , cv2.ROTATE_90_CLOCKWISE)
cv2.imshow("3. cropped", cropped)
cv2.imshow("3. resized" , resized)
cv2.imshow("3. rotated" , rotated)
cv2.waitKey(10000)