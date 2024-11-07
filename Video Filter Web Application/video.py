from utils.nudenet import NudeDetector
import cv2
import os

def blur_boxes(image, detections):
    for detection in detections:
        if detection["class"] != "FACE_FEMALE":
            x, y, w, h = detection["box"]
            image[y:y + h, x:x + w] = cv2.GaussianBlur(image[y:y + h, x:x + w], (51, 51), 0)
    return image

def video_write(vid_file):
    output_path = "static/output.webm"
    if os.path.exists(output_path):
        os.remove(output_path)

    model = NudeDetector()
    vd = cv2.VideoCapture(vid_file)
    if not vd.isOpened():
        print(f"Error: Could not open video file {vid_file}")
        return

    frame_width = int(vd.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(vd.get(cv2.CAP_PROP_FRAME_HEIGHT))
    output_video = cv2.VideoWriter(
        output_path,
        cv2.VideoWriter_fourcc(*"VP80"),
        30,
        (frame_width, frame_height),
    )

    while True:
        ret, frame = vd.read()
        if not ret:
            break

        detections = model.detect(frame)
        frame = blur_boxes(frame, detections)
        output_video.write(frame)
        cv2.imshow("live", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    vd.release()
    output_video.release()
    cv2.destroyAllWindows()

# Uncomment the following line to run the function
# video_write("/path/to/your/video/file")
