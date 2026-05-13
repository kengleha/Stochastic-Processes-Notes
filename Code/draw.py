import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Function to draw a block with text
def draw_block(ax, text, xy, transparent=False):
    if transparent:
        block = patches.Rectangle(xy, 1.6, 1, fill=None, edgecolor='none')
    else:
        block = patches.Rectangle(xy, 1.6, 1, fill=None, edgecolor='black')
    ax.add_patch(block)
    ax.text(xy[0] + 0.8, xy[1] + 0.5, text, ha='center', va='center')

# Create a figure and axis
fig, ax = plt.subplots(figsize=(8, 2))

# Draw input block x(t)
draw_block(ax, '$\{A_i\}$', (0.5, 0), transparent=True)

# Draw LTI system block
draw_block(ax, 'Communication channel', (2.0, 0))

# Draw output block y(t)
draw_block(ax, '$\{B_j\}$', (3.5, 0), transparent=True)

# Connect input to LTI system
ax.arrow(1.5, 0.5, 0.4, 0, head_width=0.1, head_length=0.1, fc='black', ec='black', lw=1)

# Connect LTI system to output
ax.arrow(3.6, 0.5, 0.4, 0, head_width=0.1, head_length=0.1, fc='black', ec='black', lw=1)

# Set axis properties
ax.set_xlim(-1, 5)
ax.set_ylim(-1, 2)
ax.axis('off')

# Show the plot
plt.show()

