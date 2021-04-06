import cv2

face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

img=cv2.imread("news.jpg")
gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)    # Turn the color to gray.

faces=face_cascade.detectMultiScale(gray_img, 
scaleFactor=1.05,       # 增加程序在单位面积内搜索面积1.5倍，搜索变粗糙，图片变模糊，倍数越大，越不清晰。
minNeighbors=5)         # 搜索相邻的五个单位。5，数字可以变化，此处5 ，是可行的。

for x, y, w, h in faces:
    img=cv2.rectangle(img, (x,y),(x+w,y+h),(0,255,0),3)    # 3 is the width of rectangle line.
                                                           # (0,255,0) is the color of the rectangle line.
print(type(faces))
print(faces)

resized=cv2.resize(img,(int(img.shape[1]/3),int(img.shape[0]/3)))

cv2.imshow("Gray",resized)            # Gray is the name of the new file.
cv2.waitKey(0)                         # the new image will not close automatically.
cv2.destroyAllWindows()
