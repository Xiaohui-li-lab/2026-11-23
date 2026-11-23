#!/usr/bin/env python3
"""
plot_fig4_coherence_vs_temperature.py
Figure 4: Theoretical infrared coherence length as a function of effective neural temperature.
"""

import numpy as np
import matplotlib.pyplot as plt

k_B = 8.617333262e-5
E_g = 25e-3
tau_0 = 10e-15
v_g = 299792458 / 4

T = np.linspace(240, 320, 200)
L = v_g * tau_0 * np.exp(E_g / (k_B * T)) * 1e9  # nm

plt.figure(figsize=(6, 4.5))
plt.plot(T, L, color='#2E86AB', linewidth=2.5)
plt.fill_between(T, L, alpha=0.15, color='#2E86AB')
plt.xlabel("Effective neural temperature $T_{\\mathrm{eff}}$ (K)", fontsize=12)
plt.ylabel("Coherence length $L_c$ (nm)", fontsize=12)
plt.title("Fig. 4 | Infrared coherence length in the IRQIC model", fontsize=13)
plt.axvline(300, color='gray', linestyle='--', alpha=0.6, label='Room temperature')
plt.legend()
plt.tight_layout()
plt.savefig("fig4_coherence_vs_temperature.png", dpi=300)
plt.show()
