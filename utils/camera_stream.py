import cv2

class CameraStream:
    def __init__(self, camera_id=0):
        self.cap = cv2.VideoCapture(camera_id)

    def stream(self):
        while True:
            ret, frame = self.cap.read()
            if not ret:
                break
            yield frame

    def __del__(self):
        self.cap.release()
        cv2.destroyAllWindows()
