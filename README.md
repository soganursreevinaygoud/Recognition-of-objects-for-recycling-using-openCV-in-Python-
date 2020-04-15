# Yolo-Object-Detection-with-openCV-in-Python
Due to rapid growth of technology and population, the need for the materials and usage have been increasing so the goods becoming useless 
from time to time. There is a huge dump of waste of all kinds i.e. electronic waste, plastic waste, wet waste and paper form. 
This waste should be taken care of, which cannot be handled completely by the government and is not the only duty of government 
but also the duty of all citizens, so there is a need to implement an application to help the citizens by recognizing the objects for recycling using image processing techniques and tools, so that it can help to recycle.

7.1 FOR LOADING THE IMAGE
#impotr the classes
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
24 | P a g e
7.2 CODE FOR DETECTING THE OBJECT
# imort the classes
import cv2
import numpy as np
# Load Yolo
net = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")
classes = []
with open("coco.names", "r") as f:
 classes = [line.strip() for line in f.readlines()]
layer_names = net.getLayerNames()
output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]
colors = np.random.uniform(0, 255, size=(len(classes), 3))
# Loading image
img = cv2.imread("mark.jpg")
img = cv2.resize(img, None, fx=0.25, fy=0.25)
height, width, channels = img.shape
# Detecting objects
blob = cv2.dnn.blobFromImage(img, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
net.setInput(blob)
outs = net.forward(output_layers)
25 | P a g e
# Showing informations on the screen
class_ids = []
confidences = []
boxes = []
for out in outs:
 for detection in out:
 scores = detection[5:]
 class_id = np.argmax(scores)
 confidence = scores[class_id]
 if confidence > 0.5:
 # Object detected
 center_x = int(detection[0] * width)
 center_y = int(detection[1] * height)
 w = int(detection[2] * width)
 h = int(detection[3] * height)
 cv2.circle(img,(center_x,center_y),10,(0,255,0),2)
cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
26 | P a g e
7.3 CODE FOR FORMIMG RECTANGULAR CORIDINATES
#import the classes
import cv2
import numpy as np
# Load Yolo
net = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")
classes = []
with open("coco.names", "r") as f:
 classes = [line.strip() for line in f.readlines()]
layer_names = net.getLayerNames()
output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]
colors = np.random.uniform(0, 255, size=(len(classes), 3))
# Loading image
img = cv2.imread("mark.jpg")
img = cv2.resize(img, None, fx=0.25, fy=0.25)
height, width, channels = img.shape
# Detecting objects
blob = cv2.dnn.blobFromImage(img, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
net.setInput(blob)
outs = net.forward(output_layers)
27 | P a g e
# Showing informations on the screen
class_ids = []
confidences = []
boxes = []
for out in outs:
 for detection in out:
 scores = detection[5:]
 class_id = np.argmax(scores)
 confidence = scores[class_id]
 if confidence > 0.5:
 # Object detected
 center_x = int(detection[0] * width)
 center_y = int(detection[1] * height)
 w = int(detection[2] * width)
 h = int(detection[3] * height)
 # Rectangle coordinates
 x = int(center_x - w / 2)
 y = int(center_y - h / 2)
 cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
28 | P a g e
7.4 CODEFOR IDENTIFYING THE NAME OF THE OBJECT
AND CAPABLE OF RECOGNISING WHETHER IT IS
RECYCLABLE (OR) NOT
#import the classes
import cv2
import numpy as np
# Load Yolo
net = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")
classes = []
with open("coco.names", "r") as f:
 classes = [line.strip() for line in f.readlines()]
layer_names = net.getLayerNames()
output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]
colors = np.random.uniform(0, 255, size=(len(classes), 3))
# Loading image
img = cv2.imread("mark.jpg")
img = cv2.resize(img, None, fx=0.25, fy=0.25)
height, width, channels = img.shape
# Detecting objects
blob = cv2.dnn.blobFromImage(img, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
net.setInput(blob)
29 | P a g e
outs = net.forward(output_layers)
# Showing informations on the screen
class_ids = []
confidences = []
boxes = []
for out in outs:
 for detection in out:
 scores = detection[5:]
 class_id = np.argmax(scores)
 confidence = scores[class_id]
 if confidence > 0.5:
 # Object detected
 center_x = int(detection[0] * width)
 center_y = int(detection[1] * height)
 w = int(detection[2] * width)
 h = int(detection[3] * height)
 # Rectangle coordinates
 x = int(center_x - w / 2)
 y = int(center_y - h / 2)
 cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
30 | P a g e
cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
