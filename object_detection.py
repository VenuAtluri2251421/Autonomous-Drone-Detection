import cv2

class ObjectDetector:
    def __init__(self):
        # NOTE: YOLO training & model creation is in your other repo:
        # https://github.com/<your-username>/learn-yolo-in-6-steps
        # Here, we just load the trained model weights.
        self.model_path = "yolo_model/yolov5s.onnx"  # placeholder path
        try:
            self.net = cv2.dnn.readNet(self.model_path)
        except:
            self.net = None
            print("[WARNING] YOLO model not found. Please add weights in yolo_model/.")

        self.classes = ["person", "car", "dog"]  # example classes

    def detect(self, frame):
        if self.net is None:
            return []
        blob = cv2.dnn.blobFromImage(frame, 1/255.0, (640, 640), swapRB=True, crop=False)
        self.net.setInput(blob)
        outputs = self.net.forward()

        detections = []
        for output in outputs:
            if output[4] > 0.5:  # confidence threshold
                class_id = int(output[5])
                detections.append(self.classes[class_id % len(self.classes)])
        return detections
