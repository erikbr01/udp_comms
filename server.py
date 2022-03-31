import socket
import json
import time

client_addr = ('127.0.0.1', 2508)


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(client_addr)

while True:
    d = s.recvfrom(1024)
    data = d[0]
    addr = d[1]

    j_data = json.loads(data.decode())
    print(j_data['person'])

    time.sleep(2)
    reply = str.encode(data.decode())
    s.sendto(reply, addr)

s.close()
