from agri_uav_optimal_control.planner import straight_line_plan
from agri_uav_optimal_control.metrics import path_length
from agri_uav_optimal_control.visualization import plot_path


def main():
    path = straight_line_plan((0.0, 0.0), (10.0, 6.0), steps=20)
    print(f"Path length: {path_length(path):.3f}")
    fig, _ = plot_path(path, title="Agri-UAV Demo")
    fig.savefig("demo_path.png", dpi=150, bbox_inches="tight")
    print("Saved: demo_path.png")


if __name__ == "__main__":
    main()
