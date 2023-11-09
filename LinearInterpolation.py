import numpy as np

def downsample_linear_wav(wav_object, factor):
    if factor <= 1 or not isinstance(factor, int):
        raise ValueError("Downsampling factor must be a positive integer.")

    new_length = len(wav_object.audio_signal) // factor

    downsampled_signal = np.zeros(new_length)

    for i in range(new_length):
        start_idx = i * factor
        end_idx = min((i + 1) * factor, len(wav_object.audio_signal))

        alpha = i * factor - start_idx

        if end_idx >= len(wav_object.audio_signal):
            end_idx = len(wav_object.audio_signal) - 1

        downsampled_signal[i] = (1 - alpha) * wav_object.audio_signal[start_idx] + alpha * wav_object.audio_signal[end_idx]

    new_framerate = wav_object.framerate // factor
    sample_duration_downsampled = len(downsampled_signal) / new_framerate

    return downsampled_signal, new_framerate, sample_duration_downsampled