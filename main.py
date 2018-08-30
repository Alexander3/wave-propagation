from sys import argv

import matplotlib
from matplotlib.animation import FuncAnimation, FFMpegWriter
from matplotlib.colors import LinearSegmentedColormap, colorConverter

from simulation import Simulation, min_presure, max_pressure, scale, wall

matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt

simulation = Simulation()
figure = plt.figure()
ca_plot = plt.imshow(simulation.pressure, cmap='seismic', interpolation='bilinear', vmin=min_presure, vmax=max_pressure)
plt.colorbar(ca_plot)
transparent = colorConverter.to_rgba('black', alpha=0)
wall_colormap = LinearSegmentedColormap.from_list('my_colormap', [transparent, 'green'], 2)
plt.imshow(wall, cmap=wall_colormap, interpolation='bilinear', zorder=2)


def animation_func(i):
    simulation.step()
    ca_plot.set_data(simulation.pressure)
    return ca_plot


if len(argv) > 2 and argv[2] == 'save':
    writer = FFMpegWriter(fps=30)
    frames = 100
    with writer.saving(figure, "writer_test.mp4", 200):
        for i in range(frames):
            animation_func(i)
            writer.grab_frame()
            print(f'\rframe: {i}/{frames}', end='')
else:
    animation = FuncAnimation(figure, animation_func, interval=1)
    mng = plt.get_current_fig_manager()
    mng.window.showMaximized()
    plt.title(f"1 m -> {scale} cells, 1 cell -> {1 / scale}m")
    plt.show()
