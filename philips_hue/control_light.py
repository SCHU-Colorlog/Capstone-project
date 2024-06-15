from phue import Bridge
import time


bridge_ip = '192.168.0.73'
b = Bridge(bridge_ip)


b.connect()


light_names = ['colorlog-더블팩', 'colorlog-더블팩2']


color_settings = {
    '봄웜': {'hue': 56000, 'sat': 80, 'bri': 200},
    '여름쿨': {'hue': 46920, 'sat': 180, 'bri': 200},
    '가을웜': {'hue': 6500, 'sat': 180, 'bri': 200},
    '겨울쿨': {'hue': 51000, 'sat': 254, 'bri': 200}
}


def set_color_tone(tone):
    settings = color_settings.get(tone)
    if settings:
        for light_name in light_names:
            light = b.get_light_objects('name')[light_name]
            if not light.on:
                light.on = True
                time.sleep(1)  
            light.hue = settings['hue']
            light.saturation = settings['sat']
            light.brightness = settings['bri']
        
        print(f"{tone} 색상으로 모든 조명이 설정되었습니다.")
    else:
        print("올바른 색조를 입력하세요: '봄웜', '여름쿨', '가을웜', '겨울쿨'")


while True:
    user_input = input("색조를 입력하세요 ('봄웜', '여름쿨', '가을웜', '겨울쿨', '종료'로 종료): ")
    if user_input == "종료":
        
        for light_name in light_names:
            light = b.get_light_objects('name')[light_name]
            light.on = False
        print("모든 조명이 꺼졌습니다. 프로그램을 종료합니다.")
        break
    else:
        set_color_tone(user_input)
