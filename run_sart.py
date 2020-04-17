#!/usr/bin/env python3
"""
Wrapper to run SART
"""
import os
import matplotlib.pyplot as plt
import numpy as np
import scipy.io as scio
from scipy import sparse

import sart


data_dir = "data"
results_dir = "results"
# Tuples that are (sinogram file, sinogram variable name, imaging operator file, output prefix)
datasets = [
    (os.path.join(data_dir, "Sinogram90.mat"),
        "sinogram90",
        os.path.join(data_dir, "A90.mat"),
        os.path.join(results_dir, "reconstruction90")),
    (os.path.join(data_dir, "Sinogram270.mat"),
        "sinogram270",
        os.path.join(data_dir, "A270.mat"),
        os.path.join(results_dir, "reconstruction270")),
    (os.path.join(data_dir, "project_data.mat"),
        "sinogram",
        os.path.join(data_dir, "A.mat"),
        os.path.join(results_dir, "reconstructionFull")),
]

n_pixels = 256

for sinogram, name, operator, out_prefix in datasets:
    print(f"Running SART for {out_prefix}")
    # Read in the sinogram
    sinogram = scio.loadmat(sinogram)[name]
    sinogram = sinogram.flatten(order="F")

    # Read in the imaging operator and convert to CSR format
    operator = scio.loadmat(operator)["A"]
    operator = operator.tocsr()

    model_init = np.zeros(n_pixels**2)
    model, residual_norms, fig = sart.sart(operator, sinogram, model_init, plot_convergence=f"{out_prefix}Residuals")
    # Show the convergence history
    plt.show(fig)
    # Show the reconstructed image
    fig, ax = plt.subplots()
    ax.imshow(model, cmap="Greys")
    plt.show(fig)

    # Save the reconstruction to file
    np.savetxt(f"{out_prefix}Reconstruction.txt", model, fmt="%.2f", delimiter="\t", newline="\n")
