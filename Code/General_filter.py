# Draw Block Diagram
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

# Draw input block x(t)
draw_block(ax, 'x(t)', (1, 0.5), transparent=True)

# Draw LTI system block
draw_block(ax, 'LTI system', (2, 0.1))

# Draw output block y(t)
draw_block(ax, '$y(t) = \hat{z(t)}$', (3, 0.5), transparent=True)

# Connect input to LTI system
ax.arrow(1, 0.6, 0.8, 0, head_width=0.1, head_length=0.1, fc='black', ec='black', lw=1)

# Connect LTI system to output
ax.arrow(3, 0.6, 0.8, 0, head_width=0.1, head_length=0.1, fc='black', ec='black', lw=1)
ax.arrow(5, 0.6, -0.8, 0, head_width=0.1, head_length=0.1, fc='black', ec='black', lw=1)
ax.arrow(4, 0.5, 0.0, -0.3, head_width=0.1, head_length=0.1, fc='black', ec='black', lw=1)

#Draw desired signal  block y(t)
draw_block(ax, 'z(t)', (4.1, 0.5), transparent=True)

draw_block(ax, 'e(t)', (3.8, -0.4), transparent=True)

circle = patches.Circle((4, 0.6), 0.1, fill=None, edgecolor='black')
ax.add_patch(circle)
ax.text(3.9, 0.4, '+', ha='center', va='center', fontsize=10)
ax.text(4.1, 0.5, '_', ha='center', va='center', fontsize=10)

# Set axis properties
ax.set_xlim(-1, 7)
ax.set_ylim(0, 2)
ax.axis('off')


# Show the plot
plt.show()
