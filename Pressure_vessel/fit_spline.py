# fit_spline.py

import pandas as pd
import numpy as np
from scipy.interpolate import UnivariateSpline
import matplotlib.pyplot as plt

def df_to_spline(df: pd.DataFrame, x_column: str, y_column: str, smoothing_factor: float = 1.0):
    """
    Fit a spline through a specific column of a DataFrame and plot the result.

    Parameters:
    - df (pd.DataFrame): Input dataframe
    - x_column (str): Name of the column to use as the x-axis
    - y_column (str): Name of the column to fit the spline to
    - smoothing_factor (float): Smoothing factor for the spline. Default is 1.0.
    """
    # Fit a spline to the y column
    spline = UnivariateSpline(df[x_column], df[y_column], s=smoothing_factor)

    # Evaluate the spline over the x values to get smoothed y values
    y_spline = spline(df[x_column])

    # Plot the original data and the spline
    plt.scatter(df[x_column], df[y_column], color='blue', s=5, label='Original Data')
    plt.plot(df[x_column], y_spline, color='red', label='Spline')
    plt.xlabel(x_column)
    plt.ylabel(y_column)
    plt.legend()
    plt.show()
    return spline


