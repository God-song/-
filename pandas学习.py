"""pandas
面向数据分析，世居于numpy构建的
为时间序列分析提供了一个很好的支持
pandas有两个数据结构一个是
series ，另一个是DataFrame """
import pandas
import numpy
from pandas import Series
from pandas import DataFrame
a=Series([1,2,3],dtype=numpy.float32)
print(a,a[0])
# a=range(1,7)
# b=Series(a)
# print(a,b)
# print(a.values)
#print(a.index)
# b=Series([3,4,5,6],index=["a","b","C","d"])
# print(b)
# print(b.values)
c=DataFrame(data=[[1,2,3],[4,5,6],[7,8,9]],index=list(range(3)),columns=["a","b","c"])
c.iloc(0)