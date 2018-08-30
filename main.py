import matplotlib
from matplotlib.animation import FuncAnimation

from simulation import Simulation, min_presure, max_pressure

matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt

simulation = Simulation()
figure = plt.figure()
ca_plot = plt.imshow(simulation.pressure, interpolation='bilinear', vmin=min_presure, vmax=max_pressure)
plt.colorbar(ca_plot)


def animation_func(i):
    simulation.step()
    ca_plot.set_data(simulation.pressure)
    return ca_plot


animation = FuncAnimation(figure, animation_func, interval=1)
plt.show()
