import face_recognition
import cv2
import os
import numpy as np

class FaceRecog():
    def __init__(self):
        self.known_face_encodings = []
        self.known_face_names = []

        # Load sample pictures and learn how to recognize them.
        dirname = 'knowns'
        files = os.listdir(dirname)
        for filename in files:
            name, ext = os.path.splitext(filename)
            if ext == '.jpg':
                self.known_face_names.append(name)
                pathname = os.path.join(dirname, filename)
                img = face_recognition.load_image_file(pathname)
                face_encoding = face_recognition.face_encodings(img)[0]
                self.known_face_encodings.append(face_encoding)

    def recognize_faces_in_image(self, image_path):
        # Load the image
        image = face_recognition.load_image_file(image_path)

        # Find all the faces and face encodings in the image
        face_locations = face_recognition.face_locations(image)
        face_encodings = face_recognition.face_encodings(image, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            # Compare the face with known faces
            distances = face_recognition.face_distance(self.known_face_encodings, face_encoding)
            min_value = min(distances)

            # tolerance: How much distance between faces to consider it a match. Lower is more strict.
            # 0.6 is typical best performance.
            name = "Unknown"
            if min_value < 0.6:
                index = np.argmin(distances)
                name = self.known_face_names[index]

            face_names.append(name)
            print(name)

        return face_locations, face_names

if __name__ == '__main__':
    face_recog = FaceRecog()
    print(face_recog.known_face_names)

    # 이미지 파일 경로 설정
    image_path = 'unknown/2.jpg'
    face_locations, face_names = face_recog.recognize_faces_in_image(image_path)

    # Load the image
    image = face_recognition.load_image_file(image_path)

    # Display the results
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        # Draw a box around the face
        cv2.rectangle(image, (left, top), (right, bottom), (0, 0, 255), 2)

        # Draw a label with a name below the face
        cv2.rectangle(image, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(image, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    # Show the image
    # cv2.imshow("Detected Faces", image)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    # print('finish')