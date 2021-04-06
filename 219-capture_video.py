import cv2, time

video=cv2.VideoCapture(0)      # only have one camera,so input 0 there.

a=0

while True:                    # 建立图像侦查的循环，持续导入图像，连成视频
    a=a+1
    check, frame = video.read()

    print(check)
    print(frame)

    gray=cv2.cvtColor(frame.cv2.COLOR_BGR2GRAY)
    #time.sleep(3)
    cv2.imshow("Capturing",frame)


    key=cv2.waitKey(1000)       #1000代表一秒，如果改成1，则连续图像，构成视频
 
    if key==ord('q')
        break

print(a)

video.release()
cv2.destroyAllWindows