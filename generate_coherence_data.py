#!/usr/bin/env python3
"""
generate_coherence_data.py
Synthetic theoretical data for IRQIC coherence length vs effective neural temperature.
Model: L_c(T) = v_g * tau_0 * exp(E_g / (k_B * T))
"""

import numpy as np
import pandas as pd

# Physical constants
k_B = 8.617333262e-5  # eV/K
c = 299792458          # m/s

# Model parameters
E_g = 25e-3            # eV, effective gap
tau_0 = 10e-15         # s, characteristic scattering time
v_g = c / 4            # group velocity inside microtubule waveguide

T_eff = np.array([250, 260, 270, 280, 290, 300, 310], dtype=float)
L_c = v_g * tau_0 * np.exp(E_g / (k_B * T_eff))
L_c_nm = L_c * 1e9     # convert to nm

df = pd.DataFrame({"T_eff_K": T_eff, "L_c_nm": np.round(L_c_nm, 1)})
df.to_csv("coherence_length_vs_temperature.csv", index=False)
print(df)
