# Import necessary modules
from io import BytesIO

import cv2
import numpy as np
import pytesseract
import streamlit as st
from gtts import gTTS
from PIL import Image

import pytesseract
import os

import pytesseract
pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'  # Replace with the correct path


# Define functions
def extract_text_from_image(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # Convert to grayscale
    text = pytesseract.image_to_string(gray)  # Perform OCR
    return text

def text_to_speech(text):
    tts = gTTS(text, lang='en')  # Convert text to speech
    audio_fp = BytesIO()
    tts.write_to_fp(audio_fp)
    audio_fp.seek(0)
    return audio_fp

# Streamlit app
def main():
    st.title("Text-to-Speech for Visual Content")
    st.write("Upload an image to extract text and convert it to audible speech.")

    # Upload image
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
    if uploaded_file is not None:
        # Display the uploaded image
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)

        # Convert PIL image to OpenCV format
        image_cv = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

        # Extract text
        if st.button("Extract Text"):
            extracted_text = extract_text_from_image(image_cv)
            st.write("Extracted Text:")
            st.text(extracted_text)

            # Convert text to speech
            if extracted_text.strip():
                st.write("Generating Speech...")
                audio_file = text_to_speech(extracted_text)
                st.audio(audio_file, format="audio/mp3")
            else:
                st.warning("No text detected in the image.")

if __name__ == "__main__":
    main()
