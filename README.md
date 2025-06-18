#Statement : Make a simple web app to detect facial emotions of a crowd in close range

#Solution : Made a flask based web server that uses the DEEPFACE library to analyze webcam or a demo video.
           Used Threading in webcam to make it smooth and fucntional and a perfect sync in frame for a demo video
           Used basic JS to fetch stats and display.
           Has Options do download logs of every 10th frame as a csv or json file along with timestamps
           The entire pipeline is designed to work offline after model download and supports smooth demo playback and live tracking

#📦Features:
  *🔍 Real-time face detection (Webcam or Demo Video)
  *👤 Shows Age, Gender, and Emotion
  *🎯 Filters people based on proximity (face size)
  *📊 Live stats panel with smooth auto-updating
  *💾 Logs downloadable as JSON or CSV


#TechStack: >Flask,DeepFace,HTML,CSS,JavaScript,OpenCV


#ScreenShots: ![Screenshot 2025-06-18 105549](https://github.com/user-attachments/assets/f7cb6476-b9dc-4bfb-a01a-4e629245308e)
             ![Screenshot 2025-06-18 090654](https://github.com/user-attachments/assets/ae3f3f2f-9f2f-4a3a-816c-0aed3f90ff4e)
             ![Screenshot 2025-06-18 085902](https://github.com/user-attachments/assets/5946676d-1c97-4c34-83db-056f85f36e43)

#How to run:
*MAKE SURE YOUR PYTHON VERSION IS 3.10 IF NOT THEN DOWNLOAD FROM python.org
```bash
