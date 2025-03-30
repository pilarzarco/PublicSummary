import os
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from matplotlib import rcParams

# Configure matplotlib to use LaTeX
rcParams['text.usetex'] = True
rcParams['font.family'] = 'serif'
rcParams['font.size'] = 12

st.set_page_config(page_title="Matter Power Spectrum", layout="wide", page_icon="📊")

# =================================================================
# NARRATIVE THEORY SECTION (FORMAL REWORDING)
# =================================================================
st.title("Matter Power Spectrum Explorer")

with st.expander("🌟 Understanding the Matter Power Spectrum", expanded=True):
    st.markdown(r"""
    The **matter power spectrum** ($P(k)$) is a critical tool in cosmology that describes the statistical distribution of matter across various spatial scales. It provides insights into the distribution of large-scale structures, such as galaxy clusters, and the formation of smaller structures, like individual galaxies, by quantifying the density fluctuations that exist throughout the universe.

    ### The Structure of the Spectrum
    The power spectrum is determined by the degree of clustering of matter at different scales:
    - **Small $k$ values** (large scales) represent large structures like galaxy superclusters, which are the major components of the cosmic web.
    - **Large $k$ values** (small scales) correspond to smaller structures such as individual galaxies or smaller cosmic entities.

    The power spectrum is mathematically expressed as:

    $$ P(k) = \langle | \delta_k |^2 \rangle $$

    where \( k \) is the wave number, linked to the spatial scale by \( k = 2\pi/\lambda \), and \( \delta_k \) represents the Fourier transform of the matter density contrast. Analyzing the power spectrum allows us to study how matter has been distributed and how this distribution evolved since the early universe.

    ### Cosmological Parameters
    Several fundamental cosmological parameters influence the shape and characteristics of the matter power spectrum:
    - **$H_0$ (Hubble Constant)**: This parameter defines the current rate of expansion of the universe. It determines the overall scaling of the power spectrum.
    - **$\Omega_m$ (Matter Density)**: Represents the total matter content of the universe, including both dark matter and baryons. A higher value of \( \Omega_m \) leads to more pronounced clustering in the power spectrum.
    - **$\Omega_b$ (Baryon Density)**: Refers to the fraction of normal (baryonic) matter in the universe. It affects the fine structure of the spectrum, particularly at smaller scales.
    - **$n_s$ (Spectral Index)**: This parameter describes the tilt of the power spectrum. It influences whether large or small scales dominate in terms of matter distribution.
    - **$A_s$ (Amplitude)**: The amplitude controls the strength of the initial fluctuations in the early universe, determining the overall size of the density perturbations.

    ### Baryon Acoustic Oscillations (BAOs)
    One of the most significant features of the matter power spectrum is the presence of **Baryon Acoustic Oscillations (BAOs)**, which appear as a characteristic peak in the spectrum around \( k \approx 0.1 \, \text{Mpc}^{-1} \). These oscillations are the result of pressure waves that propagated through the plasma of the early universe:
    
    1. **Origin**: In the early universe, photons and baryons were tightly coupled in a hot plasma, causing sound waves to propagate through the medium.
    2. **Freezing of the Waves**: When the universe cooled sufficiently for atoms to form (during recombination), the pressure waves "froze" into the distribution of matter, leaving behind a distinctive imprint.
    3. **Legacy**: These frozen sound waves are visible today as BAOs and provide a valuable "standard ruler" for measuring cosmic distances. Their position in the power spectrum is a key probe of the expansion history of the universe, particularly in relation to dark energy.

    The BAO feature is sensitive to several cosmological parameters, especially \( \Omega_b \) (baryon density) and \( A_s \) (amplitude). Variations in these parameters can alter the strength and sharpness of the BAO peak, allowing researchers to refine measurements of the universe's expansion.
    """)

# =================================================================
# YOUR ORIGINAL CODE (UNCHANGED)
# =================================================================
# Path to the directory containing your CSV files
directory = '/Users/pilarzarco/Desktop/MPhys/Public_Summary/matter_power_spectra/'

# Load only CSV filenames from the directory
filenames = [f for f in os.listdir(directory) if f.endswith('.csv')]

# Extract unique parameter values from the filenames
parameters = {
    'h0': set(),
    'omega_m': set(),
    'omega_b': set(),
    'ns': set(),
    'ln10As': set()
}

