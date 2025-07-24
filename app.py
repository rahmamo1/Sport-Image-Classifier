import streamlit as st
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import json
from PIL import Image

# Page Configuration
st.set_page_config(page_title="🏆 Sport Image Classifier", layout="centered")

# Title Section
st.markdown(
    "<h1 style='text-align: center;'>🏅 Sport Image Classifier</h1>", 
    unsafe_allow_html=True
)
st.markdown(
    "<p style='text-align: center; font-size:18px;'>Upload a sports image and let the model predict its category!</p>", 
    unsafe_allow_html=True
)

# Load Model and Labels
@st.cache_resource
def load_model_and_labels():
    model = load_model("model_xception.h5")
    with open("labels.json", "r") as f:
        labels = json.load(f)
    return model, labels

model, labels = load_model_and_labels()

# Preprocess Function
def preprocess_image(img, target_size=(224, 224)):
    img = img.resize(target_size)
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    return img_array

# Upload Image Section
st.markdown("---")
st.subheader("📤 Upload Your Image")
uploaded_file = st.file_uploader(
    "Choose a sports image (JPG, JPEG, PNG)", 
    type=["jpg", "jpeg", "png"]
)

# Prediction Logic
if uploaded_file:
    col1, col2 = st.columns([1, 2])
    with col1:
        img = Image.open(uploaded_file).convert("RGB")
        st.image(img, caption="🎯 Uploaded Image", use_container_width=True)

    with col2:
        st.markdown("🔄 **Processing Image...**")
        processed_img = preprocess_image(img)
        prediction = model.predict(processed_img)[0]
        top_idx = np.argmax(prediction)
        predicted_label = labels[str(top_idx)]
        confidence = prediction[top_idx] * 100

        st.markdown("## ✅ Prediction Result")
        st.success(f"🏷️ **Predicted Sport:** `{predicted_label}`")
        st.info(f"📈 **Confidence:** `{confidence:.2f}%`")

    # Expander for Detailed Probabilities
    with st.expander("📊 Show Prediction Breakdown"):
        pred_probs = {labels[str(i)]: float(p) for i, p in enumerate(prediction)}
        sorted_probs = dict(sorted(pred_probs.items(), key=lambda x: x[1], reverse=True))
        st.bar_chart(sorted_probs)

# Footer
st.markdown("---")
st.markdown(
    "<p style='text-align: center; font-size:14px;'>✨ Made with ❤️</p>",
    unsafe_allow_html=True
)
