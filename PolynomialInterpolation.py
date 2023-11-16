import numpy as np
from scipy.interpolate import interp1d
def downsample(data, original_sample_rate, factor):
    indices = np.arange(0, len(data))
    new_indices = np.arange(0, len(data), factor)

    f = interp1d(indices, data, kind='cubic', fill_value="extrapolate")
    interpolated_data = f(new_indices)

    new_sample_rate = int(original_sample_rate / factor)
    new_duration = len(interpolated_data) / new_sample_rate

    return interpolated_data, new_sample_rate, new_duration
