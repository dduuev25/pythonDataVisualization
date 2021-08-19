#

import matplotlib.pyplot as pp
input_values = [x for x in range(10)]
squares = [x**2 for x in range(10)]
pp.plot(input_values,squares)
pp.title("square numbers", fontsize=24)
pp.axis([0,10,0,100])
pp.xlabel("value",fontsize=12)
pp.ylabel("square value",fontsize=12)

pp.tick_params(axis="both",labelsize=14)

pp.show()

