import pickle
import os

model_path = r"C:\Users\chotu s\Desktop\deoloy ml project\trained_model.sav"

if os.path.exists(model_path):
    try:
        with open(model_path, "rb") as file:
            loaded_model = pickle.load(file)
        print("Model loaded successfully!")
    except Exception as e:
        print(f"Error loading model: {e}")
else:
    print(f"Error: Model file not found at {model_path}")


