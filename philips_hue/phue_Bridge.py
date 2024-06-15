from phue import Bridge

bridge_ip = '192.168.0.73'

b = Bridge(bridge_ip)

try:
    b.connect()

    print("success")
    print(b)

except:
    print("failed")
