import unittest

from shapely.geometry import Point
from shapely.geometry.polygon import Polygon


class TestPointInPolygon(unittest.TestCase):

    polygon = Polygon([(0.1, 0.3), (0.1, 0.6), (0.4, 0.7), (0.8, 0.7), (0.8, 0.3), (0.5, 0.5)])

    def test_inside(self):
        point = Point(0.499999999999, 0.5)
        self.assertTrue(self.polygon.contains(point))

    def test_outside(self):
        point = Point(0.5, 0.4)
        self.assertFalse(self.polygon.contains(point))

    def test_border_case(self):
        """If the point is exactly on one of the triangle's edges,
        we consider it is outside."""
        point = Point(0.5, 0.5)
        self.assertFalse(self.polygon.contains(point))


if __name__ == "__main__":
    test_suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestPointInPolygon)
    unittest.TextTestRunner().run(test_suite)
