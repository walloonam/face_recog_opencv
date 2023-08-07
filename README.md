# 졸업프로젝트 - face_recognition

## OpenCV 및 face_recognition을 이용한 안면 인식 프로젝트

이 프로젝트는 Python과 OpenCV, 그리고 face_recognition 라이브러리를 사용하여 이미지에서 안면을 인식하는 예제입니다. 미리 학습된 얼굴 인코딩을 사용하여 이미지 내의 얼굴을 식별하고 레이블을 부여합니다.

## 기능

- 이미지에서 얼굴을 감지하고 레이블을 부여합니다.
- 사전에 학습된 얼굴 인코딩을 사용하여 이미지 내의 얼굴을 인식합니다.

## 시작하기

1. 저장소를 복제합니다:
   ```bash
   git clone https://github.com/your-username/face_recog_opencv.git
2. Python 환경을 설정합니다
   ```bash
   pip install opencv-python
   pip install face-recognition
3. knowns 폴더에 학습용 얼굴 이미지를 추가합니다.
4. unknown 폴더에 식별할 이미지를 추가합니다.
5. main.py 파일을 실행하여 이미지에서 얼굴을 인식하고 레이블을 부여합니다.

## 코드 설명
- FaceRecog 클래스: 사전에 학습된 얼굴 인코딩을 로드하고 이미지 내의 얼굴을 인식하는 클래스입니다.
- recognize_faces_in_image(image_path): 이미지 내의 얼굴을 인식하고 레이블을 반환하는 함수입니다.

## 기여하기
이 프로젝트에 기여는 환영합니다! 문제점을 찾거나 새로운 기능을 추가하려면 언제든지 풀 리퀘스트를 열어주세요.
