
import cv2
import datetime

cap = cv2.VideoCapture(0)
#=============================================================================
#تنظیم رزولوشن
cap.set(cv2.CAP_PROP_FRAME_HEIGHT , 640)
cap.set(cv2.CAP_PROP_FRAME_WIDTH , 480)

#===============================================================================
# #ذخیره ویدیو
# fourcc = cv2.VideoWriter_fourcc(*'XVID') 
# out = cv2.VideoWriter('C:/Users/aa/Desktop/output.avi' , fourcc  , 20.0  , (640, 480)) 
# #('address' , variable , frame rate یعنی در هر ثانیه چند فریم ذخیره بشن , frame size )

#================================================================================
while True:
    ret , frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break

    gray = cv2.cvtColor (frame , cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur (frame , (15 , 15) , 0)

    now = datetime.datetime.now().strftime("%H:%M:%S") #کار با کتابخانه dat&time
    cv2.putText(frame , f"Time: {now}" , (10 , 30) , cv2.FONT_HERSHEY_SIMPLEX , 1 , (255 , 255 , 255) , 2 , cv2.LINE_AA)
    combined = cv2.hconcat([frame , blur])
    #combined = cv2.vconcat([frame , blur])

    cv2.imshow("Live Camera" , combined)

    #out.write(frame)

    if cv2.waitKey(1) & 0xFF == ord('q'): #ASCII code q == 113
        break

cap.release()
#out.release()
cv2.destroyAllWindows()