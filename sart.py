#!/usr/bin/env python3
"""
Python implementation of SART
"""
import matplotlib.pyplot as plt
import numpy as np
from scipy import sparse


def sart(operator, data, model_init, max_iter=1000, omega=1.0, image_dims=(256,256), plot_convergence=None):
    """
    Given a forward operator, some data (e.g. a sinogram), and an initial guess, use the SART algorithm to
    reconstruct the noisy image.

    :param operator: scipy.sparse.csr, [len(model_init), len(data)]
        A sparse CSR matrix representation of the imaging operator.
    :param data: np.array
        The measured data (e.g. sinogram) as a vector. If the data is input as a matrix, it will be flattened into a
        Fortran-optimized vector.
    :param model_init: np.array
        Initial guess of the image as a vector.
    :param max_iter: int
        Maximum number of SART iterations.
    :param omega: int
        Omega hyperparameter for update steps.
    :param image_dims: (int, int)
        Pixel dimensions for the reconstructed image.
    :param plot_convergence: str or None
        If not None, plot the residual for each iteration and save the result to the file indicated by plot_convergence.

    :return model: np.array
        Matrix representation of the reconstructed image
    :return residual_norms: np.array
        L2-norm of the model residual at each iteration
    :return fig: matplotlib.Figure
        Handle to a figure with a plot showing the residual for every iteration
    """
    model = model_init
    # Convert the data from a matrix to a vector if necessary
    if len(data.shape) == 2:
        data = data.flatten(order="F")

    residual = data
    residual_norms = np.zeros(max_iter)

    # Precompute X, the constant term for SART
    # V is a sparse diagonal matrix corresponding to one over the row-sum of the operator
    V = sparse.spdiags((1 / operator.sum(axis=0)), 0, len(model), len(model))
    # W is a sparse diagonal matrix corresponding to one over the column-sum of the operator
    W = sparse.spdiags((1 / operator.sum(axis=1)).T, 0, len(data), len(data))
    X = omega * V * operator.T * W

    # Reconstruct the image
    for i in range(max_iter):
        model = model + X * residual
        residual = data - operator * model
        residual_norms[i] = np.linalg.norm(residual)

        # Report iteration history for logging
        if (i + 1) % 50 == 0:
            print(f"Completed {i+1} iterations.")

    # Convert the final image to a matrix
    model = model.reshape(image_dims, order="F")

    # Plot convergence history
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.plot(np.arange(max_iter) + 1, residual_norms)
    ax.set_xlabel("Iteration")
    ax.set_ylabel("Norm of residual")

    if plot_convergence:
        # Append a PNG if no file type is specific
        filetypes = {"png", "eps", "svg", "pdf"}
        if len(plot_convergence.split(".")) == 1 or plot_convergence.split(".")[-1].lower() not in filetypes:
            plot_convergence += ".png"

        fig.savefig(plot_convergence)

    return model, residual_norms, fig
