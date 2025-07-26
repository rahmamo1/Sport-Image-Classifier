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

## 📂 Dataset

The system was trained and evaluated on a comprehensive dataset of sports images comprising **100 different sports categories**.

- **Dataset Split:**
  - 🏋️ Training Set: **13,500 images**
  - 📊 Validation Set: **500 images**
  - 🧪 Test Set: **500 images**

- **Dataset Structure:**
  - Number of Classes: **100**
  - Each class contains diverse sports images for robust model generalization.

- **Dataset Source:**  
  [🔗 Dataset Link](https://www.kaggle.com/datasets/gpiosenka/sports-classification)

  ---

## 🧠 Model Details

- Base model: `Xception` (transfer learning)  Accuracy: %98
- Input size: `(224, 224)`
- Trained on a labeled dataset of sports images
- Model saved as: `model_xception.h5`
- Label mappings saved in: `labels.json`

---

## 🖼️ Sample Sports Classes

Here are some example labels (can be edited in `labels.json` it has 100 sports classes):

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

- `xception-0-98-sports-classification.ipynb` — model notenook, you should run it to download `model_xception.h5` — Pre-trained Keras model (Xception) used for prediction.
- `app.py` — Main Streamlit app that runs the image classifier interface.
- `labels.json` — JSON file storing the class labels (e.g., Basketball, Football, etc.).
- `requirements.txt` — List of dependencies required to run the project.
- `README.md` — Documentation and instructions for the project.
