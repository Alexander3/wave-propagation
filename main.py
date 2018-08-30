import matplotlib
from matplotlib.animation import FuncAnimation

from simulation import Simulation, min_presure, max_pressure, scale

matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt

simulation = Simulation()
figure = plt.figure()
ca_plot = plt.imshow(simulation.pressure, cmap='seismic', interpolation='bilinear', vmin=min_presure,
                     vmax=max_pressure)
plt.colorbar(ca_plot)


def animation_func(i):
    simulation.step()
    ca_plot.set_data(simulation.pressure)
    return ca_plot


animation = FuncAnimation(figure, animation_func, interval=1)
mng = plt.get_current_fig_manager()
mng.window.showMaximized()
plt.title(f"1 m -> {scale} cells, 1 cell -> {1 / scale}m")
plt.show()
