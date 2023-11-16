import numpy as np

def linear_interpolation(data, original_sample_rate, factor):
    indices = np.arange(0, len(data))
    new_indices = np.arange(0, len(data), factor)

    interpolated_data = np.interp(new_indices, indices, data)

    new_sample_rate = int(original_sample_rate / factor)
    new_duration = len(interpolated_data) / new_sample_rate

    return interpolated_data, new_sample_rate, new_duration