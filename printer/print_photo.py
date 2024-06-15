import os
import time
import subprocess
import threading

# 프린터 IP 주소 설정 (예: 192.168.1.100)
printer_ip = "192.168.0.88"
# printer_ip = 'EPSON_L6170_Series'

# 출력할 이미지 경로 설정 (예: /home/jetson/image.jpg)
image_path = "/home/colorlog/Capstone-project/results/qr_img.jpg"

# 커맨드 실행 함수
def run_command(command):
    subprocess.call(command, shell=True)

# 이미지 출력 함수
def print_image():
    # 이미지를 CUPS 프린터 큐에 추가
    run_command(f"lp -o media=Custom.4x6in -o scaling=fit-page -o media=GlossyPhotoPaper -o job-name='10x15cm_Photo' {image_path}")

    # 프린터 재시작 (필요한 경우)
    run_command(f"ping {printer_ip} -c 1 > /dev/null && echo && lpadmin -p {printer_ip} -E")

    # 프린트 작업 진행 확인
    while True:
        status = run_command(f"lpq -P {printer_ip} | grep 'completed'")
        if status:
            print("프린트 작업 완료")
            break
        else:
            print("프린트 작업 진행 중...")
            time.sleep(5)

# 비동기로 프린트 작업을 실행하는 함수
def print_image_async():
    threading.Thread(target=print_image).start()

