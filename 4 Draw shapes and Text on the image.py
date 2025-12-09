import cv2
import numpy as np #نشان دادن تصاویر به عنوان ارایه 

img = np.zeros((300, 500, 3), dtype=np.uint8)   #((rows , cols , channels) , نوع داده هر پیکسل = مقادیر ممکن 0  تا 255  برای هر کانال)
img[:] = (255 , 255 , 0)      #رنگ بوم

cv2. rectangle( img , (50 , 50) , (200 , 200) , (0, 0 , 0) , 3) # ( (y1 , x1) , (y2, x2) , (B , G , R) , ضخامت خط مستطیل )

#cv2.circle(img , (75, 75) , 40 , (255 , 0 , 0) , -1 ) # ((مختصات مرکز دایره) , شعاع دایره , (B , G , R) , ضخامت دایره)

cv2.line (img , (0 , 0) , (500 , 300) , (0 , 255 , 255) , 5)

cv2.putText(img, "openCV Demo" , (30 , 50) , cv2.FONT_HERSHEY_SCRIPT_SIMPLEX , 2 , (0 , 255 , 0) , 2 )
# ( name , "text" , (مختصات شروع متن ) , Font , Font size , color , ضخامت نوشته)

cv2.imshow("my numpy" , img)
cv2.waitKey(10000)

cv2.imwrite ("C:/Users/aa/Desktop/my new art.JPG" , img)

#=======================================================================================================
# slicing 
# import cv2
# import numpy as np

# img = 255 * np.ones( (400 , 600 , 3) , dtype=np.uint8)
# img [50:150 , 100:300] = (0 , 255 , 255)
# img [80 , 150] = (255 , 0 , 0)
# cv2.imshow("my numpy" , img)
# cv2.waitKey(100000)


#======================================================================
# import cv2
# import numpy as np

# h , w = 200 , 400
# grad = np.zeros((h , w , 3) , dtype=np.uint8)
# for x in range(w):    #  از x=0  تا  x=w-1  یعنی از چپ تا راست مقدار رنگ اون ستون رو تنظیم میکنه
#     color = int(255 * (x / (w - 1))) # فرمول (x / (w - 1)) عددی بین 0 و 1 میده که هر بار در 255 ضرب میشه عددی بین 0 تا 255 میشه
#     grad[ : , x] = (color , color , color) # تمام ستون X رو با یک رنگ خاکستری پر کن

# cv2.imshow("Gradiant" , grad)
# cv2.waitKey(0)
# cv2.destroyAllWindows()