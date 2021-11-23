import socket
import random
    
host="127.0.0.7"
port=1337
s=socket.socket()
s.bind((host,port))
s.listen()
s_client,adresse=s.accept()
s_client.send("Veuillez entrer le nombre maximum voulu:\n".encode())
data=s_client.recv(512)
print(data.decode())
nbr_max=random.randint(1,int(data))
print("le nombre à trouver est:", nbr_max)
s_client.send(str(nbr_max).encode())
nbr_u=0
c=0

while(nbr_u != nbr_max):
    s_client.send("Entrez un nombre".encode())
    nbr_u=int(s_client.recv(512))
    c=c+1
    
    if(nbr_u>nbr_max):
        s_client.send("moins".encode())
        data=s_client.recv(512)
        print(data.decode())
        
    elif(nbr_u<nbr_max):
        s_client.send("plus".encode())
        data=s_client.recv(512)
        print(data.decode())
        
s_client.send("win".encode())
s_client.close()
s.close()
