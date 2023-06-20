# import soundfile as sf

# y, sr = sf.read('audio.wav', dtype='int16')
# print(sr)

import wave
import matplotlib.pyplot as plt
import numpy as np

# Open wav file and read frames as bytes
sf_filewave = wave.open('sagar.wav', 'r')
signal_sf = sf_filewave.readframes(-1)
# Convert audio bytes to integers
soundwave_sf = np.frombuffer(signal_sf, dtype='int16')
# Get the sound wave frame rate
framerate_sf = sf_filewave.getframerate()
# Find the sound wave timestamps
time_sf = np.linspace(start=0,
                      stop=len(soundwave_sf)/framerate_sf,
                      num=len(soundwave_sf))
# Set up plot
f, ax = plt.subplots(figsize=(15, 3))
# Setup the title and axis titles
item=max(soundwave_sf)
# for idx, val in np.ndenumerate(soundwave_sf):
#         if val == item:
#             print(idx)
print(time_sf[list(soundwave_sf).index(item)])
plt.title('Amplitude over Time')
plt.ylabel('Amplitude')
plt.xlabel('Time (seconds)')
# Add the audio data to the plot
plt.plot(time_sf, soundwave_sf, label='Warm Memories', alpha=0.5)
plt.legend()
plt.show()


# import librosa
# import matplotlib.pyplot.plot as plt
# audio = 'audio.wav'
# x, sr = librosa.load(audio)
# X = librosa.stft(x)
# Xdb = librosa.amplitude_to_db(abs(X))
# plt.figure(figsize = (10, 5))
# librosa.display.specshow(Xdb, sr = sr, x_axis = 'time', y_axis = 'hz')
# plt.colorbar()