from ultralytics import YOLO
import cv2
import tempfile
import imageio
import os

model = YOLO("best.pt")


def detect_image(image):

    results = model(image)
    annotated = results[0].plot()

    return annotated


def detect_video(video_file):

    temp_input = tempfile.NamedTemporaryFile(delete=False)
    temp_input.write(video_file.read())
    temp_input.close()

    cap = cv2.VideoCapture(temp_input.name)

    frames = []

    while True:

        ret, frame = cap.read()

        if not ret:
            break

        results = model(frame)

        annotated_frame = results[0].plot()

        frames.append(annotated_frame)

    cap.release()

    output_path = "processed_video.mp4"

    imageio.mimsave(output_path, frames, fps=20)

    return output_path