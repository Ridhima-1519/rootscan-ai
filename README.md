# 🌱 RootScan AI – Plant Disease Detection System

RootScan AI is an AI-powered plant disease detection system that identifies diseases from leaf images using Deep Learning and Computer Vision. The project is built using Python, TensorFlow/Keras, OpenCV, and Flutter integration for mobile deployment.

The goal of this project is to help farmers and users quickly diagnose plant diseases using a camera or uploaded image and receive instant results offline.

---

# 🚀 Features

* Detects diseases from plant leaf images
* Supports Potato and Tomato leaf diseases
* Deep Learning CNN-based classification
* Real-time prediction
* Disease confidence score
* Treatment suggestions
* Offline mobile app support using TensorFlow Lite
* Cross-platform Flutter application

---

# 🧠 Diseases Supported

## Potato

* Early Blight
* Late Blight
* Healthy

## Tomato

* Early Blight
* Late Blight
* Healthy

---

# 🛠️ Technologies Used

* Python
* TensorFlow / Keras
* OpenCV
* NumPy
* Flutter
* TensorFlow Lite (TFLite)

---

# 📂 Dataset

Dataset used:
PlantVillage Dataset

Dataset Structure:

```text
ImageDataset/
│
├── train/
│   ├── potato_early
│   ├── potato_healthy
│   ├── potato_late
│   ├── tomato_early
│   ├── tomato_healthy
│   └── tomato_late
│
└── valid/
    ├── potato_early
    ├── potato_healthy
    ├── potato_late
    ├── tomato_early
    ├── tomato_healthy
    └── tomato_late
```

---

# ⚙️ Model Architecture

The project uses a Convolutional Neural Network (CNN) consisting of:

* Conv2D Layers
* MaxPooling Layers
* Flatten Layer
* Dense Layers
* Softmax Output Layer

Image size used:

```text
128 x 128
```

---

# ▶️ How to Run

## 1️⃣ Install Dependencies

```bash
pip install tensorflow opencv-python numpy matplotlib
```

---

## 2️⃣ Train Model

```bash
python train_model.py
```

This generates:

```text
plant_model.h5
```

---

## 3️⃣ Run Prediction

```bash
python predict.py
```

---

# 📱 Flutter Mobile App

The trained model is converted into TensorFlow Lite format for mobile deployment.

## Convert Model

```bash
python convert_to_tflite.py
```

Output:

```text
plant_model.tflite
```

---

# 📸 Mobile App Workflow

1. Open camera
2. Capture leaf image
3. Preprocess image
4. Run TFLite model
5. Display:

   * Disease Name
   * Confidence Score
   * Severity Percentage
   * Treatment Suggestion

---

# 📊 Sample Output

```text
Prediction: Tomato Late Blight
Confidence: 92.45%
Treatment: Avoid excess moisture and remove infected leaves.
```

---

# 🔥 Future Improvements

* More crop support
* Real-time live camera detection
* Cloud database integration
* Multi-language support
* Fertilizer recommendation system
* IoT integration with smart farming devices

---

# 👨‍💻 Author

Ridhima Panigrahi

---

# 🌟 Project Title

RootScan AI
Offline AI-Powered Plant Disease Diagnosis System
