# main.py
from flask import Flask, render_template, Response, request, send_file
import cv2
import json
import csv
import threading
import time
from datetime import datetime
from deepface import DeepFace
import numpy as np

app = Flask(__name__)

logs = []
frame_buffer = None
analysis_result = []
frame_ready = threading.Event()
last_log_time = 0
last_result=[]

class DeepFaceAnalyzer(threading.Thread): #made a class thread to handle live feed for deepface
    def __init__(self):
        super().__init__()
        self.daemon = True
        self.start()

    def run(self):
        global frame_buffer, analysis_result
        while True:
            frame_ready.wait()
            frame_ready.clear()
            if frame_buffer is not None:
                try:
                    small = cv2.resize(frame_buffer, (480, 360))
                    result = DeepFace.analyze(
                        small,
                        actions=["age", "gender", "emotion"],
                        detector_backend="retinaface",
                        enforce_detection=False
                    )
                    analysis_result = result
                except Exception as e:
                    print("Analysis error (thread):", e)

DeepFaceAnalyzer()

def process_frame(frame, result): # processes each frame and gets its regions to draw bounding boxes and gets labels
    global last_log_time
    display_frame = frame.copy()
    MIN_AREA=1000
    h_ratio = frame.shape[0] / 360
    w_ratio = frame.shape[1] / 480
    current_time = time.time()

    if result:
        for res in result:
            try:
                region = res['region']
                x = int(region['x'] * w_ratio)
                y = int(region['y'] * h_ratio)
                w = int(region['w'] * w_ratio)
                h = int(region['h'] * h_ratio)
                if w * h < MIN_AREA:
                    continue  
                age = int(res.get('age', 0))
                gender = res.get('dominant_gender', 'Unknown')
                emotion = res.get('dominant_emotion', 'Neutral')
                label = f"{gender}, {age}, {emotion}"

                y_label = y - 10 if y - 10 > 10 else y + h + 20

                cv2.rectangle(display_frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                cv2.putText(display_frame, label, (x, y_label),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

                if current_time - last_log_time >= 10:
                    logs.append({
                        "timestamp": datetime.now().isoformat(),
                        "gender": gender,
                        "age": age,
                        "emotion": emotion
                    })
            except Exception as err:
                print("Drawing error:", err)

        if current_time - last_log_time >= 10:
            last_log_time = current_time

    return display_frame


def gen_video_demo(source): # did not use threading here as needed accurate results
    global last_result
    cap = cv2.VideoCapture(source)
    cap.set(cv2.CAP_PROP_FPS, 5)
    frame_index = 0

    while cap.isOpened():
        success, frame = cap.read()
        if not success:
            break

        frame_index += 1
        result = last_result

        if frame_index % 5 == 0:
            try:
                small = cv2.resize(frame, (480, 360))
                result = DeepFace.analyze(
                    small,
                    actions=["age", "gender", "emotion"],
                    detector_backend="retinaface",
                    enforce_detection=False
                )
                last_result = result  # ✅ Cache latest result
            except Exception as e:
                print("Analysis error (demo):", e)

        output = process_frame(frame, result)
        ret, buffer = cv2.imencode('.jpg', output)
        frame = buffer.tobytes()
        yield (b'--frame\r\nContent-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
        time.sleep(0.05)
    cap.release()



def gen_video_live(source):
    global frame_buffer
    cap = cv2.VideoCapture(source)
    cap.set(cv2.CAP_PROP_FPS, 5)
    frame_index = 0

    while cap.isOpened():
        success, frame = cap.read()
        if not success:
            break

        frame_index += 1
        if frame_index % 5 == 0:
            frame_buffer = frame.copy()
            frame_ready.set()

        output = process_frame(frame, analysis_result)
        ret, buffer = cv2.imencode('.jpg', output)
        frame = buffer.tobytes()
        yield (b'--frame\r\nContent-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
        time.sleep(0.05)
    cap.release()


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(gen_video_live(0), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/demo_feed')
def demo_feed():
    return Response(gen_video_demo("demo.mp4"), mimetype='multipart/x-mixed-replace; boundary=frame')




@app.route('/download_logs')
def download_logs():
    fmt = request.args.get("format", "json")
    if fmt == "csv":
        with open("logs.csv", "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=["timestamp", "gender", "age", "emotion"])
            writer.writeheader()
            writer.writerows(logs)
        return send_file("logs.csv", as_attachment=True)
    else:
        with open("logs.json", "w") as f:
            json.dump(logs, f, indent=2)
        return send_file("logs.json", as_attachment=True)



@app.route('/get_stats')
def get_stats():
    recent = logs[-5:] if len(logs) >= 5 else logs
    return json.dumps(recent)

if __name__ == '__main__':
    app.run(debug=True)
