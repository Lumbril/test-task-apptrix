from math import acos, sin, cos


def dist(ph1: float, ph2: float, la1: float, la2: float) -> float:
    sig = acos(sin(ph1) * sin(ph2) + cos(ph1) * cos(ph2) * cos(la2 - la1))
    m = 111000.0  # meters

    return m * sig
