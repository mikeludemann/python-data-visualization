import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import random

fig=plt.figure(figsize=(8,6))

plt.plot(X,np.exp(X))

plt.title('Annotating Exponential Plot using plt.annotate()')
plt.xlabel('x-axis')
plt.ylabel('y-axis')

#changing axes limits
plt.ylim(1,8000)
plt.xlim(0,9)

# removing axes from the figure
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['top'].set_visible(False)

#changing color of the axes
plt.gca().spines['left'].set_color('red')
plt.gca().spines['bottom'].set_color('green')

plt.annotate('Point 1',xy=(6,400),arrowprops=dict(arrowstyle='->'),xytext=(4,600))

plt.annotate('Point 2',xy=(7,1150),arrowprops=dict(arrowstyle='->',connectionstyle='arc3,rad=-.2'),xytext=(4.5,2000))

plt.annotate('Point 3',xy=(8,3000),arrowprops=dict(arrowstyle='-|>',connectionstyle='angle,angleA=90,angleB=0'),xytext=(8.3,2200))

plt.show()