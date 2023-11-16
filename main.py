import numpy as np
import matplotlib.pyplot as plt
import Utils
from Timer import Timer
from Wav import Wav
import PolynomialInterpolation
import LinearInterpolation


def downsample_wav(wav: Wav, downsample_factor: int):
    audio_signal_downsampled = wav.audio_signal[::downsample_factor]
    new_framerate = wav.framerate // downsample_factor
    sample_duration_downsampled = len(audio_signal_downsampled) / new_framerate
    return audio_signal_downsampled, new_framerate, sample_duration_downsampled


def plot_signal(audio_signal, sample_duration, title):
    time_axis = np.linspace(0, sample_duration, len(audio_signal))

    plt.figure(figsize=(12, 6))
    plt.title(title)
    timer = Timer()
    timer.start()
    plt.plot(time_axis, audio_signal)
    timer.stop()
    plt.xlabel('time (s)')
    plt.ylabel('Amplitude')
    plt.grid(True)
    plt.show()

# When doing analysis of multiple files, downsampling types etc. I would comment all inputs out and hardcode values 
if __name__ == "__main__":
    wav_filename = Utils.select_file()
    wav = Wav(wav_filename)
    num_repeats = int(input("extend file by playing how many times?: "))
    wav.extend(num_repeats)

    downsample_types = [
        "Decimation",
        "Linear Interpolation",
        "Polynomial Interpolation"
    ]

    ds_choice = None
    while not (ds_choice):
        for index, downsample_type in enumerate(downsample_types):
            print(f"{index+1}. {downsample_type}")
        print("Choose which downsampling algorithm to use:")
        ds_choice = downsample_types[int(input()) - 1]
    
    downsample_factor = None
    while (downsample_factor < 0):
       downsample_factor = int(input("Enter downsample factor f>0: ")) 

    if (ds_choice == downsample_types[0]):
        audio_signal_downsampled, new_framerate, sample_duration_downsampled = downsample_wav(
        wav, downsample_factor)
    if (ds_choice == downsample_types[1]):
        audio_signal_downsampled, new_framerate, sample_duration_downsampled = LinearInterpolation.linear_interpolation(wav.audio_signal, wav.framerate, downsample_factor)
    # TODO: Fix
    if (ds_choice == downsample_types[2]):
        audio_signal_downsampled, new_framerate, sample_duration_downsampled = PolynomialInterpolation.downsample_poly_wav(
        wav, downsample_factor)

    Utils.print_params(wav)
    plot_signal(wav.audio_signal, wav.sample_duration, f'{wav.filename} original')
    plot_signal(audio_signal_downsampled, sample_duration_downsampled, f'{wav.filename} {ds_choice} f={downsample_factor}')
