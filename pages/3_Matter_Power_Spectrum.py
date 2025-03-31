import os
import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import requests
from io import StringIO

# =========================
# Define parameter ranges as floats
# =========================
h0_values      = np.linspace(50.0, 90.0, 5)      # e.g., [50.0, 60.0, 70.0, 80.0, 90.0]
omega_m_values = np.linspace(0.1, 0.6, 6)        # e.g., [0.1, 0.2, 0.3, 0.4, 0.5, 0.6]
omega_b_values = np.linspace(0.01, 0.15, 6)      # e.g., [0.01, 0.04, 0.07, 0.10, 0.13, 0.15]
ns_values      = np.linspace(0.85, 1.15, 5)      # e.g., [0.85, 0.925, 1.0, 1.075, 1.15]
ln10As_values  = np.linspace(2.0, 4.0, 5)        # e.g., [2.0, 2.5, 3.0, 3.5, 4.0]


st.set_page_config(page_title="Matter Power Spectrum", page_icon="📊")

# =========================
# Theoretical Background (Part 1)
# =========================
st.markdown(r"""
# The Matter Power Spectrum: Mapping the Universe’s Structure

The universe’s matter isn’t distributed evenly—it clumps into galaxies, clusters, and vast cosmic voids.
To quantify these patterns, cosmologists use the matter power spectrum, **P(k)**, which reveals how much structure exists at different scales, from enormous superclusters to individual galaxies.

## Density Fluctuations and Fourier Space

At its core, the power spectrum analyzes **density fluctuations**, regions where matter is more or less concentrated than the cosmic average. By applying a **Fourier transform**, we break these fluctuations into waves of different sizes.
Each wavenumber **k** corresponds to a physical scale in the universe: small **k** values describe large, smooth structures (like superclusters), while large **k** values reveal smaller, detailed features (like galaxies).
**P(k)** then measures the strength of these fluctuations at each scale.

## Linear vs. Nonlinear Evolution

On large scales (low **k**), matter clustering is in the **linear regime**, where gravity gently amplifies the faint primordial fluctuations from the Big Bang. In this regime, theory predicts **P(k)** very precisely. However, on smaller scales (high **k**), gravity’s pull becomes chaotic, collapsing matter into dense halos and filaments—the **nonlinear regime**. Here, simulations are needed to model the steep rise in **P(k)** as structure grows.
""", unsafe_allow_html=True)
# =========================
# Callout Prompt
# =========================
st.info("Try changing the parameters in the sidebar to see how the matter power spectrum behaves under different cosmological conditions.")

# =========================
# Helper function for formatting float display
# =========================
def float_display(x):
    return f"{x:.2f}"

# =========================
# Sidebar Sliders (using numpy arrays with custom display format)
# =========================
with st.sidebar:
    st.header("Cosmological Parameters")
    h0      = st.select_slider(r"$H_0$",             options=list(h0_values),      value=h0_values[0],      format_func=float_display)
    omega_m = st.select_slider(r"$\Omega_m$",         options=list(omega_m_values), value=omega_m_values[0], format_func=float_display)
    omega_b = st.select_slider(r"$\Omega_b$",         options=list(omega_b_values), value=omega_b_values[0], format_func=float_display)
    ns      = st.select_slider(r"$n_s$",              options=list(ns_values),      value=ns_values[0],      format_func=float_display)
    ln10As  = st.select_slider(r"$\ln(10^{10}A_s)$",  options=list(ln10As_values),  value=ln10As_values[0],  format_func=float_display)

# =========================
# Google Drive API Settings & Helper Functions
# =========================
API_KEY = st.secrets["API_KEY"]
FOLDER_ID = st.secrets["FOLDER_ID"]

@st.cache_data
def get_files_from_drive():
    """Fetch CSV files from Google Drive with error handling."""
    try:
        url = f"https://www.googleapis.com/drive/v3/files?q='{FOLDER_ID}' in parents&key={API_KEY}"
        response = requests.get(url, timeout=50)
        response.raise_for_status()
        files = response.json().get('files', [])
        return [f for f in files if f['name'].lower().endswith('.csv')]
    except Exception as e:
        st.error(f"Failed to access Google Drive: {str(e)}")
        return []

