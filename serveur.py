import socket
from datetime import datetime
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(("127.0.0.1",50000))
s.listen(3)
client,addr=s.accept()
request=client.recv(1024)
request=request.decode("UTF-8")
print (addr,request)
time=str(datetime.now())
time=time.encode("UTF-8")
client.send(time)
print("done...!")
client.close()