from haucs import data
import matplotlib.pyplot as plt

poly = data.dataset.polygon(num_vrtx=4, xlims=[0, 1], ylims=[0, 1])
multipoly,_ = poly.create_polygons(3)

pond = data.dataset.ponds(num_pts=100, polygon = multipoly)

pond.plot_pts()
plt.show()
print(pond.loc)