
import cv2
img = cv2.imread("C:/Users/aa/Desktop/cat_hangover_relax_213869.JPG") # عکس رو از مسیر میخونه 
cv2.imshow("Cat", img) # یه پنجره باز میکنه و تصویر رو نشون میده
# برای ارور لود نشدن عکس ها 
# if img is not None:
#     print ("shape: " , img.shape)
# else:
#     print("Error")

cv2.waitKey(0) #صبر میکنه تا یه کلید فشار بدی
cv2.destroyAllWindows() # همه پنجره ها رو میبنده
