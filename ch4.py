#coding=utf-8
#�Ĥ@�ӽd��

x = [1,2,3]
y = [4,5,6]
print x+y

import numpy as np
a = np.array([1, 2, 3])
b = np.array([2, 4, 6])
print a+b

#�ĤG�ӽd��

import numpy as np

a=np.array([1,3,2])
b=np.array([-2,1,-1])

la=np.sqrt(a.dot(a))
lb=np.sqrt(b.dot(b))
print("----�p��V�q����----")
print (la,lb)

cos_angle=a.dot(b)/(la*lb)

print("----�p��cos ----")
print (cos_angle)

angle=np.arccos(cos_angle)

print("----�p�⧨��(��쬰�k)----")
print (angle)

angle2=angle*360/2/np.pi
print("----�ഫ��쬰����----")
print (angle2)


#�ĤT�ӽd��

import numpy as np
a=np.array([[3, 4], [2, 3]])
b=np.array([[1, 2], [3, 4]])
c=np.mat([[3, 4], [2, 3]])
d=np.mat([[1, 2], [3, 4]])
e=np.dot(a,b)
f=np.dot(c,d)
print("----���k�B��----")
print (a*b)
print (c*d)
print("----�x�}�ۭ�----")
print (e)
print (f)

#�ĥ|�ӽd��

import numpy as np

a=np.random.randint(1, 10, (3, 5)) 

print (a)

#�Ĥ��ӽd��

from numpy import *

a = mat([[1,2,-1],[3,0,1],[4,2,1]])
  
print linalg.det(a)

#�Ĥ��ӽd��

import numpy as np
from matplotlib import pyplot

x = np.arange(0,10,0.1)
y = np.sin(x)
pyplot.plot(x,y)
pyplot.show()






