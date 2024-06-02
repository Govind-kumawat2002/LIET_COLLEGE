import socket

s =socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
ip_address= '192.168.147.177'
port = 8888
target= (ip_address,port)
message = input("kya msg kroge")
encript_message =message.encode('ascii')
s.sendto(encript_message,target)


# port 0 to 65536 
# ip_address = 172.20.10.8
# port = 8888
