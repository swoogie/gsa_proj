import numpy as np

def downsample_poly_wav(wav_object, factor, degree=3):
    if factor <= 1 or not isinstance(factor, int):
        raise ValueError("Downsampling factor must be a positive integer.")

    x = np.arange(0, len(wav_object.audio_signal))
    new_x = np.arange(0, len(wav_object.audio_signal), factor)

    coeffs = np.polyfit(x, wav_object.audio_signal, deg=degree)
    
    downsampled_signal = np.polyval(coeffs, new_x)

    new_framerate = wav_object.framerate // factor
    sample_duration_downsampled = len(downsampled_signal) / new_framerate

    return downsampled_signal, new_framerate, sample_duration_downsampled
