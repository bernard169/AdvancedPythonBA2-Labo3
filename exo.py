import socket

vinci = socket.socket ()
vinci.connect (('www.vinci.be',80))  #80 est le port
print (vinci.getsockname())
data = "GET /shit HTTP/1.0\n\n".encode()
sent = vinci.send (data)
if sent != len (data):
    print ("Envoi incomplet")
response = vinci.recv(512).decode()
print (response)
vinci.close()

