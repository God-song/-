import numpy as np
from matplotlib import pyplot
from mpl_toolkits.mplot3d import Axes3D
import numpy
import matplotlib
import random
#matplotlib.rcParams["font.family"]="SimHei"
# x=numpy.linspace(0,2*numpy.pi)
# #print(x,type(x),x[0],x[1])
# y1=numpy.sin(x)
# y2=numpy.cos(x)
# pyplot.title("sin and cos")
# pyplot.xlabel("x")
# pyplot.ylabel("y")
# pyplot.plot(x,y1)
# pyplot.plot(x,y2)
#pyplot.show()

# name_list=["武汉","成都","广西","北京"]
#
# num_list=[10,20,30,20]
# num_list1=[15,25,33,15]
# width=0.5
# pyplot.bar((range(1,5)),num_list,color="Red",label="测试",tick_label=name_list)
# print(num_list)
# map(lambda x:x/2,num_list)
# print(num_list)
#pyplot.plot(name_list,list(map(lambda x:x/2,num_list)))
# for a,b in zip(name_list,num_list):
#     pyplot.text(a,b,"{}".format(b))
# pyplot.bar((range(1,5)),num_list1,width=width,color="blue",label="测试",tick_label=name_list)

# pyplot.legend()
# pyplot.show()
#饼状图
# label=["a","b","c","d"]
# num=[12,33,44,11]
# pyplot.axis()
# pyplot.pie(x=num,autopct="%.2f%%",explode=None,labels=label,colors=["red","green","blue","yellow"],shadow=True)
# pyplot.show()

"""重点"""
#实时画图
ax=[]
ay=[]
pyplot.ion()
#pyplot.show()
for i in range(10):
    ax.append(i)
    ay.append(i**2)
    pyplot.clf()
    pyplot.plot(ax,ay)
    pyplot.pause(0.1)
    pyplot.ioff()
pyplot.show()
#三维散点
# x=numpy.random.normal(0,1,100)
# y=numpy.random.normal(0,1,100)
# z=numpy.random.normal(0,1,100)
# print(x,y,z,type(x))
# fig=pyplot.figure()
# ax=Axes3D(fig)
# ax.scatter(x,y,z)
# pyplot.show()
#二维散点图
# n=50
# x=numpy.random.randn(n)
# y=np.random.randn(n)
# pyplot.scatter(x,y)
# pyplot.show()