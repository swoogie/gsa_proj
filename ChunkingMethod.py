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


def chunk_and_average(signal, chunk_size):
    chunks = np.array_split(signal, np.arange(
        chunk_size, len(signal), chunk_size))
    averaged_signal = np.array([chunk.mean() for chunk in chunks])
    return averaged_signal


def plot_signal(signal):
    plt.figure(figsize=(12, 4))
    plt.plot(signal)
    plt.title('Averaged Chunked Signal')
    plt.xlabel('Chunk number')
    plt.ylabel('Average amplitude')
    plt.show()


def plot_averaged_signal_time_axis(averaged_signal, chunk_size, framerate):
    timer = Timer()
    chunk_duration = chunk_size / framerate
    time_axis = np.arange(len(averaged_signal)) * chunk_duration

    timer.start()
    plt.figure(figsize=(12, 4))
    plt.plot(time_axis, averaged_signal)
    plt.title('Averaged Chunked Signal over Time')
    plt.xlabel('Time (seconds)')
    plt.ylabel('Average amplitude')
    plt.show()
    timer.stop()


def save_to_wav(params: wave._wave_params, signal: np.ndarray[16], filename):
    with wave.open(filename, 'w') as wav_file:
        n_channels = params.nchannels  # Mono
        sampwidth = params.sampwidth  # Sample width in bytes
        n_frames = len(signal)
        comp_type = params.comptype
        comp_name = params.compname
        framerate = params.framerate

        wav_file.setparams((n_channels, sampwidth, framerate,
                           n_frames, comp_type, comp_name))

        wav_file.writeframes(signal.astype(np.int16).tobytes())


wav_filename = Utils.select_file()
chunk_size = 10  # chunk_size = 44100 average every second at 44100Hz sample rate

params, audio_signal, framerate = load_wav(wav_filename)

averaged_signal = chunk_and_average(audio_signal, chunk_size)

# plot_signal(audio_signal)

timer = Timer()
timer.start()
plot_signal(averaged_signal)
timer.stop()

plot_averaged_signal_time_axis(averaged_signal, chunk_size, framerate)

save_to_wav(params, averaged_signal,
            "./shortened_wavs/")
