#!/usr/bin/env python3
"""
plot_fig1_dual_scale.py
Figure 1: Coarse-quantum vs fine-quantum dual-scale neural information processing.
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

fig, ax = plt.subplots(figsize=(8, 5))

# Coarse layer
ax.add_patch(mpatches.FancyBboxPatch((0.5, 2.5), 8, 1.2, boxstyle="round,pad=0.05", color='#E63946', alpha=0.2))
ax.text(4.5, 3.3, "Coarse-quantum layer", ha='center', fontsize=12, weight='bold')
ax.text(4.5, 2.9, "Ions • Neurotransmitters • Action potentials • Synapses", ha='center', fontsize=10)

# Fine layer
ax.add_patch(mpatches.FancyBboxPatch((0.5, 0.8), 8, 1.2, boxstyle="round,pad=0.05", color='#457B9D', alpha=0.2))
ax.text(4.5, 1.6, "Fine-quantum layer (IRQIC)", ha='center', fontsize=12, weight='bold', color='#1D3557')
ax.text(4.5, 1.2, "Infrared photons • Quantum superposition • Microtubule waveguide", ha='center', fontsize=10)

# Bidirectional arrows
ax.annotate("", xy=(4.5, 2.5), xytext=(4.5, 2.0), arrowprops=dict(arrowstyle="<->", lw=2, color='black'))
ax.text(6.2, 2.25, "Decomposition\n& recombination", ha='center', fontsize=9)

ax.set_xlim(0, 9)
ax.set_ylim(0, 4.2)
ax.axis('off')
plt.title("Fig. 1 | Dual-scale model of neural information processing", fontsize=13)
plt.tight_layout()
plt.savefig("fig1_dual_scale.png", dpi=300)
plt.show()
