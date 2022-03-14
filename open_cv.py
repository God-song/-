#和PIL类似
import cv2
from PIL import Image,ImageDraw
#注意文件路径不要有中文
img1=cv2.imread(r"./Image/1.jpg")
#cv2.imshow("image",img1)
#等待任意键盘
#cv2.waitKey()
#等待所以的win窗口关掉
#cv2.destroyWindow()
# blue=(0,0,255)
# cv2.line(img1,(10,10),(100,100),blue,thickness=3)
# cv2.imshow("image",img1)
# cv2.waitKey()

#画一个矩形
img2=Image.open("./Image/1.jpg")
draw1=ImageDraw.Draw(img2)
draw1.rectangle((200,200,600,600),outline=(120,20,20))

draw1.line((300,300,500,500),"red")
#img2.show()
cv2.rectangle(img1,(20,20),(100,100),(155,155,155))
cv2.imshow("image",img1)
cv2.waitKey()
