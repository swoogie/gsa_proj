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
                audio_signal = self.to_mono(self.audio_signal)

            self.sample_duration = len(audio_signal) / self.framerate
    
    def to_mono(self, audio_signal):
        return audio_signal.reshape((-1, 2)).mean(axis=1)

    def extend(self, num_repeats):
        if num_repeats <= 0:
            raise ValueError("Number of repeats should be greater than 0")

        extended_signal = np.tile(self.audio_signal, num_repeats)

        self.audio_signal = extended_signal
        self.n_frames = len(extended_signal)
        self.sample_duration = len(extended_signal) / self.framerate