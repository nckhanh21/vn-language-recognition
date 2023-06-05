import os
from utils import open_and_get_params, get_ave_energy, get_pitch, get_spectral_centroid_2, read_excel, predict
import librosa
import numpy as np
import pandas as pd
root = 'outdb/hoang.wav'
data, num_frames, framerate = open_and_get_params(root)
data_audio, sample = librosa.load(root)
energy = get_ave_energy(data, num_frames)
# spectral_centroid = get_spectral_centroid(data, framerate)
spectral_centroid = librosa.feature.spectral_centroid(y = data_audio, sr = sample)
spectral_centroid = get_spectral_centroid_2(data, framerate)
pitch = get_pitch(data_audio, sample)
x = np.array([])
x = np.append(x, spectral_centroid)
x = np.append(x, energy)
x = np.append(x, pitch)
x = x.reshape(1, -1)
X, Y = read_excel('output.xlsx')
y_pred, dis = predict(X, Y, x)
print(dis)
if dis>40:
    y_pred = 'unknown'
print(y_pred)