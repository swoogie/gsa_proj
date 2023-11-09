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
            max_min = (chunk.max(), chunk.min())
            max_min_signal.append(max_min)

    return np.array(max_min_signal)


def plot_signal(signal):
    plt.figure(figsize=(12, 4))
    plt.plot(signal)
    plt.title('Averaged Chunked Signal')
    plt.xlabel('Chunk number')
    plt.ylabel('Average amplitude')
    plt.show()


def plot_max_min_signal_time_axis(max_min_signal, chunk_size, framerate):
    timer = Timer()
    
    chunk_duration = chunk_size / framerate
    time_axis = np.arange(len(max_min_signal)) * chunk_duration
    max_values = max_min_signal[:, 0]
    min_values = max_min_signal[:, 1]

    timer.start()
    plt.figure(figsize=(12, 4))
    plt.fill_between(time_axis, min_values, max_values, color='skyblue')
    plt.title('Chunked Signal Range over Time')
    plt.xlabel('Time (seconds)')
    plt.ylabel('Amplitude')
    timer.stop()
    plt.show()


wav_filename = Utils.select_file()
chunk_size = 10  # chunk_size = 44100 average every second at 44100Hz sample rate

params, audio_signal, framerate = load_wav(wav_filename)

min_max_signal = chunk_and_get_max_min(audio_signal, chunk_size)

# plot_signal(audio_signal)

timer = Timer()
timer.start()
plot_signal(audio_signal)
timer.stop()

plot_max_min_signal_time_axis(min_max_signal, chunk_size, framerate)