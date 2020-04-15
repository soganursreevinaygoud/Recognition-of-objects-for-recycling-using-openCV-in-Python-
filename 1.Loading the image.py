import cv2
import numpy as np

# Load Yolo
net = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")
classes = []
with open("coco.names", "r") as f:
    classes = [line.strip() for line in f.readlines()]
layer_names = net.getLayerNames()
output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]

# Loading image
img = cv2.imread("mark.jpg")
img = cv2.resize(img, None, fx=0.25, fy=0.25)
cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

