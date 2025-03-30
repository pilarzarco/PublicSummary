import numpy as np
import camb
from camb import model
import os
import pandas as pd

# Define parameter ranges
h0_values = np.linspace(50, 90, 5)  # Hubble constant
omega_m_values = np.linspace(0.1, 0.6, 6)  # Matter density
omega_b_values = np.linspace(0.01, 0.15, 6)  # Baryon density
ns_values = np.linspace(0.85, 1.15, 5)  # Spectral index
ln10As_values = np.linspace(2.0, 4.0, 5)  # Amplitude of scalar perturbations

# Create output folder
output_dir = "matter_power_spectra"
os.makedirs(output_dir, exist_ok=True)

def run_camb(h0, omega_m, omega_b, ns, ln10As):
    As = np.exp(ln10As) / 1e10  # Convert to A_s
    pars = camb.CAMBparams()
    pars.set_cosmology(H0=h0, 
                       ombh2=omega_b * h0**2 / 10000, 
                       omch2=(omega_m - omega_b) * h0**2 / 10000, 
                       mnu=0.06, omk=0, tau=0.06)
    pars.InitPower.set_params(As=As, ns=ns, r=0)
    pars.set_matter_power(redshifts=[0], kmax=10.0)
    
    # Get results
    results = camb.get_results(pars)
    k, z, pk = results.get_matter_power_spectrum(minkh=1e-4, maxkh=10, npoints=300)
    
    # Return k and pk data
    return k, pk[0]

# Loop over all parameter combinations and save results
for h0 in h0_values:
    for omega_m in omega_m_values:
        for omega_b in omega_b_values:
            for ns in ns_values:
                for ln10As in ln10As_values:
                    # Run CAMB simulation for current parameter set
                    k, pk_vals = run_camb(h0, omega_m, omega_b, ns, ln10As)
                    
                    # Create a file name based on parameters
                    filename = f"h0_{h0}_omega_m_{omega_m}_omega_b_{omega_b}_ns_{ns}_ln10As_{ln10As}.csv"
                    filepath = os.path.join(output_dir, filename)
                    
                    # Save k, P(k) to CSV
                    df = pd.DataFrame({"k [1/Mpc]": k, "P(k) [Mpc^3]": pk_vals})
                    df.to_csv(filepath, index=False)
                    print(f"Saved: {filepath}")

print("Grid generation complete!")
