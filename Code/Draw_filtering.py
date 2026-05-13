import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Function to draw a block with text
def draw_block(ax, text, xy, transparent=False):
    if transparent:
        block = patches.Rectangle(xy, 1, 1, fill=None, edgecolor='none')
    else:
        block = patches.Rectangle(xy, 1, 1, fill=None, edgecolor='black')
    ax.add_patch(block)
    ax.text(xy[0] + 0.5, xy[1] + 0.5, text, ha='center', va='center')

# Create a figure and axis
fig, ax = plt.subplots(figsize=(8, 2))

# Draw addition/subtraction circle
circle = patches.Circle((3.3, 0.5), 0.1, fill=None, edgecolor='black')
ax.add_patch(circle)
ax.text(3.1, 0.2, '+', ha='center', va='center', fontsize=12)
ax.text(3.5, 0.2, '-', ha='center', va='center', fontsize=12)
# Draw input block x(t)
draw_block(ax, 'x(t)', (0.8, 0.5), transparent=True)

# Draw LTI system block
draw_block(ax, 'LTI system', (1.6, 0))

# Draw output block y(t)
draw_block(ax, 'y(t)', (2.4, 0.5), transparent=True)

# Connect input to LTI system
ax.arrow(1, 0.5, 0.5, 0, head_width=0.1, head_length=0.1, fc='black', ec='black', lw=1)

# Connect LTI system to output
ax.arrow(2.6, 0.5, 0.5, 0, head_width=0.1, head_length=0.1, fc='black', ec='black', lw=1)


# Connect z(t) to output
ax.arrow(4, 0.5, -0.5, 0, head_width=0.1, head_length=0.1, fc='black', ec='black', lw=1)

# Draw desired block z(t)
draw_block(ax, 'z(t)', (3.3, 0.5), transparent=True)

# Connect z(t) to output
ax.arrow(3.3, 0.4, 0, -1, head_width=0.1, head_length=0.1, fc='black', ec='black', lw=1)

# Draw desired block z(t)
draw_block(ax, 'e(t)', (2.8, -1.5), transparent=True)

# Set axis properties
ax.set_xlim(-1, 6)
ax.set_ylim(-1, 2)
ax.axis('off')

# Show the plot
plt.show()