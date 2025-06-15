# 🧠 Talking Hands – Real-Time Sign Language Detection ✋🤟

Welcome to **Talking Hands**, a real-time sign language detection system built to interpret American Sign Language (ASL) gestures using computer vision and deep learning.

## 🚀 Project Overview

Talking Hands uses webcam video to detect hand gestures and classify them into ASL numbers (0–9). The goal is to bridge communication gaps and make gesture-based interactions more accessible using AI.

## 🎯 Key Features

- 🔎 Real-time hand gesture recognition
- 🤖 CNN-based model trained on ASL digit images
- 🧠 MediaPipe & OpenCV for hand tracking and image preprocessing
- 💻 Webcam-based live predictions
- 📊 Visual output with gesture overlay and predicted digit

## 🛠️ Tech Stack

| Tool/Library   | Purpose                           |
|----------------|-----------------------------------|
| Python         | Main programming language         |
| OpenCV         | Video capture and preprocessing   |
| MediaPipe      | Hand tracking and landmarks       |
| TensorFlow/Keras | Model training and inference    |
| NumPy/Pandas   | Data handling and manipulation    |
| Matplotlib     | Model evaluation and visualization|

## 🖼️ Model Architecture

- Convolutional Neural Network (CNN) trained on ASL digit dataset (0–9)
- Input: Processed hand images from webcam
- Output: Digit class (0–9)

## 📁 Project Structure

```
Talking-Hands/
├── data/                  # ASL digit dataset
├── model/                 # Trained model files
├── src/                   # Python source code
│   ├── hand_tracker.py
│   ├── predict.py
│   └── train_model.py
├── test_images/           # Sample test images
├── README.md              # This file
└── requirements.txt       # Python dependencies
```

## 🧪 How to Run

1. **Clone the repo**
   ```bash
   git clone https://github.com/gurpreetgitsingh13/Sign-Language-Detection---Talking-Hands.git
   cd Sign-Language-Detection---Talking-Hands
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the detection script**
   ```bash
   python src/predict.py
   ```

4. **Make hand gestures (0–9) in front of your webcam and see predictions in real-time!**

## 📈 Future Improvements

- 🔤 Support for full ASL alphabet
- 🌐 Web interface using Flask or React
- 📱 Mobile deployment (Android/iOS)
- 🗣️ Gesture-to-speech integration

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

## 📄 License

MIT License © Gurpreet Singh

## 🙌 Acknowledgements

- [ASL Dataset](https://www.kaggle.com/datasets/datamunge/sign-language-mnist)
- [MediaPipe by Google](https://mediapipe.dev/)
- TensorFlow + Keras community

---

> _“Code is poetry. Data is the voice of reality.”_
