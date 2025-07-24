# 🏅 Sport Image Classifier

A web app built with **Streamlit** and **TensorFlow (Keras)** that allows users to upload an image of a sports scene and get an instant prediction of the sport category!

<div align="center">
  <img src="https://img.shields.io/badge/Streamlit-%23FF4B4B.svg?&style=for-the-badge&logo=streamlit&logoColor=white"/>
  <img src="https://img.shields.io/badge/TensorFlow-FC7308?style=for-the-badge&logo=tensorflow&logoColor=white"/>
  <img src="https://img.shields.io/badge/PIL-Python%20Imaging%20Library-blue?style=for-the-badge"/>
</div>

---


## 📌 Features

- 📤 Upload images in JPG/PNG format
- 🧠 Predicts the **type of sport** in the image
- 📊 Displays prediction confidence
- 📈 Shows a bar chart of all class probabilities
- ✅ Clean and interactive UI with emojis and expander sections

---

## 🧠 Model Details

- Base model: `Xception` (transfer learning)  Accuracy: %98
- Input size: `(224, 224)`
- Trained on a labeled dataset of sports images
- Model saved as: `model_xception.h5`
- Label mappings saved in: `labels.json`

---

## 🖼️ Sample Sports Classes

Here are some example labels (can be edited in `labels.json`):

- Soccer
- Basketball
- Tennis
- Swimming
- Baseball
- Running

---

## 🛠️ Tech Stack

| Tool           | Description                      |
|----------------|----------------------------------|
| Streamlit      | Web App UI                       |
| TensorFlow     | Model loading & prediction       |
| PIL            | Image loading and preprocessing  |
| NumPy & JSON   | Data manipulation & labels       |

---

## 📁 Project Structure

- `app.py` — Main Streamlit app that runs the image classifier interface.
- `model_xception.h5` — Pre-trained Keras model (Xception) used for prediction.
- `labels.json` — JSON file storing the class labels (e.g., Basketball, Football, etc.).
- `requirements.txt` — List of dependencies required to run the project.
- `README.md` — Documentation and instructions for the project.

---

## 🔗 Kaggle Model Notebook

Due to GitHub file size limits, please download my pre-trained model from:

🔗 [Kaggle - Sport Image Model](https://www.kaggle.com/code/rahmamabdelfattah/xception-0-98-sports-classification)

After downloading, place `model_xception.h5` and `labels.json` in the root folder.
