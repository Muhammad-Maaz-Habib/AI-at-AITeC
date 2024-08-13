import sys
import cv2
cap = cv2.VideoCapture(0)
tracker = cv2.TrackerCSRT_create()
ok, frame=cap.read()
bbox = cv2.selectROI("Select ROI", frame, False)
tracker.init(frame,bbox)
def box(frame,bbox):
    x = bbox[0]
    y=bbox[1]
    w = bbox[2]
    h = bbox[3]
    cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
    cv2.putText(frame, "Tracking Object", (75, 80), cv2.FONT_HERSHEY_SIMPLEX, 1, (69, 30, 20), 2)
while True:
    timer = cv2.getTickCount()
    ok, frame=cap.read()
    success,bbox = tracker.update(frame)
    if not success:
        cv2.putText(frame, "Lost object", (75, 80), cv2.FONT_HERSHEY_SIMPLEX, 1, (69, 30, 20), 2)
    else:
        box(frame,bbox)
    fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer)
    cv2.putText(frame, str(int(fps)), (75,30), cv2.FONT_HERSHEY_SIMPLEX,1,(69,30,20),2)
    cv2.imshow("Tracking", frame)
    k = cv2.waitKey(1)
    if k == ord('q'):
        break


