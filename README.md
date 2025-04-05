Real-Time Face Detection with OpenCV
A Python-based application for real-time face detection using Haar Cascade classifiers via webcam.

📌 Features
Real-Time Detection: Identifies faces in live webcam feed.

Green Bounding Boxes: Highlights detected faces with green rectangles.

Matplotlib Integration: Uses matplotlib for visualization instead of OpenCV's default window.

Simple Exit: Press any key in the plot window to terminate.

🛠️ Installation
Clone the repository:

bash
git clone https://github.com/your-username/face-detection.git
cd face-detection
Install dependencies:

bash
pip install opencv-python matplotlib
🚀 Usage
bash
python face_detection.py
Ensure your webcam is accessible

Faces will be highlighted with green boxes

Press any key in the matplotlib window to exit

📂 Code Structure
python
face_detection.py
├── Webcam initialization
├── Haar Cascade classifier setup
├── Real-time frame processing loop
├── Face detection and visualization
└── Clean exit handling
