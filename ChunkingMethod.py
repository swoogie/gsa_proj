import numpy as np
import wave
import matplotlib.pyplot as plt
import Utils
from Timer import Timer


def load_wav(filename):
    with wave.open(filename, 'r') as wav_file:
        params = wav_file.getparams()
        n_channels, _, framerate, n_frames, _, _ = wav_file.getparams()
        audio_frames = wav_file.readframes(n_frames)
        audio_signal = np.frombuffer(audio_frames, dtype=np.int16)
        if n_channels == 2:
            audio_signal = audio_signal.reshape((-1, 2)).mean(axis=1)
        return params, audio_signal, framerate


def chunk_and_get_max_min(signal, chunk_size):
    num_chunks = len(signal) // chunk_size + (1 if len(signal) % chunk_size else 0)
    max_min_signal = []

    for i in range(num_chunks):
        start = i * chunk_size
        end = start + chunk_size
        chunk = np.array(signal[start:end])
        if len(chunk) > 0:
            max_min_signal.append(chunk.max())
            max_min_signal.append(chunk.min())

    return np.array(max_min_signal)


def plot_signal(signal):
    plt.figure(figsize=(12, 6))
    plt.subplot(2, 1, 1)
    plt.plot(signal)
    plt.title('Averaged Chunked Signal')
    plt.xlabel('Chunk number')
    plt.ylabel('Average amplitude')
    plt.grid(True)
    plt.show()


def plot_max_min_signal_time_axis(max_min_signal, sample_duration, audio_signal, title):
    timer = Timer()
    
    time_axis = np.linspace(0, sample_duration, len(audio_signal))
    new_time_axis = np.linspace(0, sample_duration, len(max_min_signal))
    print(len(audio_signal))
    print(len(max_min_signal))

    plt.figure(figsize=(15, 4))
    plt.plot(time_axis, audio_signal, color='r', alpha=0.5)
    timer.start()
    plt.plot(new_time_axis, max_min_signal)
    timer.stop()
    plt.title(title)
    plt.xlabel('time (s)')
    plt.ylabel('Amplitude')
    plt.grid(True)
    plt.show()