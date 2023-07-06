import cv2
import pyvirtualcam

# Face Recognition (you can change the cascade if you want)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

video_capture = cv2.VideoCapture(0)

padding = 0

def calc_padding():
    try:
        x_pad = max(0, x - padding)
        y_pad = max(0, y - padding)
        w_pad = min(frame.shape[1], x + w + padding) - x_pad
        h_pad = min(frame.shape[0], y + h + padding) - y_pad
        return x_pad, y_pad, w_pad, h_pad
    except:
        return 0, 0, 0, 0

# Create a virtual camera (you can modify the width, height and fps)
with pyvirtualcam.Camera(width=680, height=480, fps=60) as virtual_cam:
    print(f'Using virtual camera')

    while True:
        ret, frame = video_capture.read()
        faces = face_cascade.detectMultiScale(frame, scaleFactor=1.1, minNeighbors=4, minSize=(1, 1))

        try:
            x, y, w, h = faces[0]
            padding = 100
            x_pad, y_pad, w_pad, h_pad = calc_padding()

            face_roi = frame[y_pad:y_pad + h_pad, x_pad:x_pad + w_pad]
            
            # Resize frame to match virtual camera dimensions
            frame = cv2.resize(face_roi, (680, 480))

            # Convert the frame to RGB format
            frame= cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # Send the frame to the virtual camera
            virtual_cam.send(frame)
        except:
            padding = 0
            x_pad, y_pad, w_pad, h_pad = (0, 0, 0, 0)
            face_roi = frame[y_pad:y_pad + h_pad, x_pad:x_pad + w_pad]

            # Convert the frame to RGB format
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # Resize frame to match virtual camera dimensions
            frame = cv2.resize(frame, (680, 480))

            # Send the frame to the virtual camera
            virtual_cam.send(frame)

        # Receive the frame in the virtual camera
        virtual_cam.sleep_until_next_frame()