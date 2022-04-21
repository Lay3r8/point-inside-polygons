import random
import argparse
from typing import Final

from matplotlib import pyplot
from matplotlib.patches import Polygon as PolygonPatch
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon
from alive_progress import alive_bar

# TODO: Have a look at this project as well: https://geopandas.org/en/stable/getting_started.html

# The diagram area
SIZE_X_AXIS: Final = 1
SIZE_Y_AXIS: Final = 1

# Results path
PDF_PATH: Final = 'output/points_in_polygon.pdf'


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--points', help='Number of points to test.', type=int)
    parser.add_argument('-r', help='Record the result to a PDF file instead of just showing it on screen', action='store_true')
    args = parser.parse_args()

    # Number of random points
    count_points: Final = args.points or 1000

    # The polygon TODO: randomize this (can be hard to do though...)
    polygon = Polygon([(0.1, 0.3), (0.1, 0.6), (0.4, 0.7), (0.8, 0.7), (0.8, 0.3), (0.5, 0.5)])

    print('Prepare the pyplot figure...')
    figure = pyplot.figure()
    axes = figure.add_subplot(1, 1, 1, aspect='equal')
    axes.set_title(f'Test the point_in_polygon function with \n {polygon}')
    axes.set_xlim(0, SIZE_X_AXIS)
    axes.set_ylim(0, SIZE_Y_AXIS)

    print('Drawing the polygon...')
    axes.add_patch(PolygonPatch(polygon.exterior.coords, linewidth=1, edgecolor='k', facecolor='none'))

    print('Plotting the point...')
    with alive_bar(count_points, bar='filling', spinner='waves') as bar:
        for _ in range(count_points):
            x = random.uniform(0, SIZE_X_AXIS)
            y = random.uniform(0, SIZE_Y_AXIS)
            point = Point(x, y)
            if polygon.contains(point):
                pyplot.plot(x, y, '.g')
            else:
                pyplot.plot(x, y, '.r')
            bar()

    if args.r:
        print(f'Saving results in {PDF_PATH}')
        figure.savefig(PDF_PATH)
    else:
        pyplot.show()

    print('Done!')


if __name__ == '__main__':
    main()
