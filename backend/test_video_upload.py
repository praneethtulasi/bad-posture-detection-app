import requests

video_path = "squat.mp4"  # Ensure this file is in the backend folder

with open(video_path, "rb") as f:
    files = {"video": f}
    response = requests.post("http://localhost:5001/posture/video", files=files)

print("Status Code:", response.status_code)
print("Response:", response.json())

