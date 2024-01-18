from utils.nudenet import NudeDetector
import matplotlib.pyplot as plt
import cv2
import numpy as np
import os

def blur_boxes(image, detections):
    for detection in detections:
        if detection["class"] != "FACE_FEMALE":
            box = detection["box"]
            x, y, w, h = box[0], box[1], box[2], box[3]
           
            image[y:y + h, x:x + w] = (0,0,0)
    return image


def video_write(vid_file):
    try:
        os.remove("static/output.webm")
    except:
        pass
    model = NudeDetector()
    vd = cv2.VideoCapture(vid_file)
    output_video = cv2.VideoWriter(
        "output.webm",
        cv2.VideoWriter_fourcc(*"vp80"),
        30,
        (500, 500),
    )
    ret, frame = vd.read()
    while ret:
        dec = model.detect(frame)
        frame = blur_boxes(frame, dec)
        frame = cv2.resize(frame, (500, 500))
        output_video.write(frame)
        cv2.imshow("live", frame)
        key = cv2.waitKey(1)
        if key == ord('q'):
            break
        ret, frame = vd.read()
    vd.release()
    output_video.release()
    cv2.destroyAllWindows()


# video_write()
