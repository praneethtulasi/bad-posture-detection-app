**Bad Posture Detection App**
This is a full-stack posture analysis application designed to help individuals monitor and correct their posture in real time or from recorded videos. The system uses a combination of modern web technologies and computer vision to detect and provide feedback on common posture-related issues, particularly during activities like squatting or prolonged desk work.

The application includes a React-based frontend for capturing video or webcam input and a Flask backend that processes the visual data, detects key points using MediaPipe, and evaluates posture based on a rule-based system.

Ke**y Features**
Real-time posture analysis through webcam

Support for video uploads (MP4 format)

Rule-based detection for identifying incorrect postures

Visual feedback and suggestions for correction

Simple and intuitive user interface

Black and pink themed design for a focused and modern look

**Technologies Used**
**Frontend:**

React

react-webcam

Axios

CSS for theming and layout

**Backend:**

Python

Flask

OpenCV

MediaPipe (for pose/keypoint detection)

Project Structure
php
Copy
Edit
**bad-posture-detection-app/
├── backend/                  # Flask backend logic
│   ├── postureRules.py       # Rule-based logic for posture detection
│   └── app.py                # API endpoints
├── public/                   # React public assets
├── src/                      # React frontend source
│   └── components/           # React components
├── squat.jpg                 # Sample image
├── squat.mp4                 # Sample video
├── .gitignore
├── package.json
└── README.md**
**How It Works**
The user selects either webcam input or video file.

The frontend captures the frame or video and sends it to the backend.

The backend uses MediaPipe to extract human pose keypoints.

Predefined rules (based on angles, posture alignment) are applied to evaluate correctness.

Feedback is sent back and displayed in the UI.

**How to Run**
**1. Frontend (React):**

bash
Copy
Edit
cd bad-posture-detection-app
npm install
npm start
**2. Backend (Flask):**

bash
Copy
Edit
cd backend
pip install -r requirements.txt
python app.py
Ensure both the frontend and backend servers are running concurrently for full functionality.

**Future Improvements**
Integrate machine learning for dynamic posture classification

Add support for different types of exercises or movements

Deploy the full-stack app using platforms like Vercel (frontend) and Render or Railway (backend)

Add authentication and user history tracking

**License**
This project is intended for educational and personal portfolio use.
