import cv2
from matplotlib import pyplot as plt


face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')


video_capture = cv2.VideoCapture(0)

if not video_capture.isOpened():
    print("Error: Could not open webcam.")
    exit()

while True:
    
    ret, frame = video_capture.read()
    if not ret:
        print("Error: Failed to capture frame.")
        break

    
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    
    faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    
    plt.imshow(rgb_frame)
    plt.title("Face Detection")
    plt.axis("off")
    plt.pause(0.01)  

    
    if plt.waitforbuttonpress(timeout=0.01):  
        break


video_capture.release()
plt.close()
