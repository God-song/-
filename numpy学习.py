"""numpy详细学习
开源数值扩展，存储和处理大型
矩阵，比pytho）n自带的嵌套列表要高效很多
矩阵（mmatrix

numpy 提供了python对多维数组对象的支持
ndarray,具有矢量运算，此外也针对数组运算
提供大量的数学函数库"""
import numpy as np
from PIL import  Image
from PIL import  ImageDraw
from  PIL import  ImageFont
#创建
#a=np.array([[1,2],[3,4],[5,6])
#b=a.tolist(),将np转成list
# a=np.ndarray(12).reshape(2,2,3)
# print(a)
#b=np.arange(12.0,dtype=np.float32).reshape(2,2,3)

#print(b)
# print(b,type(b))
# print(b[0][1][1])
# #查看形状
# print(np.shape(b))
# print(b.shape)
# print(b.ndim)
# print(b.size)
# print(b.dtype)
#生成0数组。1数组，空数组
# a=np.zeros(shape=[2,2,3],dtype=np.float32)
# b=np.ones(shape=[2,2,3],dtype=np.float32)
# c=np.empty()
# print(a,a.dtype,b,sep="\n")

#案例a.one-hot 独热 8-5-2-6
# a=np.zeros(shape=[4,10])
# #print(a)
# def one_hot(a,flag=0):
#     if flag==0:
#         for i,k in enumerate(a):
#             if i==0:
#                 k[8]=1
#             elif i==1:
#                 k[5]=1
#             elif i==2:
#                 k[2]=1
#             elif i==3:
#                 k[6]=1
#     # else:
#     #     a[:  ]
#
# one_hot(a)
# print(a)
# print(np.argmax(a,axis=0))
# print(np.ma   x(a,axis=0))
# np.argmax(a,axis=1)
# print(np.argmax(a,axis=1))
# print(np.max(a,axis=1))
# b=np.arange(12).reshape(2,2,3)
# print(np.argmax(b,axis=2))
# print(b)
# print(np.max(b,axis=2))
# a=np.arange(24).reshape(3,2,2,2)
# print(a)
# print(np.argmax(a,axis=0),
#       np.max(a,axis=0),sep="\n")
# print(np.argmax(a,axis=1),
#       np.max(a,axis=1),sep="\n")
# print(np.argmax(a,axis=3),
#       np.max(a,axis=3),sep="\n")
# a=np.linspace(0,2,10)
# print(a,type(a))

#numpy的运算,矩阵+数字，矩阵每个数字都+num
# a=np.arange(16).reshape(4,4)
# print(a)
# b=[1]
# c=a+b
# print(c)
# a=np.sqrt(9)
# print(a)
# a=np.arange(24).reshape(2,3,4)
# print(a)
# print()
# print(a.shape)
# print(a.T)
# print()
# print(a.shape)
# b=np.transpose(a,[1,0,2])
# print(b)
# print(b.shape)
# path="./Image/1.jpg"
# img1=Image.open(path)
# img_array=img1.load()
# print(type(img_array))
# imgsize=img1.size
# for i in range(imgsize[0]):
#     for j in range(imgsize[1]):
#         print(img_array[i,j])
a=np.arange((24)).reshape(2,3,4)
print(a)
# b=np.max(a,axis=1)
# print(b)
c=np.sum(a,axis=0)
print(c)