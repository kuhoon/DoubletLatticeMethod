import numpy as np
from math import pi

# x = np.linspace(0, pi/2, 13)
# y= np.sin(x)
# print(y)
#
# x1 = np.linspace(-pi/2, pi/2, 33) #좁 넓 좁
# y1 = np.sin(x1)
# print((y1+1)/2)

# y = np.arange(0,1.25,0.25)
# print(y)

for i in range(len(idSectList) - 1):  # leg, list = 길이, 원소의 갯수
    bSpan = round(5*i) # round 반올림
    bSpanList.append(bSpan)