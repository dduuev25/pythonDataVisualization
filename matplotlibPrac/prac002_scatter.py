#
import cmath
import time

from matplotlib import pyplot as pp

x_values = list(range(0,21))

y_values = [i**1.3 for i in range(0,21)]

pp.axis([0,50,0,50])
pp.scatter(x_values,y_values,s=1,c='red')  #s设置点的大小
pp.xlabel(x_values)
pp.ylabel(y_values)
pp.savefig("D:\\datavisual\\001.png",bbox_inches="tight")
#pp.show()