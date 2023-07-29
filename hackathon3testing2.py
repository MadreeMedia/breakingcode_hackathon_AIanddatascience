import threading

import cv2
from deepface import DeepFace
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

counter = 0
face_match = False

reference_img = cv2.imread("C:/Users/Admin/PycharmProjects/pythonProject/source code/images/WIN_20230728_23_31_48_Pro.jpg")
reference_img2 = cv2.imread("C:/Users/Admin/PycharmProjects/pythonProject/source code/images/sahananew.jpg")
reference_img3 = cv2.imread("C:/Users/Admin/PycharmProjects/pythonProject/source code/images/ot member 2.jpg")
reference_img4 = cv2.imread("C:/Users/Admin/PycharmProjects/pythonProject/source code/images/ot memeber 3.jpg")
reference_img5 = cv2.imread("C:/Users/Admin/PycharmProjects/pythonProject/source code/images/WhatsApp Image 2023-07-28 at 16.59.35.jpg")

def check_face(frame):
    global face_match
    try:
        if DeepFace.verify(frame, reference_img.copy())['verified']:
            face_match = True
        else:
            face_match = False
    except ValueError:
        face_match = False

while True:
    ret, frame = cap.read()

    if ret:
      if counter % 45 == 0:
         try:
            threading.Thread(target=check_face, args=(frame.copy(),)).start()
         except ValueError:
             pass
      counter += 1

      if face_match:
        cv2.putText(frame, "This is a human", (20, 450), cv2.FONT_ITALIC, 2, (255, 0, 0), 3)
      else:
        cv2.putText(frame, "This is an alien", (20, 450), cv2.FONT_ITALIC, 2, (0, 0, 255), 3)

      cv2.imshow("video", frame)

    key = cv2.waitKey(1)
    if key == ord("q"):
        break

cv2.destroyAllWindows()

reference_img = reference_img2

while True:
    ret, frame = cap.read()

    if ret:
      if counter % 45 == 0:
         try:
            threading.Thread(target=check_face, args=(frame.copy(),)).start()
         except ValueError:
             pass
      counter += 1

      if face_match:
        cv2.putText(frame, "HUMAN", (20, 450), cv2.FONT_ITALIC, 2, (255, 0, 0), 3)
      else:
        cv2.putText(frame, "ALIEN", (20, 450), cv2.FONT_ITALIC, 2, (0, 0, 255), 3)

      cv2.imshow("video", frame)

    key = cv2.waitKey(1)
    if key == ord("q"):
        break

cv2.destroyAllWindows()

reference_img = reference_img3

while True:
    ret, frame = cap.read()

    if ret:
      if counter % 45 == 0:
         try:
            threading.Thread(target=check_face, args=(frame.copy(),)).start()
         except ValueError:
             pass
      counter += 1

      if face_match:
        cv2.putText(frame, "This is a human", (20, 450), cv2.FONT_ITALIC, 2, (255, 0, 0), 3)
      else:
        cv2.putText(frame, "This is an alien", (20, 450), cv2.FONT_ITALIC, 2, (0, 0, 255), 3)

      cv2.imshow("video", frame)

    key = cv2.waitKey(1)
    if key == ord("q"):
        break

cv2.destroyAllWindows()

reference_img = reference_img4

while True:
    ret, frame = cap.read()

    if ret:
      if counter % 45 == 0:
         try:
            threading.Thread(target=check_face, args=(frame.copy(),)).start()
         except ValueError:
             pass
      counter += 1

      if face_match:
        cv2.putText(frame, "This is a human", (20, 450), cv2.FONT_ITALIC, 2, (255, 0, 0), 3)
      else:
        cv2.putText(frame, "This is an alien", (20, 450), cv2.FONT_ITALIC, 2, (0, 0, 255), 3)

      cv2.imshow("video", frame)

    key = cv2.waitKey(1)
    if key == ord("q"):
        break

cv2.destroyAllWindows()

reference_img = reference_img5

while True:
    ret, frame = cap.read()

    if ret:
      if counter % 45 == 0:
         try:
            threading.Thread(target=check_face, args=(frame.copy(),)).start()
         except ValueError:
             pass
      counter += 1


      if face_match:
        cv2.putText(frame, "This is a human", (20, 450), cv2.FONT_ITALIC, 2, (255, 0, 0), 3)
      else:
        cv2.putText(frame, "This is an alien", (20, 450), cv2.FONT_ITALIC, 2, (0, 0, 255), 3)

      cv2.imshow("video", frame)

    key = cv2.waitKey(1)
    if key == ord("q"):
        break

cv2.destroyAllWindows()







