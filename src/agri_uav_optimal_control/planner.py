from typing import List, Tuple

Point = Tuple[float, float]


def straight_line_plan(start: Point, goal: Point, steps: int = 50) -> List[Point]:
    """Simple placeholder planner to bootstrap the repository."""
    xs = [start[0] + (goal[0] - start[0]) * i / (steps - 1) for i in range(steps)]
    ys = [start[1] + (goal[1] - start[1]) * i / (steps - 1) for i in range(steps)]
    return list(zip(xs, ys))
