from fastapi import FastAPI, UploadFile, File
import uvicorn
import numpy as np
import cv2
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, BatchNormalization, GlobalAveragePooling2D
from tensorflow.keras.applications import EfficientNetB0
from tensorflow.keras.applications.efficientnet import preprocess_input

app = FastAPI()

en = EfficientNetB0(include_top=False, input_shape=(224,224,3), weights="imagenet")
en.trainable = False

model = Sequential([
    en,
    GlobalAveragePooling2D(),
    BatchNormalization(),
    Dropout(0.3),
    Dense(16, activation='relu'),
    Dropout(0.2),
    Dense(2, activation='softmax')
])
model.load_weights("cycle_vs_bike_weights.h5")

class_names = ["cycle", "bike"]

@app.post('/predict')
async def predict(file: UploadFile=File(...)):
    contents = await file.read()
    
    nparr = np.frombuffer(contents, np.uint8) #convert bytes to numpy array
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img, (224,224))
    img = np.expand_dims(img, axis=0).astype('float32')
    img = preprocess_input(img)

    preds = model.predict(img)
    confidence = float(np.max(preds))
    
    if confidence < 0.8:
        return {"prediction": "I only recognize cycles and bikes… try again!", "confidence": confidence}

    predicted_class = class_names[int(np.argmax(preds))]
    return {"prediction": predicted_class, "confidence": confidence}