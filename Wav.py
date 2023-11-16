import wave
import matplotlib.pyplot as plt
import numpy as np
from Timer import Timer

class Wav:
    def __init__(self, filename):
        with wave.open(filename, 'r') as wav_file:
            self.filename = filename
            self.n_channels, self.sampwith, self.framerate, self.n_frames, self.comptype, self.compname = wav_file.getparams()
            audio_frames = wav_file.readframes(self.n_frames)
            self.audio_signal = np.frombuffer(audio_frames, dtype=np.int16)
            if self.n_channels > 1:
                self.audio_signal = self.audio_signal[::self.n_channels]

            self.sample_duration = len(self.audio_signal) / self.framerate
            
        self.new_audio_signal, self.new_framerate, self.new_sample_duration = self.audio_signal, self.framerate, self.sample_duration
    
    def to_mono(self, audio_signal, num_channels):
        mono_audio_signal = np.mean(audio_signal.reshape(-1, num_channels), axis=1, dtype=np.int16)
        return mono_audio_signal

    def extend(self, num_repeats):
        if num_repeats <= 0:
            raise ValueError("Number of repeats should be greater than 0")

        extended_signal = np.tile(self.audio_signal, num_repeats)

        self.audio_signal = extended_signal
        self.n_frames = len(extended_signal)
        self.sample_duration = len(extended_signal) / self.framerate
        self.new_audio_signal = self.audio_signal
        self.new_sample_duration = self.sample_duration

    def plot(self, title):
        time_axis = np.linspace(0, self.sample_duration, len(self.audio_signal))
        new_time_axis = np.linspace(0, self.new_sample_duration, len(self.new_audio_signal))

        plt.figure(figsize=(15, 4))
        plt.title(title)
        timer = Timer()
        timer.start()
        plt.plot(time_axis, self.audio_signal, color='r', alpha=0.5)
        timer.stop()
        timer.start()
        plt.plot(new_time_axis, self.new_audio_signal)
        timer.stop()
        plt.xlabel('time (s)')
        plt.ylabel('Amplitude')
        plt.grid(True)
        plt.show()
    