import wave
import numpy as np
class Wav:
    def __init__(self, filename):
        with wave.open(filename, 'r') as wav_file:
            self.filename = filename
            self.n_channels, self.sampwith, self.framerate, self.n_frames, self.comptype, self.compname = wav_file.getparams()
            audio_frames = wav_file.readframes(self.n_frames)
            self.audio_signal = np.frombuffer(audio_frames, dtype=np.int16)
            if self.n_channels == 2:
                self.audio_signal = self.to_mono(self.audio_signal, self.n_frames, self.n_channels)

            self.sample_duration = len(self.audio_signal) / self.framerate
            print(self.n_channels)
    
    def to_mono(self, audio_signal, num_frames, num_channels):
        audio_data = np.frombuffer(audio_signal, dtype=np.int16)
        audio_data = np.reshape(audio_data, (num_frames, num_channels))
        mono_audio_signal = audio_data.mean(axis=1, dtype=np.int16)
        return mono_audio_signal

    def extend(self, num_repeats):
        if num_repeats <= 0:
            raise ValueError("Number of repeats should be greater than 0")

        extended_signal = np.tile(self.audio_signal, num_repeats)

        self.audio_signal = extended_signal
        self.n_frames = len(extended_signal)
        self.sample_duration = len(extended_signal) / self.framerate