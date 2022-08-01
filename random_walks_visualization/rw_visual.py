import matplotlib.pyplot as plt
from random_walks import RandomWalk

while True:
    rw = RandomWalk(5_000)
    rw.walk_fill()

    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(10, 9))
    point_nums = range(rw.num_points)
    ax.scatter(0, 0, c='green', edgecolor='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='blue', edgecolors='none', s=100)
    ax.plot(rw.x_values, rw.y_values, linewidth=0.1)

    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    plt.show()

    keep_running = input("Would you like to make another walk? (y/n)> ")
    if keep_running.lower() == 'n':
        break