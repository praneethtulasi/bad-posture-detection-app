import base64
import requests
import json

image_path = "squat.jpg"  # Make sure this image exists in the backend folder

with open(image_path, "rb") as img_file:
    b64_string = base64.b64encode(img_file.read()).decode('utf-8')
    payload = {
        "image": f"data:image/jpeg;base64,{b64_string}"
    }

    response = requests.post("http://localhost:5001/posture", json=payload)
    print("Status Code:", response.status_code)
    print("Response:", response.json())
