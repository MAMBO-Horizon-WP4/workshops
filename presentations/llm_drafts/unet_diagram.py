import matplotlib.pyplot as plt
import matplotlib.patches as patches
import os

# Set style
plt.style.use('seaborn-v0_8')

# Create figure and axis
fig, ax = plt.subplots(figsize=(12, 6))
ax.set_xlim(0, 12)
ax.set_ylim(0, 6)
ax.axis('off')

# Helper function to draw boxes
def draw_box(x, y, label, color):
  box = patches.FancyBboxPatch((x, y), 1.5, 1, boxstyle="round,pad=0.1", edgecolor='black', facecolor=color)
  ax.add_patch(box)
  ax.text(x + 0.75, y + 0.5, label, ha='center', va='center', fontsize=10)

# Encoder blocks
encoder_colors = ['lightblue'] * 4
for i, color in enumerate(encoder_colors):
  draw_box(0.5 + i*1.5, 4.5, f"Enc {i+1}", color)

# Decoder blocks
decoder_colors = ['lightgreen'] * 4
for i, color in enumerate(decoder_colors):
  draw_box(6.5 + i*1.5, 1.5, f"Dec {4-i}", color)

# Skip connections
for i in range(4):
  ax.annotate('', xy=(0.5 + i*1.5 + 0.75, 4.5), xytext=(6.5 + (3-i)*1.5 + 0.75, 2.5),
                              arrowprops=dict(arrowstyle='->', color='gray'))

# Attention gates
attention_positions = [(6.5 + (3-i)*1.5, 3.5) for i in range(4)]
for i, (x, y) in enumerate(attention_positions):
  draw_box(x, y, f"Attn {i+1}", 'salmon')

# Input and Output
draw_box(0, 5.5, "Input", 'orange')
draw_box(11, 0.5, "Output", 'orange')

# Save diagram
output_path = "/mnt/data/attention_unet_architecture.svg"
os.makedirs(os.path.dirname(output_path), exist_ok=True)
plt.savefig(output_path, format='svg')
plt.close()

print("SVG diagram saved as attention_unet_architecture.svg")

