import numpy as np
import matplotlib.pyplot as plt
# from scipy.io import wavfile
import librosa
import wave
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
# mở file bằng wave audio
def open_and_get_params(audio_file):
    with wave.open(audio_file, 'rb') as wavfile:   
        params = wavfile.getparams()
        num_channels = params[0]
        sample_width = params[1]
        framerate = params[2]
        num_frames = params[3]
        data = wavfile.readframes(num_frames)
        sample_rate = wavfile.getframerate()

        # Chuyển đổi dữ liệu âm thanh thành mảng numpy
        if sample_width == 2:
            data = np.frombuffer(data, dtype=np.int16)
        elif sample_width == 4:
            data = np.frombuffer(data, dtype=np.int32)
        return data, num_frames, sample_rate
    
# hàm tính năng lượng trung bình
def get_ave_energy(data, num_frames):
    # energy = power / số khung trong 1 file audio
    # power = data^2
    energy = np.sum(data**2)/num_frames
    return energy

# hàm tính spectral cetroid
def get_spectral_centroid(audio_data, sample_rate):
    audio_spectrum = np.fft.fft(audio_data)
    # Tính toán trục tần số
    freq_axis = np.fft.fftfreq(len(audio_data), 1/sample_rate)
    # tính spectral centroid theo cthuc
    arr=[]
    mag = np.abs(audio_spectrum)
    for i in range(len(freq_axis)):
        a = freq_axis[i]*mag[i]
        arr = np.append(arr, a)
    spectral_centroid = np.sum(arr) / np.sum(mag)
    return spectral_centroid
# cách 2
def get_spectral_centroid_2(audio_data, sample):
    spectrum = abs(np.fft.rfft(audio_data))
    normalized_spectrum = spectrum / sum(spectrum)  # like a probability mass function
    normalized_frequencies = np.linspace(0, 1, len(spectrum))
    spectral_centroid = sum(normalized_frequencies * normalized_spectrum)/sum(normalized_spectrum)
    return spectral_centroid
# hàm tính pitch dựa trên mối tương quan của tần số (cao độ)
def get_pitch(data, sample_rate):
    fft = np.fft.fft(data)
    freqs = np.fft.fftfreq(len(data), 1/sample_rate)
    positive_freq_mask = freqs > 0 
    freq_axis_positive = freqs[positive_freq_mask]
    fft_pos = fft[positive_freq_mask]
    mag = np.abs(fft_pos)
    highest_freq = freq_axis_positive[np.argmax(mag)]
    return highest_freq
def read_excel(file):
    X = np.empty((0, 3))
    # Read the Excel file into a DataFrame
    df = pd.read_excel(file)
    df['label'] = df['label'].astype(str)
    Y = df['label'].values
    for index, row in df.iterrows():
        x = np.array([])
        x = np.append(x, row['Spectral Centroid'])
        x = np.append(x, row['Energy'])
        x = np.append(x, row['Pitch'])
        X = np.concatenate((X, [x]), axis=0)
    return X, Y
def predict(X, Y, input):
    k = 1 # Number of neighbors
    knn = KNeighborsClassifier(n_neighbors=k)

    # Fit the classifier to the training data
    knn.fit(X, Y)

    # Predict the labels for the test set
    y_pred = knn.predict(input)
    distances, indices = knn.kneighbors(input)
    # Evaluate the accuracy of the classifier
    # accuracy = accuracy_score(y_test, y_pred)
    # print("Accuracy:", accuracy)
    return y_pred, distances