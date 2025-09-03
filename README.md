# 🎨 Color Detection using OpenCV and Streamlit

This project is about detecting colors in real time using your computer's webcam.  
We use **OpenCV** (for image processing), **NumPy** (for handling arrays), and **Streamlit** (for making a simple web app).

---

## 🔍 How the Code Works

1. **Capture video**  
   The app uses your webcam to capture live video.

2. **Convert colors**  
   The captured video (BGR format) is converted into **HSV format**.  
   - H (Hue): actual color (red, green, blue, etc.)  
   - S (Saturation): intensity of the color  
   - V (Value): brightness of the color  

3. **Define color ranges**  
   For each color (Red, Green, Blue, Yellow, Orange, Purple), we set a **range in HSV values**.  
   Example: Red is between `[161, 155, 84]` and `[179, 255, 255]`.

4. **Create a mask**  
   The mask checks which pixels of the frame fall inside the chosen color range.

5. **Show result**  
   Only the parts of the frame that match the selected color are displayed.  
   You can choose the color from the sidebar in the Streamlit app.

---

## ▶️ How to Run

1. Install requirements:
   ```bash
   pip install -r requirements.txt
