from dataclasses import dataclass, field
from typing import List, Tuple

Point = Tuple[float, float]

@dataclass
class CircleObstacle:
    center: Point
    radius: float

@dataclass
class RectangleObstacle:
    center: Point
    width: float
    height: float

@dataclass
class AgriScene:
    start: Point
    goal: Point
    circles: List[CircleObstacle] = field(default_factory=list)
    rectangles: List[RectangleObstacle] = field(default_factory=list)
    safe_distance: float = 1.0