for filename in filenames:
    try:
        parts = filename.strip().split('_')
        h0 = float(parts[1])
        omega_m = float(parts[4])
        omega_b = float(parts[7])
        ns = float(parts[9])
        ln10As = float(parts[11].replace('.csv', ''))
        
        parameters['h0'].add(h0)
        parameters['omega_m'].add(omega_m)
        parameters['omega_b'].add(omega_b)
        parameters['ns'].add(ns)
        parameters['ln10As'].add(ln10As)
    except (ValueError, IndexError) as e:
        continue

# Convert to sorted lists and round to 2 decimals for display
parameters_display = {
    'h0': sorted([round(x, 2) for x in parameters['h0']]),
    'omega_m': sorted([round(x, 2) for x in parameters['omega_m']]),
    'omega_b': sorted([round(x, 2) for x in parameters['omega_b']]),
    'ns': sorted([round(x, 2) for x in parameters['ns']]),
    'ln10As': sorted([round(x, 2) for x in parameters['ln10As']])
}

# Keep original precision for file lookup
parameters_exact = {
    k: sorted(list(v)) for k, v in parameters.items()
}

# Streamlit app setup
st.title('Matter Power Spectrum Interactive Plot')

def find_closest(display_val, exact_vals):
    """Find the closest exact value to the displayed value"""
    return min(exact_vals, key=lambda x: abs(x - display_val))

# SIDEBAR CONTROLS
with st.sidebar:
    st.header("Cosmological Parameters")
    
    h0_display = st.select_slider(
        r'$H_0$ (km/s/Mpc)',
        options=parameters_display['h0'],
        value=float(f"{parameters_display['h0'][0]:.2f}")
    )
    h0 = find_closest(h0_display, parameters_exact['h0'])

    omega_m_display = st.select_slider(
        r'$\Omega_m$ (Matter density)',
        options=parameters_display['omega_m'],
        value=float(f"{parameters_display['omega_m'][0]:.2f}")
    )
    omega_m = find_closest(omega_m_display, parameters_exact['omega_m'])

    omega_b_display = st.select_slider(
        r'$\Omega_b$ (Baryon density)',
        options=parameters_display['omega_b'],
        value=float(f"{parameters_display['omega_b'][0]:.2f}")
    )
    omega_b = find_closest(omega_b_display, parameters_exact['omega_b'])

    ns_display = st.select_slider(
        r'$n_s$ (Spectral index)',
        options=parameters_display['ns'],
        value=float(f"{parameters_display['ns'][0]:.2f}")
    )
    ns = find_closest(ns_display, parameters_exact['ns'])

    ln10As_display = st.select_slider(
        r'$\ln(10^{10}A_s)$ (Amplitude)',
        options=parameters_display['ln10As'],
        value=float(f"{parameters_display['ln10As'][0]:.2f}")
    )
    ln10As = find_closest(ln10As_display, parameters_exact['ln10As'])

# MAIN CONTENT AREA
filename = f"h0_{h0}_omega_m_{omega_m}_omega_b_{omega_b}_ns_{ns}_ln10As_{ln10As}.csv"
filepath = os.path.join(directory, filename)

# Load and plot data with LaTeX formatting
if os.path.exists(filepath):
    df = pd.read_csv(filepath)
    
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.loglog(df['k [1/Mpc]'], df['P(k) [Mpc^3]'], linewidth=2)
    
    ax.set_xlabel(r'$k\ [\mathrm{Mpc}^{-1}]$', fontsize=14)
    ax.set_ylabel(r'$P(k)\ [\mathrm{Mpc}^3]$', fontsize=14)
    ax.set_title(
        r'Matter Power Spectrum $P(k)$' + '\n' +
        fr'$H_0={h0:.2f}$, $\Omega_m={omega_m:.2f}$, $\Omega_b={omega_b:.2f}$' + '\n' +
        fr'$n_s={ns:.2f}$, $\ln(10^{10}A_s)={ln10As:.2f}$',
        fontsize=12
    )

    st.pyplot(fig)
else:
    st.error(f"File not found: {filename}")

# DYNAMIC INTERPRETATION
if 'k' in locals() and os.path.exists(filepath):  # Only show if plot exists
    with st.expander("🔍 Reading the Spectrum"):
        st.markdown(f"""
        **What You're Seeing Now** (for $H_0={h0:.2f}$, $\Omega_m={omega_m:.2f}$):
        
        - **Left Side (Large Scales)**: The gentle rise shows how gravity built superclusters 
          from tiny initial fluctuations. Try increasing $\Omega_m$ to boost the clustering.
        
        - **Right Side (Small Scales)**: The falling slope reveals galaxy-scale structure. 
          Notice how $n_s$ changes the steepness here.
        
        """)
