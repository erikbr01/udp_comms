import socket
import json

json_msg = {}
json_msg["person"] = {"x": 1.2, "y": 1.4, "z": 1.0}
msg = json.dumps(json_msg)
byte_msg = str.encode(msg)

srv_addr = ('127.0.0.1', 2508)
buf_size = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


while True:
    s.sendto(byte_msg, srv_addr)

    res = s.recvfrom(1024)

    print('server says:' + str(res[0]))
