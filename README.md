# 🧠 Real-Time Facial Emotion Detection Web App

> A simple web app to detect facial emotions of a crowd in close range using webcam or a demo video.

---

## 📌 Statement

Build a simple web app that can detect **facial emotions** from a **crowd in close proximity** using a webcam or video file.

---

## 💡 Solution

Created a **Flask-based web server** using the **DeepFace** library to analyze frames from a webcam or demo video.

### ✅ Key Highlights:

- 🧵 Used threading for **smooth live webcam performance**
- 🎞️ Achieved perfect **frame sync** for demo video playback
- ⚙️ Built a **live stats panel** using basic JavaScript
- 💾 Logs are saved every **10 seconds** and downloadable as `.csv` or `.json`
- 📡 Fully **offline capable** after first-time model download

---

## 📦 Features

- 🔍 Real-time face detection (Webcam or Demo Video)
- 👤 Displays Age, Gender, and Emotion
- 🎯 Proximity filtering (based on face size)
- 📊 Auto-updating live stats panel (updated every 2s)
- 💾 Download logs as **JSON** or **CSV**
- 🌐 Works offline and deployable via Render

---

## 🛠️ Tech Stack

> **Backend:** Flask, DeepFace  
> **Frontend:** HTML, CSS, JavaScript  
> **Libraries:** OpenCV, Numpy, Gunicorn

---

## 📸 Screenshots

| Interface | Detection | Stats Panel |
|-----------|-----------|-------------|
| ![Screenshot 1](https://github.com/user-attachments/assets/f7cb6476-b9dc-4bfb-a01a-4e629245308e) | ![Screenshot 2](https://github.com/user-attachments/assets/ae3f3f2f-9f2f-4a3a-816c-0aed3f90ff4e) | ![Screenshot 3](https://github.com/user-attachments/assets/5946676d-1c97-4c34-83db-056f85f36e43) |

---

## 🧱 Project Structure

```text
RT_Facial_Analysis/
├── app.py               # Flask backend
├── requirements.txt     # Python dependencies
├── demo.mp4             # Preloaded demo video
├── templates/
│   └── index.html       # Frontend HTML
├── static/
│   ├── style.css        # CSS styling
│   └── app.js           # JavaScript functionality
```
## 🚀 How to Run Locally
 > ⚠️ Python 3.10 is required
 > Download it from: https://www.python.org/downloads/release/python-3100/

📥 1. Clone the Repository
```bash
git clone https://github.com/NoobieDYG/RT_Facial_Analysis.git
cd RT_Facial_Analysis
```
🧪 2. Create a Virtual Environment (Python 3.10)
```bash
python -m venv venv
venv\Scripts\activate     # On Windows
```
📦 3. Install Dependencies
```bash
pip install -r requirements.txt
```
▶️ 4. Run the App
```bash
python app.py
```
### ⚙️ How It Works
  > Live Mode	Uses background thread for analysis to keep webcam feed smooth
  > Demo Mode	Blocks on every 10th frame to ensure boxes are perfectly aligned
  > DeepFace	Returns age, gender, and emotion for each detected face
  > UI	Stats panel updates every 2 seconds with only the closest visible person




