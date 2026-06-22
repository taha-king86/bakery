import cv2
import face_recognition
import os
from datetime import datetime
from utils import print_fa

def capture_and_save_face(save_dir='assets/faces/'):
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    cap = cv2.VideoCapture(0)
    print_fa('لطفاً روبروی دوربین قرار بگیرید و کلید "Space" را فشار دهید.')
    face_image_path = None
    while True:
        ret, frame = cap.read()
        if not ret:
            print_fa('خطا در دریافت تصویر از دوربین!')
            break
        cv2.imshow('دوربین - برای ثبت تصویر Space را بزنید', frame)
        key = cv2.waitKey(1)
        if key == 32:  # Space
            # تشخیص چهره
            rgb_frame = frame[:, :, ::-1]
            faces = face_recognition.face_locations(rgb_frame)
            if len(faces) == 0:
                print_fa('هیچ چهره‌ای شناسایی نشد. دوباره تلاش کنید.')
                continue
            # ذخیره تصویر
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            face_image_path = os.path.join(save_dir, f'face_{timestamp}.jpg')
            cv2.imwrite(face_image_path, frame)
            print_fa(f'تصویر چهره ذخیره شد: {face_image_path}')
            break
        elif key == 27:  # ESC
            print_fa('لغو شد.')
            break
    cap.release()
    cv2.destroyAllWindows()
    return face_image_path
