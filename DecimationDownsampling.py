import numpy as np
import wave
import matplotlib.pyplot as plt
import Utils
from Timer import Timer
from Wav import Wav
import PolynomialInterpolation
import LinearInterpolation



def lowpass_filter(audio_signal, cutoff_freq, framerate):
    filter_length = int(2 * framerate / cutoff_freq)
    filter_coeff = np.ones(filter_length) / filter_length

    filtered_signal = np.convolve(audio_signal, filter_coeff, mode='same')

    return filtered_signal


def downsample_wav(wav: Wav, downsample_factor: int):
    audio_signal_downsampled = wav.audio_signal[::downsample_factor]
    new_framerate = wav.framerate // downsample_factor
    sample_duration_downsampled = len(audio_signal_downsampled) / new_framerate
    return audio_signal_downsampled, new_framerate, sample_duration_downsampled


def plot_signal(audio_signal, sample_duration):
    time_axis = np.linspace(0, sample_duration, len(audio_signal))

    plt.figure(figsize=(12, 6))
    plt.subplot(2, 1, 1)
    plt.title('Waveform')
    timer = Timer()
    timer.start()
    plt.plot(time_axis, audio_signal)
    timer.stop()
    plt.xlabel('time (s)')
    plt.ylabel('Amplitude')
    plt.grid(True)
    plt.show()


wav_filename = Utils.select_file()
wav = Wav(wav_filename)
num_repeats = int(input("repeat file how many times?: "))
wav.extend(num_repeats)

downsample_type = None
while (downsample_type not in range(1, 4)):
    downsample_type = int(input("1. Decimation\n2. Linear Interpolation\n3. Polynomial Interpolation\nchoose which downsampling algorithm to use:"))

downsample_factor = 2

if (downsample_type == 1):
    audio_signal_downsampled, new_framerate, sample_duration_downsampled = downsample_wav(
    wav, downsample_factor)
if (downsample_type == 2):
    audio_signal_downsampled, new_framerate, sample_duration_downsampled = LinearInterpolation.downsample_linear_wav(
    wav, downsample_factor)
if (downsample_type == 3):
    audio_signal_downsampled, new_framerate, sample_duration_downsampled = PolynomialInterpolation.downsample_poly_wav(
    wav, downsample_factor)

use_filter = None
while (use_filter != 'y' and use_filter != 'n'):
    use_filter = input("use lowpass filter? (wip) y/n: ").lower()
if (use_filter == 'y'):
    cutoff_frequency = 0.2
    audio_signal_downsampled = lowpass_filter(
        audio_signal_downsampled, cutoff_frequency, new_framerate)

plot_signal(wav.audio_signal, wav.sample_duration)
plot_signal(audio_signal_downsampled, sample_duration_downsampled)
