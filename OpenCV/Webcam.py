#pip install opencv-python
import cv2

#=========================================================
# # Подключение к вэбкамере
# cap = cv2.VideoCapture(0)
# while True:
#     _, frame = cap.read()
#     cv2.imshow("camera", frame)

#     if cv2.waitKey(1) & 0xff == ord('q'):
#         break
#=========================================================



#=========================================================
# Определение лица на фото
 
# face_cascades = cv2.CascadeClassifier(cv2.data.hearcascades + "hearcascade_frontalface_default.xml")
# img = cv2.imread("face.jpg")
# img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# faces = face_cascades.detectMultiScale(img_gray)

# for(x,y,w,h) in faces:
#     cv2.rectangle(img,(x,y), (x + w, y + h), (255, 0, 0), 2)

# cv2.imshow('Result', img)
# cv2.waitKey(0)
#=========================================================


#=====================================================================
# Распознание через вэбкамеру лица и выделение его в прямоугольник

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascades.detectMultiScale(img_gray)

    for(x, y, w, h) in faces:
        cv2.rectangle(img,(x,y), (x + w, y + h), (255, 0, 0), 2)
    
    cv2.imshow('Result', frame)

    if cv2.waitKey(1) & 0xff == ord('q')
        break
#=====================================================================