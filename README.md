
# 🚴‍♂️ Cycle vs Bike Classification

*A Deep Learning Project using EfficientNetB0 & Transfer Learning*

## 📌 Project Overview

This project demonstrates how to apply **Transfer Learning** for an image classification task.
The goal is to build a model that can distinguish between **cycles (bicycles)** and **bikes (motorcycles)** using the **EfficientNetB0** architecture.

The project was created as a hands-on exercise to understand:

* 🔹 Transfer learning workflow
* 🔹 Fine-tuning pre-trained models
* 🔹 Building an end-to-end image classification pipeline

---

## ⚙️ Tech Stack

* **Python 3.10+**
* **TensorFlow / Keras**
* **EfficientNetB0 (pre-trained on ImageNet)**
* **Streamlit** for deployment (web app interface)
* **FastAPI + Uvicorn** for backend API

---


### 🚀 Installation
1️⃣ Clone the Repository
```
  git clone https://github.com/hetbhalani/Cycle_vs_Bike
  cd Cycle_vs_Bike
```

2️⃣ Create Virtual Environment
```
# Linux / Mac
python3 -m venv .venv
source .venv/bin/activate


# Windows (PowerShell)
python -m venv .venv
.venv\Scripts\activate
```

3️⃣ Install Requirements
```
pip install --upgrade pip
pip install -r requirements.txt
```

▶️ Running the Project
Run FastAPI Backend (for API)
```
uvicorn app.main:app --reload
```

App will be available at: http://127.0.0.1:8000

Docs (Swagger UI): http://127.0.0.1:8000/docs

▶️Run Streamlit App (UI)
```
streamlit run app/streamlit_app.py
```

UI will open in your browser at: http://localhost:8501

---
## 📂 Project Structure

```
cycle-vs-bike-classification/
│── dataset/                # Training & validation images                 
│── main.py                 # FastAPI app
│── streamlit_app.py        # Streamlit UI
│── cycle_vs_bike.h5        # Trained model
│── requirements.txt        # Dependencies
│── runtime.txt             # Python version for deployment
│── Procfile                # Render/Heroku deployment config
│── README.md               # Project documentation
```

---

## 🧠 Model Training

* **Base model**: EfficientNetB0 (ImageNet weights)
* **Custom head**:

  * GlobalAveragePooling
  * Dense (ReLU)
  * Dropout layers for regularization
  * Dense (Softmax) → 2 classes (cycle, bike)
* **Optimizer**: Adam
* **Loss**: SparseCategoricalCrossentropy
* **Metrics**: Accuracy

---

## 📊 Results

* Training Accuracy: \~98%
* Validation Accuracy: \~99%
* The model generalizes well on unseen data.

---

## 🔮 Future Improvements

* Add a third class: “Other” (to handle unrelated images like bananas 🍌)
* Improve dataset size & diversity
* Experiment with different EfficientNet variants (B3, B7, etc.)
* Deploy on Hugging Face Spaces for quick demo

---

## 🤝 Contributing

This project was made for **learning purposes**. Suggestions and contributions are always welcome!

---
Made With ❤️ by Het Bhalani 👽