# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 14:38:34 2020

@author: kdutta01
"""

import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
import scipy.io as scio
from skimage.metrics import structural_similarity as ssim
from skimage.metrics import peak_signal_noise_ratio as psnr
from skimage.metrics import mean_squared_error as mse

data_dir = "data"
results_dir = "results"

ssim_array = []
mse_array = []

mse_array_roi = [];
ssim_array_roi = [];

path_data = os.path.join(data_dir,"project_data.mat")
original_image = scio.loadmat(path_data)["imgref"]
original_image_roi = original_image[175:220,100:140]

datasets = [(os.path.join(results_dir,"sartFullReconstruction.txt")),
            (os.path.join(results_dir,"sart270Reconstruction.txt")),
            os.path.join(results_dir,"sart90Reconstruction.txt"),
            os.path.join(results_dir,"tv_fista_full_image_beta_1e-3.txt")]

for i in range(0,len(datasets)):
    image_recon = np.loadtxt(datasets[i]);
    image_recon_roi = image_recon[175:220,100:140]
    
    # Global Image comparision Metrics
    ssim_array.append(ssim(original_image, image_recon, data_range = original_image.max() - original_image.min()))
    mse_array.append(mse(original_image, image_recon))
    
    # ROI Defined comparision Metrics
    ssim_array_roi.append(ssim(original_image_roi, image_recon_roi, data_range = original_image.max() - original_image.min()))
    mse_array_roi.append(mse(original_image_roi, image_recon_roi))

    
plt.imshow(original_image_roi,cmap='gray')

