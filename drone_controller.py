import time
from utils.camera_stream import CameraStream
from object_detection import ObjectDetector

class DroneController:
    def __init__(self):
        self.camera = CameraStream()
        self.detector = ObjectDetector()

    def takeoff(self):
        print("[DRONE] Taking off...")
        time.sleep(2)
        print("[DRONE] Hovering at safe altitude.")

    def land(self):
        print("[DRONE] Landing...")
        time.sleep(2)
        print("[DRONE] Drone landed successfully.")

    def patrol(self):
        print("[DRONE] Starting patrol mode...")
        for frame in self.camera.stream():
            detections = self.detector.detect(frame)
            if detections:
                print(f"[DETECTION] Objects detected: {detections}")
            else:
                print("[DETECTION] No objects detected.")

            if "person" in detections:
                print("[DRONE] Person detected! Hovering in place.")
                break

        self.land()


if __name__ == "__main__":
    drone = DroneController()
    drone.takeoff()
    drone.patrol()
