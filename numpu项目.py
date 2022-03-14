import os
import numpy as np
from PIL import Image
path_img=r"D:/照片/"
class Sample:
    def read_data(self):
        img_list=os.listdir(path_img)
        #print(img_list)
        self.img_array = []
        for i in img_list:
            #print(i)

            img1=Image.open(path_img+i)
            #将照片转变成数组,三维
            image=np.array(img1)
            self.img_array.append(image)
            #print(image)
        return self.img_array


    def get_batch(self,set):
        #得到的是四维的数组n h w c
        img_ar=self.read_data()
        #生成随机书
        self.get_image=[]
        for i in range(set):
            index=np.random.randint(1,len(self.img_array))
            #print(index)
            one_image=self.img_array[index]
            self.get_image.append(one_image)
        return self.get_image


sample=Sample()
img_array=sample.read_data()
#print(img_array)
get_image=sample.get_batch(5)
print(get_image)
print(np.shape(get_image))
#print(np.shape(get_image))