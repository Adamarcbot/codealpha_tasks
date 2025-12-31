import os
import librosa
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout
from tensorflow.keras.utils import to_categorical


DATASET_PATH = "dataset"
MAX_PAD_LEN = 174  # fixed length MFCC
EMOTIONS = os.listdir(DATASET_PATH)


def extract_mfcc(file_path):
    audio, sr = librosa.load(file_path, sr=None)
    mfcc = librosa.feature.mfcc(y=audio, sr=sr, n_mfcc=40)
    mfcc = mfcc.T

    if len(mfcc) < MAX_PAD_LEN:
        pad_width = MAX_PAD_LEN - len(mfcc)
        mfcc = np.pad(mfcc, pad_width=((0, pad_width), (0, 0)))
    else:
        mfcc = mfcc[:MAX_PAD_LEN]

    return mfcc

X, y = [], []

for emotion in EMOTIONS:
    emotion_path = os.path.join(DATASET_PATH, emotion)
    for file in os.listdir(emotion_path):
        if file.endswith(".wav"):
            file_path = os.path.join(emotion_path, file)
            mfcc = extract_mfcc(file_path)
            X.append(mfcc)
            y.append(emotion)

X = np.array(X)
y = np.array(y)

encoder = LabelEncoder()
y_encoded = encoder.fit_transform(y)
y_onehot = to_categorical(y_encoded)


X_train, X_test, y_train, y_test = train_test_split(
    X, y_onehot, test_size=0.2, random_state=42, stratify=y_onehot
)


model = Sequential([
    LSTM(128, return_sequences=True, input_shape=(X.shape[1], X.shape[2])),
    Dropout(0.3),
    LSTM(64),
    Dropout(0.3),
    Dense(len(EMOTIONS), activation="softmax")
])

model.compile(
    optimizer="adam",
    loss="categorical_crossentropy",
    metrics=["accuracy"]
)

model.fit(
    X_train,
    y_train,
    validation_data=(X_test, y_test),
    epochs=30,
    batch_size=32
)

loss, accuracy = model.evaluate(X_test, y_test)
print("Test Accuracy:", accuracy)
