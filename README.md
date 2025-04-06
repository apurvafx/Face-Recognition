# Real-Time Face Detection Using OpenCV and Matplotlib

This project demonstrates a real-time face detection system using Python, OpenCV, and Matplotlib. The program captures video from your webcam, detects faces in real-time using Haar cascades, and displays the video feed with detected faces highlighted in a matplotlib plot.

---

## Features

- **Real-Time Face Detection**: Detects faces in live video captured from your webcam.
- **Haar Cascade Classifier**: Uses OpenCV's pre-trained Haar cascade classifier for face detection.
- **Interactive Plot**: Displays the video feed with detected faces in a matplotlib plot. You can exit the program by pressing any key in the plot window.

---

## Requirements

Make sure you have the following installed:

- Python 3.x
- OpenCV (`cv2`)
- Matplotlib

You can install the required libraries using pip:
```pip install opencv-python matplotlib

---

## How to Run

1. Clone this repository or download the script file.
2. Open a terminal or command prompt and navigate to the directory containing the script.
3. Run the script using Python:


4. The program will activate your webcam and display a live video feed with detected faces highlighted by green rectangles.
5. Press any key in the matplotlib plot window to terminate the program.

---

## Code Explanation

### Key Components

1. **Face Detection**:
- The program uses OpenCV's `CascadeClassifier` with the `haarcascade_frontalface_default.xml` model to detect faces in each frame of the video.

2. **Webcam Video Capture**:
- The `cv2.VideoCapture(0)` function captures live video from your default webcam.

3. **Matplotlib Integration**:
- The live video feed is displayed using Matplotlib's `imshow` function, allowing for an interactive display.

4. **Exit Mechanism**:
- The program terminates when you press any key inside the matplotlib plot window.

---

## Troubleshooting

1. **Webcam Not Detected**:
- Ensure that your webcam is connected and accessible.
- Check if another application is using your webcam.

2. **No Faces Detected**:
- Ensure proper lighting conditions for better face detection.
- Adjust the parameters of `detectMultiScale` (e.g., `scaleFactor` or `minNeighbors`) if necessary.

3. **Matplotlib Window Freezes**:
- Ensure that you're running the script in an environment that supports interactive plotting (e.g., local Python installation, not Jupyter Notebook).

---

## License

This project is licensed under the MIT License. Feel free to use, modify, and distribute it as needed.

---

## Acknowledgments

- OpenCV for providing powerful computer vision tools.
- Matplotlib for enabling interactive visualization.

