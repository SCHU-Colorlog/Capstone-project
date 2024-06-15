# -*- coding: utf-8 -*-
import cv2

def crop_and_resize_frame(frame, crop_width, crop_height, img_size):
    original_height, original_width = frame.shape[:2]
    center_x = original_width // 2
    center_y = original_height // 2

    left = int(center_x - crop_width // 2)
    top = int(center_y - crop_height // 1.8)
    right = int(center_x + crop_width // 2)
    bottom = int(center_y + crop_height // 2.25)

    cropped_frame = frame[top:bottom, left:right]
    resized_frame = cv2.resize(cropped_frame, img_size)
    return resized_frame


def get_camera_frame():
    cap = cv2.VideoCapture(0, cv2.CAP_V4L2)
    if not cap.isOpened():
        print("카메라를 열 수 없습니다.")
        return None, None, None

    # 비디오 녹화를 위한 설정 (XVID 코덱 사용, 초당 30 프레임)
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    # fourcc = cv2.VideoWriter_fourcc(*'MJPG')
    # fourcc = cv2.VideoWriter_fourcc(*'mp4v')

    # out = cv2.VideoWriter('results/output.avi', fourcc, 30.0, (640, 480))
    out = cv2.VideoWriter('results/output.avi', fourcc, 30.0, (int(cap.get(3)), int(cap.get(4))))
    
    def frame_generator():
        while True:
            ret, frame = cap.read()
            if not ret:
                print("프레임을 받을 수 없습니다. 종료합니다.")
                break
            crop_width = 582
            crop_height = 325
            img_size = (890, 625)
            frame = crop_and_resize_frame(frame, crop_width, crop_height, img_size)
            yield frame

    return frame_generator(), cap, out


def release_camera(cap, out):
    if cap:
        cap.release()
    if out:
        out.release()
    cv2.destroyAllWindows()

