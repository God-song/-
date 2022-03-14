from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
img1=Image.open(r"./图片/1.jpg")
a=ImageDraw.Draw(img1)
a.line((0,0,100,100),"red")
del a
img1.show()