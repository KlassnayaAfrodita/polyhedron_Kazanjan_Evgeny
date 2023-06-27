from pytest import approx
from math import sqrt
from common.r3 import R3
from shadow.polyedr import Edge, Polyedr


# class TestR3:
#     def test_abs(self):
#         vector = R3(1.0, 1.0, 1.0)
#         assert abs(vector) == approx(sqrt(3))


class Test_1:
    def test_good_point1(self):
        f = R3(0.5, 0.8, 0)
        assert not f.is_good_point() is True

    def test_good_point2(self):
        f = R3(1, 1, 1)
        assert f.is_good_point() is True

    def test_lenght_projection1(self):
        f = Edge(R3(5, 6, 0), R3(34, 7, 3))
        assert f.projection_lenght() == approx(29.01, 0.03)

    def test_lenght_projection2(self):
        f = Edge(R3(5, 6, 0), R3(5, 6, 0))
        assert f.projection_lenght() == 0


class Test_sum:
    def test1(self):
        Polyedr1 = Polyedr("data/test_pir.geom")
        assert Polyedr1.sum_projection() == approx(10.19, 0.03)

    def test2(self):
        Polyedr2 = Polyedr("data/test_tri.geom")
        assert Polyedr2.sum_projection() == approx(0.71, 0.03)

    def test3(self):
        Polyedr3 = Polyedr("data/king.geom")
        assert Polyedr3.sum_projection() == approx(11589.53, 0.03)
