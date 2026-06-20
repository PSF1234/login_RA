import os
import requests
import pickle


import requests
import pickle

MODEL_URL = "https://drive.google.com/uc?export=download&id=1010GY63W3yCfQyuY8bKnpWjGnm8iNnO9"
MODEL_PATH = "ml_model.pkl"

def download_model():
    if not os.path.exists(MODEL_PATH):
        print("Downloading model...")
        r = requests.get(MODEL_URL, stream=True)
        r.raise_for_status()

        with open(MODEL_PATH, "wb") as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)

    with open(MODEL_PATH, "rb") as f:
        return pickle.load(f)"
MODEL_PATH = "ml_model.pkl"

def download_model():
    if not os.path.exists(MODEL_PATH):
        print("Downloading model...")
        r = requests.get(MODEL_URL, stream=True)
        r.raise_for_status()

        with open(MODEL_PATH, "wb") as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)

    with open(MODEL_PATH, "rb") as f:
        return pickle.load(f)