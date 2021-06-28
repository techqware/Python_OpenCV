import cv2
import winsound

# zero(0) is for single camera if you've ultiple camera you can change with 1,2,3,4..... etc 
cam = cv2.VideoCapture(0,cv2.CAP_DSHOW)
while cam.isOpened():        
    haar_cascade = cv2.CascadeClassifier('haar_face.xml')

    people = ['pp']
    # features = np.load('features.npy', allow_pickle=True)
    # labels = np.load('labels.npy')

    face_recognizer = cv2.face.LBPHFaceRecognizer_create()
    face_recognizer.read('face_trained.yml')

    img = cv2.imread(r'F:\pic\riz.jpg')

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv.imshow('Person', gray)

    # Detect the face in the image
    faces_rect = haar_cascade.detectMultiScale(gray, 1.1, 4)

    for (x,y,w,h) in faces_rect:
        faces_roi = gray[y:y+h,x:x+w]

        label, confidence = face_recognizer.predict(faces_roi)
        print(f'Label = {people[label]} with a confidence of {confidence}')

        cv2.putText(img, str(people[label]), (20,20), cv.FONT_HERSHEY_COMPLEX, 1.0, (0,255,0), thickness=2)
        cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), thickness=2)

    cv2.imshow('Detected Face', img)
    if cv2.waitKey(10) == ord('q'):
        break
