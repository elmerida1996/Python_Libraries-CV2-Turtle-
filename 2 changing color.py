import cv2

img = cv2.imread("C:/Users/aa/Desktop/my catt.JPG")

gray = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)
hsv = cv2.cvtColor(img , cv2.COLOR_BGR2HSV)

cv2.imshow("Gray" , gray)
cv2.imshow("HSV" , hsv)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite("C:/Users/aa/Desktop/my new cat.JPG" , gray , [cv2.IMWRITE_JPEG_QUALITY, 100])
print("Image saved successfuly !")
