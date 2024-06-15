from PIL import Image, ImageDraw, ImageFont, ImageEnhance
import datetime as dt
import qrcode
import requests

def send_diag_results(tone_result):
    server_url = 'https://colorlog.site/api/api/user/user_upload'

    image_path = '/home/colorlog/Capstone-project/results/photo_0.jpg'
    palette_path = '/home/colorlog/Capstone-project/results/palette.jpg'
    palette_path = '/home/colorlog/Capstone-project/results/palette.jpg'

    if tone_result == 'spr':
        tone_result = '봄 웜톤'
    elif tone_result == 'sum':
        tone_result = '여름 쿨톤'
    elif tone_result == 'fal':
        tone_result = '가을 웜톤'
    elif tone_result == 'win':
        tone_result = '겨울 쿨톤'

    data = {'result': tone_result}
    files = {'resultImage': open(image_path, 'rb'), 'facePalette': open(palette_path, 'rb')}

    try:
        response = requests.post(server_url, data=data, files=files)
        if response.status_code == 200:

            print("사용자 데이터가 성공적으로 처리되었습니다.")
            print('사진 그룹이 성공적으로 업로드되었습니다.')
        else:
            print("사용자 데이터 처리에 실패했습니다. 상태 코드:", response.status_code)
            
    except Exception as e:
	    print("사용자 데이터 처리 중 오류 발생:", str(e))


def increase_brightness(image, value):
	factor = 1 + value / 255
	return ImageEnhance.Brightness(image).enhance(factor)


