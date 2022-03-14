from PIL import Image,ImageDraw,ImageFilter,ImageFont
import random


w=240
h=120
def get_char():
    return chr(random.randint(65,90))

def bg_color():
    return (random.randint(65,255),
            random.randint(65,255),
            random.randint(65,255))
def f_color():
    return (random.randint(10, 100),
            random.randint(10, 100),
            random.randint(10, 100))
def get_newimg():
    return Image.new("RGB",(w,h),(255,255,255))
def mod_img(img1,flag=0):
    if flag==0:
        img_array=img1.load()
        for i in range(w):
            for j in range(h):
                img_array[i,j]=bg_color()
    else:
        for i in range(w):
            for j in range(h):
                img1.point((i,j),bg_color())
    
if __name__=="__main__":
    img1=get_newimg()
    #img1.show()
    draw1=ImageDraw.Draw(img1)
    font=ImageFont.truetype(r"simsun.ttc",40)
    mod_img(draw1,2)
    for i in range(1,5):
        draw1.text((45*i,45),text=get_char(),fill=f_color(),font=font)

    img1.show()



