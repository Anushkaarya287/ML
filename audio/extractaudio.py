import librosa
import numpy as np
import pandas as pd
import os


audio_folder = "."

data_list = []


for filename in os.listdir(audio_folder):
    if filename.endswith(".mp3") or filename.endswith(".wav"):
        file_path = os.path.join(audio_folder, filename)

        
        y, sr = librosa.load(file_path)

        
        duration = librosa.get_duration(y=y, sr=sr)
        rms = np.mean(librosa.feature.rms(y=y))
        zcr = np.mean(librosa.feature.zero_crossing_rate(y))
        spectral_centroid = np.mean(librosa.feature.spectral_centroid(y=y, sr=sr))

        
        data_list.append({
            "File": filename,
            "Duration (sec)": round(duration, 2),
            "RMS Energy": float(rms),
            "Zero Crossing Rate": float(zcr),
            "Spectral Centroid": float(spectral_centroid)
        })


df = pd.DataFrame(data_list)

print(df)


df.to_csv("audio_data.csv", index=False)
print("\nExtracted audio features saved to audio_data.csv")