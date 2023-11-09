import matplotlib.pyplot as plt
import numpy as np
from scipy.io import wavfile
import os
from Wav import Wav


def select_file():
    sound_dir = os.getcwd() + "/wavs"

    wav_files = [file for file in os.listdir(
        sound_dir) if file.endswith(".wav")]

    if not wav_files:
        print("No .wav files found in wavs/.")
    else:
        print("Select a .wav file to use:")

        for i, wav_file in enumerate(wav_files):
            print(f"{i + 1}. {wav_file}")
        while True:
            try:
                selection = (
                    int(input("Enter the number of the .wav file you want to use: ")) - 1)
                if 0 <= selection < len(wav_files):
                    selected_wav_file = wav_files[selection]
                    return "wavs/" + selected_wav_file

                else:
                    print("Invalid selection.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
