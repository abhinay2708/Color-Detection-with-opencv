# 🎥 Real-time Color Detection with OpenCV + Streamlit

This project lets you detect specific colors in **real time** using your **webcam**.  
It is built with:
- **OpenCV** → for image processing  
- **NumPy** → for working with pixel arrays  
- **Streamlit** + **streamlit-webrtc** → for creating a live interactive web app  

---

## 🔍 How It Works
1. The app captures video from your webcam directly in the browser.  
2. Each video frame is converted from **BGR to HSV color space**.  
   - **Hue (H)** = the type of color (red, green, blue, etc.)  
   - **Saturation (S)** = intensity of the color  
   - **Value (V)** = brightness of the color  
3. Based on the color you choose in the sidebar, the app creates a **mask** that isolates only that color.  
4. The result is displayed in real time on the screen.  

---

## 🛠️ Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/color-detection-webcam.git
   cd color-detection-webcam
