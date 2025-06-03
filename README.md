# AI-powered Face Recognition Attendance System

An intelligent attendance management system that leverages computer vision and speech technologies to automate and streamline the process of recording attendance through facial recognition.

## 🔍 Overview

This project utilizes OpenCV for real-time face detection and recognition, Pillow for image processing, and Tkinter for a user-friendly GUI. Additionally, it incorporates speech capabilities using `pyttsx3` for text-to-speech and `SpeechRecognition` for voice command processing, enhancing interactivity and accessibility.

## 🎯 Features

- **Real-time Face Detection & Recognition**: Accurately detects and recognizes faces from live webcam feed.
- **Graphical User Interface (GUI)**: Intuitive interface built with Tkinter for ease of use.
- **Voice Interaction**: Provides auditory feedback and accepts voice commands for hands-free operation.
- **Image Processing**: Processes and manages images using the Pillow library.
- **Attendance Logging**: Records attendance data with timestamps in a log file.

## 🛠️ Technologies Used

- **Programming Language**: Python
- **Libraries & Frameworks**:
  - OpenCV
  - Pillow
  - Tkinter
  - pyttsx3
  - SpeechRecognition

## 📂 Project Structure
AI-powered-Face-Recognission-Attendance-System/
├── fras.py # Main application script
├── SpeechR.py # Handles speech recognition and text-to-speech
├── util.py # Utility functions for image processing
├── log.txt # Attendance log file
├── README.md # Project documentation


## 🚀 Getting Started

### Prerequisites

Ensure you have Python 3.x installed. Install the required libraries using pip:

```bash
pip install opencv-python Pillow pyttsx3 SpeechRecognition
```

Installation:

1. Clone the repository:
   ```bash
   git clone https://github.com/Chetansonawane7/AI-powered-Face-Recognission-Attendance-System.git
2. Navigate to the Project Directory:
   ```bash
   cd AI-powered-Face-Recognission-Attendance-System
3. Run The Main Application:
   ```bash
   python fras.py

🧠 How It Works
Face Detection: The system accesses the webcam feed and detects faces in real-time using OpenCV's Haar cascades or deep learning-based methods.

Face Recognition: Recognized faces are matched against a stored dataset to identify individuals.

Attendance Logging: Upon successful recognition, the system logs the individual's name along with the current timestamp in log.txt.

Voice Feedback: The system provides auditory confirmation of attendance marking and can accept voice commands for certain operations.

🤝 Contributing
Contributions are welcome! Please follow these steps:

Fork the repository.

Create a new branch: git checkout -b feature/YourFeature

Commit your changes: git commit -m 'Add your feature'

Push to the branch: git push origin feature/YourFeature

Open a pull request.

📄 License
This project is open-source and available under the MIT License.

📬 Contact
For any inquiries or feedback, please contact Chetan Sonawane on sonawanechetan847@gmail.com

Let me know if you'd like a shorter version or any customization (like adding a demo video or image links)!

