import socket

s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)


s.connect((socket.gethostname(),1100))

full_msg =''
while True:
    msg = s.recv(100)
    if len(msg)<=0:
        break
    full_msg+=msg.decode('utf-8')

    #print(msg.decode('utf-8'))

print(full_msg)
