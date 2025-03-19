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
    [51.28, 60.90, 84.92, 82.25, 87.70],
    [57.42, 71.35, 87.12, 85.27, 88.63],
    [56.93, 67.93, 76.57, 86.43, 89.80],
    [48.43, 58.70, 64.60, 72.93, 80.90],
    [67.56, 69.68, 81.32, 85.81, 91.69]
]
# 19.13
labels = ["Tip", "Tip-F", "CoOp", "CoCoOp", "Ours"]

# Example usage with save path
plot_data(x, ys, labels, line_width=5, marker_size=18, font_size=35, x_limit=(-0.2, 4.2), y_limit=(39, 92.5),
          save_path='fig51.pdf')
