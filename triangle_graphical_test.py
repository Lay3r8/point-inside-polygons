import random

from matplotlib import pyplot
from matplotlib.patches import Polygon

from triangle import point_in_triangle


# The diagram area
size_x = 1
size_y = 1

# The triangle
triangle = ((0, 0), (0, 1), (1, 1))

# Number of random points
count_points = 10000

# Prepare the figure
figure = pyplot.figure()
axes = figure.add_subplot(1, 1, 1, aspect='equal')
axes.set_title(f'Test the point_in_triangle function with triangle = {triangle}')
axes.set_xlim(0, size_x)
axes.set_ylim(0, size_y)

# Plot the triangle
axes.add_patch(Polygon(triangle, linewidth=1, edgecolor='k', facecolor='none'))

# Plot the points
for i in range(count_points):
    x = random.uniform(0, size_x)
    y = random.uniform(0, size_y)
    if point_in_triangle((x,y), triangle):
        pyplot.plot(x, y, '.g')
    else:
        pyplot.plot(x, y, '.r')


# Save it
figure.savefig('output/point_in_triangle.pdf')
