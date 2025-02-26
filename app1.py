import streamlit as st
import cv2
import torch
import numpy as np
from transformers import TrOCRProcessor, VisionEncoderDecoderModel
from PIL import Image
from textblob import TextBlob

def add_background_color():
    st.markdown(
        """
        <style>
        body {
            background-color: #f0f2f6;
        }
        .stApp {
            background-color: #e6f7ff;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

# Load the pre-trained TrOCR model
processor = TrOCRProcessor.from_pretrained("microsoft/trocr-base-handwritten")
model = VisionEncoderDecoderModel.from_pretrained("microsoft/trocr-base-handwritten")

def preprocess_image(image):
    """Apply Gaussian Blur and Adaptive Thresholding for better OCR results."""
    image_np = np.array(image.convert("L"))  # Convert to grayscale NumPy array
    image_np = cv2.GaussianBlur(image_np, (3, 3), 0)  # Reduce noise
    image_np = cv2.adaptiveThreshold(image_np, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                     cv2.THRESH_BINARY, 11, 2)  # Enhance contrast
    processed_image = Image.fromarray(cv2.cvtColor(image_np, cv2.COLOR_GRAY2RGB))  # Convert back to RGB
    return processed_image

def extract_text_trocr(image):
    """Extract text using TrOCR from a preprocessed image."""
    preprocessed_img = preprocess_image(image)
    pixel_values = processor(images=preprocessed_img, return_tensors="pt").pixel_values

    with torch.no_grad():
        generated_ids = model.generate(pixel_values)

    extracted_text = processor.batch_decode(generated_ids, skip_special_tokens=True)[0]
    return extracted_text

def correct_text(image):
    extracted_text = extract_text_trocr(image)
    corrected_text = str(TextBlob(extracted_text).correct())  # Fix typos
    return corrected_text

add_background_color()

st.title("📝 Handwritten Text Recognition")
st.write("Upload a sentence of handwritten text, and the model will extract and correct the text.")

uploaded_file = st.file_uploader("Choose an image...", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded Image", use_container_width=True)

    with st.spinner("Extracting text..."):
        extracted_text = correct_text(image)

    st.subheader("Extracted & Corrected Text:")
    st.write(extracted_text)
