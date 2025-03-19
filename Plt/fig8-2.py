import matplotlib.pyplot as plt
import numpy as np
import matplotlib

matplotlib.use('TkAgg')


def plot_data(x, ys, labels, line_width=2.5, marker_size=10, font_size=20, x_limit=None, y_limit=None, save_path=None):
    # Adjusting x-axis for unit distance
    x_unit_distance = list(range(len(x)))

    # Line styles and colors
    linestyle = ['--', '--', '-.', 'dashdot', 'solid', ':']
    color = ['#629dc8', '#cf88f2', '#40E0D0', '#CD8500', '#EE0000', '#FF8571']
    marker = ['v', '4', '1', 'x', 'o']

    # Drawing the line chart
    plt.figure(figsize=(12, 10))
    for i, y in enumerate(ys):
        plt.plot(x_unit_distance, y, linestyle=linestyle[i], label=labels[i], marker=marker[i],
                 markerfacecolor='none', color=color[i], linewidth=line_width, markersize=marker_size,
                 fillstyle='full', clip_on=False)

    plt.grid(axis='y', linestyle=':', which='major', color="#BDBDBD", fillstyle='full')
    plt.legend(loc=2, ncol=2, fontsize=font_size, markerscale=1.2, columnspacing=0.4, frameon=True, fancybox=True)
    plt.xticks(ticks=x_unit_distance, labels=x, fontsize=font_size)
    plt.yticks(fontsize=font_size)
    plt.xlabel('Shot', fontdict={'weight': 'normal', 'size': font_size})
    plt.ylabel('Accuracy(%)', fontdict={'weight': 'normal', 'size': font_size})
    plt.tick_params(labelsize=font_size, color='#474747')

    # Setting axis limits
    ax = plt.gca()
    if x_limit is not None:
        ax.set_xlim(x_limit)
    if y_limit is not None:
        ax.set_ylim(y_limit)

    # Spine styles
    for spine in ax.spines.values():
        spine.set_color('gray')
        spine.set_linewidth(1)
    plt.legend(loc='lower right', prop={'size': font_size - 12})

    # Save plot as PDF if a save path is provided
    if save_path:
        plt.savefig(save_path, format='pdf', bbox_inches='tight')

    plt.show()


# Data
x = [1, 2, 4, 8, 16]
ys = [
    [51.51, 57.66, 71.35, 82.25, 81.90],
    [48.72, 70.07, 81.67, 88.75, 90.84],
    [59.57, 62.83, 75.27, 84.37, 89.67],
    [45.37, 54.63, 64.07, 77.60, 79.80],
    [62.76, 70.69, 75.44, 85.65, 91.19]
]
labels = ["Tip", "Tip-F", "CoOp", "CoCoOp", "Ours"]

# Example usage with save path
plot_data(x, ys, labels, line_width=5, marker_size=18, font_size=35, x_limit=(-0.2, 4.2), y_limit=(39, 92.5),
          save_path='fig52.pdf')
