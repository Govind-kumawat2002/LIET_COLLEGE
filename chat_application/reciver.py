import socket

s =socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
ip_addrss= '172.20.10.8'
port = 888
target=(ip_addrss,port)
s.bind(target)
while True:
    message = s.recvfrom(120)
    print(message)
    data = message[0]
    data = '\n'
    print(data.encode('ascii'))
# except Exception as e:
    # print("hello sir mene msg recive kr liya hai ")
