from math import sin

import matplotlib

matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt

scale = 50  # 1m -> 50 cells
size_x = 6 * scale
size_y = 4 * scale

# Let's plot anything to see if it's working
pressure = [[sin(x + y) for x in range(size_x)] for y in range(size_y)]
min_presure = -1
max_pressure = 1

fig = plt.figure()
ca_plot = plt.imshow(pressure, interpolation='bilinear', vmin=min_presure, vmax=max_pressure)
plt.colorbar(ca_plot)
plt.show()