def insert_frame(result):
    t_img1 = Image.open("/home/colorlog/Capstone-project/results/photo_1.jpg")
    t_img2 = Image.open("/home/colorlog/Capstone-project/results/photo_2.jpg")
    t_img3 = Image.open("/home/colorlog/Capstone-project/results/photo_3.jpg")
    t_img4 = Image.open("/home/colorlog/Capstone-project/results/photo_4.jpg")

    crop_width = 582
    crop_height = 325

    # 원본 이미지의 크기를 구합니다.
    original_width, original_height = t_img1.size

    center_x = original_width // 2
    center_y = original_height // 2

    # 가운데를 기준으로 이미지를 자릅니다.
    left = int(center_x - crop_width // 2)
    top = int(center_y - crop_height // 1.8)
    right = int(center_x + crop_width // 2)
    bottom = int(center_y + crop_height // 2.25)

    img1 = t_img1.crop((left, top, right, bottom))
    img2 = t_img2.crop((left, top, right, bottom))
    img3 = t_img3.crop((left, top, right, bottom))
    img4 = t_img4.crop((left, top, right, bottom))

    img_size = (600, 425)

    img1 = increase_brightness(img1, 20)
    img2 = increase_brightness(img2, 20)
    img3 = increase_brightness(img3, 20)
    img4 = increase_brightness(img4, 20)

    img1 = img1.resize(img_size)
    img2 = img2.resize(img_size)
    img3 = img3.resize(img_size)
    img4 = img4.resize(img_size)

    if(result == 'spr1'):
        frame_color = '#F8E0EC'
    elif(result == 'spr2'):
        frame_color = '#FFE300'
    elif(result == 'spr3'):
        frame_color = '#05AC00'
        
    elif(result == 'sum1'):
        frame_color = '#E0F2F7'
    elif(result == 'sum2'):
        frame_color = '#EDFAD5'
    elif(result == 'sum3'):
        frame_color = '#9C89C8'
        
    elif(result == 'fal1'):
        frame_color = '#81543F'
    elif(result == 'fal2'):
        frame_color = '#7F9E58'
    elif(result == 'fal3'):
        frame_color = '#CA5C3E'
        
    elif(result == 'win1'):
        frame_color = '#0122AC'
    elif(result == 'win2'):
        frame_color = '#D62EE4'
    elif(result == 'win3'):
        frame_color = '#000000'

    new_img = Image.new("RGB", (1500, 1000), frame_color)
    new_img.paste(img1, (50,50))
    new_img.paste(img2, (img_size[0] + 100, 50))
    new_img.paste(img3, (50, img_size[1] + 100))
    new_img.paste(img4, (img_size[0] + 100, img_size[1] + 100))

    #watermark
    waterFont = ImageFont.truetype('/home/colorlog/Capstone-project/media/Freesentation-7Bold.ttf', 60)
    mark_width, mark_height = waterFont.getsize('Colorlog')
    watermark = Image.new('RGBA', (mark_width, mark_height), (0, 0, 0, 0))
    waterdraw = ImageDraw.Draw(watermark)
    waterdraw.text((0,0), 'Colorlog', fill='#F8F5F8', font=waterFont)
    watermark = watermark.rotate(90,expand=1)

    new_img.paste(watermark, ((img_size[0]*2) + 100 + 10, 1000 - 50 - 10 - 10 - mark_width), watermark)

    #datestr
    time = dt.datetime.now()
    datestr = time.strftime('%Y/%m/%d')
    dateFont = ImageFont.truetype('/home/colorlog/Capstone-project/media/Freesentation-7Bold.ttf', 30)
    date_width, date_height = dateFont.getsize(datestr)
    datemark = Image.new('RGBA', (date_width, date_height), (0, 0, 0, 0))
    datedraw = ImageDraw.Draw(datemark)
    datedraw.text((0,0), datestr, fill='black', font=dateFont)
    datemark = datemark.rotate(90,expand=1)

    new_img.paste(datemark, ((img_size[0]*2) + 100 + 10 + mark_height + 10, 1000 - 50 - 10 - 10 - date_width), datemark)
    new_img.save("/home/colorlog/Capstone-project/results/merged_img.jpg","JPEG")


def send_frame():
    # 스프링 서버의 엔드포인트 URL
    server_url = 'https://colorlog.site/api/api/photogroup/photogroup_upload'

    image_path = '/home/colorlog/Capstone-project/results/merged_img.jpg'
    video_path = '/home/colorlog/Capstone-project/results/output.avi'

    try:
        # 파일들을 전송할 딕셔너리
        files = {
            'video': open(video_path, 'rb'), # 동영상 파일 전송
            'image': open(image_path, 'rb'),  # 이미지 파일 전송
        }

        # POST 요청 보내기
        response = requests.post(server_url, files=files)

        # 응답 확인
        if response.status_code == 200:
            print('Photo group uploaded successfully.')
        else:
            print(f'Failed to upload photo group. Status code: {response.status_code}')
    except Exception as e:
        print('Error uploading photo group:', str(e))


def insert_qr():
    spring_server_url = "https://colorlog.site/api/api/user/qr-code"
    
    img = Image.open("/home/colorlog/Capstone-project/results/merged_img.jpg")
    img_size = (600, 425)

    try:
        # 스프링 서버로 GET 요청 보내기
        response = requests.get(spring_server_url)

        # 응답 확인
        if response.status_code == 200:
            # 링크를 가져옴
            qr_code_link = response.json()["link"]

            # QR 코드 생성
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_H,
                box_size=1,
                border=1,
            )
            qr.add_data(qr_code_link)
            qr.make(fit=True)

            # QR 코드 이미지 저장
            qr_img = qr.make_image(fill_color="black", back_color="white")
            qr_img.save("/home/colorlog/Capstone-project/results/QRCodeImg.png")
            print("QR 코드 생성 완료")
        else:
            print("Failed to get link from Spring server. Status code:", response.status_code)
    except Exception as e:
        print("Error getting link from Spring server:", str(e))

    qr_img = Image.open("/home/colorlog/Capstone-project/results/QRCodeImg.png")
    qr_img = qr_img.resize((130,130))
    img.paste(qr_img, ((img_size[0]*2) + 100 + 10, 230 - 50 - 130))
    
    img.save("/home/colorlog/Capstone-project/results/qr_img.jpg","JPEG")
    
