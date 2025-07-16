import torch
import cv2

model = torch.hub.load("ultralytics/yolov5", "yolov5s", pretrained=True)

def detect_objects(frame):
    results = model(frame)
    detected = results.pandas().xyxy[0]
    labels = []

    for _, row in detected.iterrows():
        conf = row['confidence']
        label = row['name']
        if conf > 0.5:
            x1, y1, x2, y2 = map(int, [row['xmin'], row['ymin'], row['xmax'], row['ymax']])
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0,255,0), 2)
            cv2.putText(frame, f"{label} {conf:.2f}", (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), 2)
            labels.append(label)
    return frame, labels

