from agri_uav_optimal_control.metrics import path_length


def test_path_length():
    assert abs(path_length([(0, 0), (3, 4)]) - 5.0) < 1e-9
