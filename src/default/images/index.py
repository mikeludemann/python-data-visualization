import numpy as np
import matplotlib.cm as cm
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook
from matplotlib.path import Path
from matplotlib.patches import PathPatch

delta = 0.025
x = y = np.arange(-3.0, 3.0, delta)
X, Y = np.meshgrid(x, y)
Z1 = np.exp(-X**2 - Y**2)
Z2 = np.exp(-(X - 1)**2 - (Y - 1)**2)
Z = (Z1 - Z2) * 2

fig, ax = plt.subplots()
im = ax.imshow(Z, interpolation='bilinear', cmap=cm.RdYlGn,
	origin='lower', extent=[-3, 3, -3, 3],
	vmax=abs(Z).max(), vmin=-abs(Z).max())

plt.show()


delta2 = 0.025
x2 = y2 = np.arange(-3.0, 3.0, delta2)
X2, Y2 = np.meshgrid(x2, y2)
Z12 = np.exp(-X2**2 - Y2**2)
Z22 = np.exp(-(X2 - 1)**2 - (Y2 - 1)**2)
Z2 = (Z12 - Z22) * 2

path = Path([[0, 1], [1, 0], [0, -1], [-1, 0], [0, 1]])
patch = PathPatch(path, facecolor='none')

fig2, ax2 = plt.subplots()
ax2.add_patch(patch)

im2 = ax2.imshow(Z, interpolation='bilinear', cmap=cm.gray,
	origin='lower', extent=[-3, 3, -3, 3],
	clip_path=patch, clip_on=True)
im2.set_clip_path(patch)

plt.show()
