import matplotlib

from simulation import Simulation, min_presure, max_pressure

matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt

simulation = Simulation()

for i in range(50):
    simulation.step()

ca_plot = plt.imshow(simulation.pressure, interpolation='bilinear', vmin=min_presure, vmax=max_pressure)
plt.colorbar(ca_plot)
plt.show()
