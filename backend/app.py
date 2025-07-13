from flask import Flask, request, jsonify
from flask_cors import CORS
import base64
import cv2
import numpy as np
import tempfile
import os
from posture_rules import analyze_posture

app = Flask(__name__)
CORS(app)

@app.route('/posture', methods=['POST'])
def process_webcam_image():
    try:
        data = request.get_json()
        image_data = data.get('image') if data else None

        if not image_data:
            return jsonify({'feedback': 'No image data received'}), 400

        header, encoded = image_data.split(",", 1) if "," in image_data else ("", image_data)
        image_bytes = base64.b64decode(encoded)
        np_arr = np.frombuffer(image_bytes, np.uint8)
        frame = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

        if frame is None:
            return jsonify({'feedback': 'Failed to decode image'}), 500

        result = analyze_posture(frame)
        return jsonify({'feedback': result})

    except Exception as e:
        return jsonify({'feedback': f'Error analyzing posture: {str(e)}'}), 500

@app.route('/posture/video', methods=['POST'])
def process_video_upload():
    try:
        if 'video' not in request.files:
            return jsonify({'feedback': 'No video file uploaded'}), 400

        video_file = request.files['video']

        with tempfile.NamedTemporaryFile(delete=False, suffix='.mp4') as tmp:
            video_file.save(tmp.name)
            video_path = tmp.name

        cap = cv2.VideoCapture(video_path)
        frame_count = 0
        posture_results = []

        while True:
            ret, frame = cap.read()
            if not ret:
                break
            frame_count += 1
            if frame_count % 15 == 0:
                result = analyze_posture(frame)
                posture_results.append(f"Frame {frame_count}: {result}")
            if frame_count > 150:
                break

        cap.release()
        os.remove(video_path)

        if not posture_results:
            return jsonify({'feedback': 'No valid frames detected in video'}), 500

        return jsonify({'feedback': "\n".join(posture_results)})

    except Exception as e:
        return jsonify({'feedback': f'Error processing video: {str(e)}'}), 500

if __name__ == '__main__':
    print("✅ Flask app running on http://localhost:5001")
    app.run(debug=True, host="0.0.0.0", port=5001)

