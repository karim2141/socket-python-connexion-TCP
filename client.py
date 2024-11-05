import socket 
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(("127.0.0.1",50000))
request="hi server , i went to know the time now please :"
request=request.encode(("UTF-8"))
client.send(request)
time=client.recv(1024)
time.decode("UTF-8")
print(time)
client.close()