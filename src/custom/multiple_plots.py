import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import random

fig=plt.figure(figsize=(8,8))

ax1=plt.subplot2grid((4,4),(0,0),colspan=3)
ax1.plot(X,[x+(x*random.random()) for x in X])
ax1.set_title('Plot 1 : (0,0)')

ax2=plt.subplot2grid((4,4),(0,3))
ax2.plot(X,[x-(x*random.random()) for x in X])
ax2.set_title('Plot 2 : (0,3)')

ax3=plt.subplot2grid((4,4),(1,0),rowspan=3,colspan=3)
ax3.plot(X,[x-(x*random.random()) for x in X])
ax3.set_title('Plot 3 : (1,0)')

ax4=plt.subplot2grid((4,4),(1,3),rowspan=3,colspan=1)
ax4.plot(X,[x+(x*random.random()) for x in X])
ax4.set_title('Plot 4 : (1,3)')

fig.tight_layout()

plt.show()