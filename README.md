# ESE5932 final project
## Authors: Kaushik Dutta, Ryan Friedman, and Siqi Zhao

This repository contains all code necessary to reproduce results for the ESE 5932 Spring 2020 final project. The generation of the forward operators and sinograms is implemented in MATLAB, all other code is implemented with Python 3 in Jupyter notebooks. The following packages are required to run the Jupyter notebooks:
* matplotlib
* numpy and scipy
* pandas
* pyunlocbox
* scikit-image

In addition, the <code>paralleltomo.m</code> is required to generate the forward operators. This code is included for convenience. We have also included the Python file <code>plot_utils.py</code>, which generates default rcParams for plotting in matplotlib.

The <code>doc</code> directory contains LaTeX and PDF files for the final report. The other directories are described below.

## Step 1: Generate forward operators and sinograms
Run the script <code>1_prepare_inputs.m</code>. This loads in the project data from <code>data/project_data.mat</code> and outputs a sinogram and forward operator (AKA <code>A</code>) for 540 (full image), 270, and 90 views. All files are output as <code>.mat</code> to the <code>data</code> directory.

## Step 2: Run FISTA
Run the Jupyter notebook <code>2_fista.ipynb</code>. This uses <code>pyunlocbox</code> as the implementation for FISTA. It reconstructs the image using total variation for multiple regularization parameters and generates an L-curve. All figures and reconstructed images are output in the <code>results</code> directory.

## Step 3: Run SART
Run the Jupyter notebook <code>3_sart.ipynb</code>. This uses our own implementation of the SART algorithm to reconstruct the image. As before, the reconstructed images are output in the <code>results</code> directory.

## Step 4: Assess image quality
Run the Jupyter notebook <code>4_quality.ipynb</code>. This uses <code>scikit-image</code> to compute the SSIM and MSE for the full image and over an ROI for the reconstructions using FISTA and SART. The results are output to <code>results/ssimMetrics.txt</code> and <code>results/mseMetrics.txt</code>.
