import matplotlib.pyplot as plt


def plot_path(path, title: str = "Demo Path"):
    xs = [p[0] for p in path]
    ys = [p[1] for p in path]
    fig, ax = plt.subplots()
    ax.plot(xs, ys, marker="o")
    ax.set_title(title)
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.axis("equal")
    return fig, ax
