import socket
host="127.0.0.7"
port=1337
s=socket.socket()
s.connect((host,port))
data=s.recv(512)
print(data.decode())
nbr=int(input(""))
s.send(str(nbr).encode())
reponse=s.recv(512)
data=s.recv(512)
print(data.decode())
data=s.recv(512)
print(data.decode())
rep=int(input(""))
while( True ):
    if (data != "win"):
        rep=int(input(""))
        s.send(str(rep).encode())
        data=s.recv(512)
        print(data.decode())
    else:
        print("fin de la partie")
        break
s.close()
