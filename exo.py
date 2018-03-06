import socket
import subprocess


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

import random
import threading as th
#Exercice 4

lock = th.Lock ()
L= []

def throwDice (myList,c):
    lock.acquire ()
    myList.append (random.randint (1,6))
    lock.release ()

threads = [th.Thread (target=throwDice, args=(L,counter)) for counter in range (1,1000)]
for thread in threads:
    thread.start ()
for thread in threads:
    thread.join ()

avg = (sum (L)) / len (L)
print (avg)
