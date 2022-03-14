import numpy as np
# a=np.arange(12).reshape(4,3)
#b==a
#b=a[:]
#二维的1，3
# b=a[:1]
# print(b,b.shape)
#二维的1，1
# b=a[:1,:1]
# print(b,b.shape)
# a[0,1]=100
# print(a[0,1])
# print(a)
#切片不会把轴变少
#a[0][0]会改变维度
# c=a[:1][0:1]
# print(c)

#三维的
# a=np.arange(24).reshape(2,3,4)
# print(a)
# b=a[:1,:,2:]
# print(b)
#kaobe
# a=np.arange(12).reshape(4,3)
# print(a)
# b=a.copy()
# print(b)
# a[0,1]=100
# print(a)
# print(b)
# print(a==b)

#拼接
# a=np.arange(12).reshape(3,4)
# b=np.array([4,5,6,7])
# print(a)
# print(b)
# a=a.tolist()
# a.append(b)
# a=np.array(a)
# print(a)
# a=a.tolist()
# print(a)
# a.extend([b.tolist()])
# print(a)

#在0轴添加
a=np.arange(12).reshape(3,4)
b=np.arange(12).reshape(3,4)
c=np.vstack((a,b))
print(c,c.shape)
#在一轴添加
d=np.hstack((a,b))
print(d,d.shape)