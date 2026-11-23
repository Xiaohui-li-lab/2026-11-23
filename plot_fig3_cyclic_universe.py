#!/usr/bin/env python3
"""
plot_fig3_cyclic_universe.py
Figure 3: Schematic of the consciousness-driven cyclic universe.
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

fig, ax = plt.subplots(figsize=(8, 4))

# Draw cycles as ellipses
centers = [(1.5, 2), (4.5, 2), (7.5, 2)]
labels = ["Universe $_n$", "Black-hole\nseed", "Universe $_{n+1}$"]
colors = ["#F18F01", "#C73E1D", "#6A994E"]

for (x, y), lab, col in zip(centers, labels, colors):
    ellipse = mpatches.Ellipse((x, y), 1.6, 1.0, color=col, alpha=0.7)
    ax.add_patch(ellipse)
    ax.text(x, y, lab, ha='center', va='center', fontsize=10, color='white', weight='bold')

# Arrows
ax.annotate("", xy=(3.2, 2), xytext=(2.3, 2), arrowprops=dict(arrowstyle="->", lw=2, color='#333'))
ax.annotate("", xy=(6.2, 2), xytext=(5.3, 2), arrowprops=dict(arrowstyle="->", lw=2, color='#333'))

# Stage labels
ax.text(2.75, 2.35, "Great\nRefinement", ha='center', fontsize=9)
ax.text(5.75, 2.35, "Bounce inside\nhorizon", ha='center', fontsize=9)

# Consciousness field
ax.text(4.5, 3.3, r"Consciousness field $\Psi_C$", ha='center', fontsize=12, style='italic')
ax.annotate("", xy=(4.5, 3.0), xytext=(4.5, 3.15), arrowprops=dict(arrowstyle="->", color='purple', lw=1.5))

ax.set_xlim(0, 9)
ax.set_ylim(1.0, 3.8)
ax.axis('off')
plt.title("Fig. 3 | Consciousness-driven cyclic universe model", fontsize=13)
plt.tight_layout()
plt.savefig("fig3_cyclic_universe.png", dpi=300)
plt.show()
