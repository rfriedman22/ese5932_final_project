# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 14:38:34 2020

@author: kdutta01
"""

import os
import numpy as np
import matplotlib.pyplot as plt
import scipy.io as scio
from skimage.metrics import structural_similarity as ssim
from skimage.metrics import peak_signal_noise_ratio as psnr
from skimage.metrics import mean_squared_error as mse

data_dir = "data"
results_dir = "results"
ssim_array = []
psnr_array = []
mse_array = []

path_data = os.path.join(data_dir,"project_data.mat")
original_image = scio.loadmat(path_data)["imgref"]
plt.imshow(original_image, cmap = 'gray')

datasets = [(os.path.join(results_dir,"reconstructionFullReconstruction.txt")),
            (os.path.join(results_dir,"reconstruction270Reconstruction.txt")),
            os.path.join(results_dir,"reconstruction90Reconstruction.txt")]

for i in range(0,len(datasets)):
    image_recon = np.loadtxt(datasets[i]);
    ssim_array.append(ssim(original_image, image_recon, data_range = original_image.max() - original_image.min()))
    psnr_array.append(psnr(original_image, image_recon, data_range = original_image.max() - original_image.min()))
    mse_array.append(mse(original_image, image_recon))
    
