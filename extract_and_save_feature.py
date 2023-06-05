import os
from utils import open_and_get_params, get_ave_energy, get_spectral_centroid, get_pitch, get_spectral_centroid_2
import librosa
import numpy as np
import pandas as pd
root = './datawav'
E = np.array([])
S = np.array([])
P = np.array([])
L = np.array([])
for i in os.listdir(root):
    data, num_frames, framerate = open_and_get_params(root+'/'+i)
    data_audio, sample = librosa.load(root+'/'+i)
    energy = get_ave_energy(data, num_frames)
    # spectral_centroid = get_spectral_centroid(data, framerate)
    # spectral_centroid = librosa.feature.spectral_centroid(y = data_audio, sr = sample)
    spectral_centroid = get_spectral_centroid_2(data, framerate)
    pitch = get_pitch(data_audio, sample)
    label = i[:-5]
    E = np.append(E, energy)
    S = np.append(S, spectral_centroid)
    P = np.append(P, pitch)
    L = np.append(L, label)
data_excel = {
    'label': L,
    'Spectral Centroid': S,
    'Energy': E,
    'Pitch': P
}
df = pd.DataFrame(data_excel)
df.to_excel('output.xlsx', index=False)