def parse_filename(filename):
    """
    Extract parameter values from a filename.
    Expected filename format:
      <prefix>_<h0>_<...>_<omega_m>_<...>_<omega_b>_<...>_<n_s>_<...>_<ln10As>.csv
    """
    try:
        parts = filename.strip().split('_')
        h0_val      = float(parts[1])
        omega_m_val = float(parts[4])
        omega_b_val = float(parts[7])
        ns_val      = float(parts[9])
        ln10As_val  = float(parts[11].replace('.csv', ''))
        return h0_val, omega_m_val, omega_b_val, ns_val, ln10As_val
    except (ValueError, IndexError):
        return None

def read_csv_from_drive(file_id):
    """Read a CSV file directly from Google Drive using its file ID."""
    download_url = f"https://www.googleapis.com/drive/v3/files/{file_id}?alt=media&key={API_KEY}"
    response = requests.get(download_url, stream=True)
    if response.status_code == 200:
        return pd.read_csv(StringIO(response.text))
    else:
        st.error(f"Failed to fetch file with ID {file_id}. HTTP Status: {response.status_code}")
        return None

# =========================
# File Matching by Nearest Neighbor and Plotting the CSV Data
# =========================
filenames = get_files_from_drive()
matched_filename = None
min_distance = float('inf')

for file in filenames:
    parsed = parse_filename(file['name'])
    if parsed:
        h0_file, omega_m_file, omega_b_file, ns_file, ln10As_file = parsed
        # Compute a "distance" as the sum of absolute differences:
        distance = (abs(h0 - h0_file) +
                    abs(omega_m - omega_m_file) +
                    abs(omega_b - omega_b_file) +
                    abs(ns - ns_file) +
                    abs(ln10As - ln10As_file))
        if distance < min_distance:
            min_distance = distance
            matched_filename = file['name']

if matched_filename:
    file_id = next((f['id'] for f in filenames if f['name'] == matched_filename), None)
    if file_id:
        df = read_csv_from_drive(file_id)
        if df is not None:
            fig, ax = plt.subplots(figsize=(10, 6))
            ax.loglog(df['k [1/Mpc]'], df['P(k) [Mpc^3]'], linewidth=2)
            ax.set_xlabel(r'$k\ [\mathrm{Mpc}^{-1}]$', fontsize=14)
            ax.set_ylabel(r'$P(k)\ [\mathrm{Mpc}^3]$', fontsize=14)
            ax.set_title(
                r'Matter Power Spectrum $P(k)$' + '\n' +
                fr'$H_0={h0:.2f},\ \Omega_m={omega_m:.2f},\ \Omega_b={omega_b:.2f},\ n_s={ns:.2f},\ \ln(10^{{10}}A_s)={ln10As:.2f}$',
                fontsize=12
            )
            st.pyplot(fig)
        else:
            st.error("Failed to process the CSV file.")
    else:
        st.error(f"File ID not found for: {matched_filename}")
else:
    st.error("No matching file found.")

# =========================
# Theoretical Background (Part 2)
# =========================
st.markdown(r"""
## Baryon Acoustic Oscillations and Cosmic Fossils

Embedded in the power spectrum is a subtle bump near **k ≈ 0.05 h/Mpc**, a relic of **baryon acoustic oscillations (BAO)**. These are frozen sound waves from the early universe, acting as a standard ruler that helps measure cosmic expansion. At even larger scales, $P(k)$ turns over—a fossil imprint of the universe’s horizon size when matter first dominated over radiation. Together, these features encode the universe’s history, from its fiery beginnings to the web of galaxies we see today.

## Why It Matters

By measuring **P(k)**, we test fundamental theories of dark matter, inflation, and gravity. Its shape depends on cosmic ingredients like $\Omega_m$ (total matter density) and $n_s$ (primordial fluctuation strength), making it a powerful probe of both the universe’s composition and its evolution. Tools like **CAMB** compute it from first principles, while galaxy surveys map it in practice, bridging the gap between theory and observation.
""", unsafe_allow_html=True)
