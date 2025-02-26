# Handwritten_Text_Recognition

## 🚀 Inspiration  
Reading handwritten text accurately is a common challenge, especially when dealing with different handwriting styles. We wanted to create a tool that makes it easy to extract and refine handwritten text using AI. Our goal was to help students, professionals, and researchers by automating the process with deep learning.  

## ✨ What It Does  
- Allows users to **upload an image** of handwritten text.  
- Uses **AI-powered OCR (TrOCR)** to extract text from the image.  
- Applies **preprocessing techniques** to enhance OCR accuracy.  
- **Automatically corrects spelling mistakes** using TextBlob.  
- Provides an intuitive **Streamlit-based UI** for ease of use.  

## 🏗️ How We Built It  
1. **Model Selection**: We used **TrOCR (Transformer-based OCR)** for handwritten text recognition.  
2. **Preprocessing**: Converted images to grayscale, applied **Gaussian blur** and **adaptive thresholding** to improve text clarity.  
3. **Text Correction**: Integrated **TextBlob** for minor spelling corrections.  
4. **Frontend**: Built an interactive **Streamlit** web app for easy user interaction.  

## 🛠️ Challenges We Ran Into  
- Handwriting varies significantly, making OCR accuracy inconsistent.  
- Some extracted text contained **errors due to poor image quality** or model limitations.  
- Finding the right **preprocessing techniques** to improve recognition results.  

## 🎉 Accomplishments That We're Proud Of  
- Successfully integrated **TrOCR** for accurate handwritten text recognition.  
- Improved text accuracy through **adaptive preprocessing** techniques.  
- Created a **fully functional and user-friendly** web app with Streamlit.  

## 📚 What We Learned  
- The impact of **image preprocessing** on OCR performance.  
- How to fine-tune AI models for better accuracy.  
- The importance of **UX/UI design** in AI-powered applications.  

## 🔮 What's Next for Handwritten Text Recognition  
- Improving **support for different handwriting styles** and languages.  
- Adding a **real-time handwriting recognition feature** using a webcam.  
- Exploring **fine-tuning TrOCR** with a custom dataset for better accuracy.  
- Deploying the application as a **web service** for broader accessibility.  

