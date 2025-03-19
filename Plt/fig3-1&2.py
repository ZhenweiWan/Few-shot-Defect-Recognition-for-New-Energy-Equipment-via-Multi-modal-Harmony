import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')

# Data
x = [1, 2, 4, 8, 16]
# y0 = [59.40, 61.06, 77.53, 82.02, 91.15]
# y1 = [58.89, 62.88, 78.38, 82.13, 91.07]
# y2 = [60.32, 62.49, 78.32, 82.75, 91.06]
# y3 = [62.33, 65.16, 79.78, 84.57, 91.30]

y0 = [66.70, 72.33, 76.11, 77.80, 81.06]
y1 = [67.11, 72.33, 75.99, 77.05, 80.94]
y2 = [67.23, 72.04, 75.01, 77.38, 81.00]
y3 = [68.00, 72.60, 76.34, 78.03, 81.21]


# Define the font size and bar settings
font_size = 19
bar_width = 0.2
hatches = ['//', '\\\\', 'xx', '*']
edge_colors = ['#7f7f7f', '#629dc8', '#cf88f2', '#CD8500']

# Create figure
plt.figure(figsize=(10, 10))

# Plot bars for each dataset
for i in range(len(x)):
    plt.bar(i - 3/2 * bar_width, y0[i] - 55, bottom=55, width=bar_width, label='Zero' if i == 0 else "",
            color='white', edgecolor=edge_colors[0], hatch=hatches[0], linewidth=2.5)

    plt.bar(i - 1/2 * bar_width, y1[i] - 55, bottom=55, width=bar_width, label='Uniform' if i == 0 else "",
            color='white', edgecolor=edge_colors[1], hatch=hatches[1], linewidth=2.5)

    plt.bar(i + 1/2 * bar_width, y2[i] - 55, bottom=55, width=bar_width, label='Normal' if i == 0 else "",
            color='white', edgecolor=edge_colors[2], hatch=hatches[2], linewidth=2.5)

    plt.bar(i + 3/2 * bar_width, y3[i] - 55, bottom=55, width=bar_width, label='Text Feature' if i == 0 else "",
            color='white', edgecolor=edge_colors[3], hatch=hatches[3], linewidth=2.5)

# Set axes labels, ticks, and limits
plt.xlabel('Shot', fontsize=font_size + 15)
plt.ylabel('Accuracy (%)', fontsize=font_size + 15)
plt.xticks(range(len(x)), x, fontsize=font_size + 15)
plt.yticks(range(55, 96, 5), fontsize=font_size + 15)
plt.ylim(55, 93)
plt.xlim(-0.75, len(x) - 0.25)

plt.grid(axis='y', linestyle='--', linewidth=0.5, color='gray')


# Add legend
plt.legend(loc='upper left', prop={'size': font_size + 10})

# Customize axes
plt.gca().spines['bottom'].set_linewidth(1)
plt.gca().spines['left'].set_linewidth(1)
plt.gca().spines['right'].set_linewidth(1)
plt.gca().spines['top'].set_linewidth(1)

# Save the plot
file_path_with_y0 = 'fig32.pdf'
plt.savefig(file_path_with_y0)
