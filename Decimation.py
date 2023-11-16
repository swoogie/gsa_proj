from Wav import Wav
def downsample(wav: Wav, downsample_factor: int):
    audio_signal_downsampled = wav.audio_signal[::downsample_factor]
    new_framerate = wav.framerate // downsample_factor
    sample_duration_downsampled = len(audio_signal_downsampled) / new_framerate
    return audio_signal_downsampled, new_framerate, sample_duration_downsampled
