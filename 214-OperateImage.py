import cv2

img=cv2.imread("galaxy.jpg",0)       # 当为0 和 1 时，得到的图片大小，维度，数组会变化。
                                     # 为0时，是灰色；当是1时，会是彩色，且由三层组成。

print(type(img))    # 检查图片类型，可以得到是numpy类型
print(img)          # 可以得到图片的数组
print(img.shape)    # 检查图片大小，有多少像素点
print(img.ndim)     # 检查图片维度

resized_image=cv2.resize(img,(int(img.shape[1]/2),int(img.shape[0]/2)))   #等比例resize picture。
cv2.imshow("Galaxy",resized_image)            # cv2.imshow("Galaxy",img)        # show the image
cv2.imwrite("Galaxy_resized.jpg",resized_image)
cv2.waitKey(0)                                # 括号里如果是2000代表两秒，图片展示两秒然后关闭。如果是0，则会持续展示，知道摁了任意键，会关闭图片。
cv2.destroyALLWindows()                       # close all the windows