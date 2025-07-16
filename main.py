from PyQt5 import QtWidgets, uic
import sys
import cv2
from Utils.yolo_utils import detect_objects
from Utils.alert import send_email_alert

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi("gui_main.ui", self)

        self.startButton.clicked.connect(self.start_detection)
        self.stopButton.clicked.connect(self.stop_detection)
        self.alert_classes = ["person", "fire", "knife"]
        self.detection_active = False

    def start_detection(self):
        self.detection_active = True
        cap = cv2.VideoCapture(0)

        while self.detection_active:
            ret, frame = cap.read()
            if not ret:
                break
            frame, detected_labels = detect_objects(frame)

            for label in detected_labels:
                if label in self.alert_classes:
                    send_email_alert(label)

            cv2.imshow("Live Detection", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()

    def stop_detection(self):
        self.detection_active = False

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
