from scipy.spatial import Voronoi, voronoi_plot_2d, Delaunay
import random as r
import matplotlib.pyplot as plt
import numpy as np

seed = r.randint(0, 10 ** 10)
#seed = 9
r.seed(seed)
x_upper = 10
x_lower = -10
y_upper = 10
y_lower = -10

points = np.array([[round(r.uniform(x_lower, x_upper), 2), round(r.uniform(y_lower, y_upper), 2)] for _ in range(3000)])

xs = [points[i][0] for i in range(len(points))]
ys = [points[i][1] for i in range(len(points))]

fig = plt.figure()
ax = fig.add_subplot('111')
ax.scatter(xs, ys, s = 0.6, color = 'k')

vor = Voronoi(points)
tri = Delaunay(points)
#ax.triplot(xs, ys, color='r', linewidth = 0.7)
voronoi_plot_2d(vor, show_points = False, show_vertices = False, line_width = 0.5, ax = ax, line_alpha = 1)
plt.axis('off')
plt.savefig("voronoi_2d.pdf", bbox_inches='tight')
plt.show()


