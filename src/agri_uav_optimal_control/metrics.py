from math import hypot
from typing import Iterable, Tuple

Point = Tuple[float, float]


def path_length(path: Iterable[Point]) -> float:
    pts = list(path)
    if len(pts) < 2:
        return 0.0
    return sum(hypot(pts[i + 1][0] - pts[i][0], pts[i + 1][1] - pts[i][1]) for i in range(len(pts) - 1))
