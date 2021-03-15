import socket, platform, os, sys
from _thread import *
from datetime import datetime

#criacao socket
ServerSocket = socket.socket()
host = '127.0.0.1'
port = 1233
ThreadCount = 0
#tentativa de bind no endereço
try:
    ServerSocket.bind((host, port))
except socket.error as e:
    print(str(e))

#esperando clients
print('Waitiing for a Connection..')
ServerSocket.listen(5)

#thread client 
def threaded_client(connection):
   #envio mensagem cliente
   connection.send(str.encode('Welcome to the Servern'))
   state = True;
   listdir = ""
   file_list = ""
   system = ""
   
   #tratativas do servidor
   while state:
      data = connection.recv(2048)
      request = data.decode('utf-8')
      
      if not data:
         break
      
      elif request == "TIME":
         response = datetime.now()
         connection.sendall(str.encode(str(response.time())))
      
      elif request == "DATE":
         response = str(datetime.now().date())
         response = response.split("-")
         response_parse = response[2]+"-"+response[1]+"-"+response[0];
         connection.sendall(str.encode(response_parse))
      
      elif request == "FILES":
         count = 0;
         if platform.system() == "Windows":
            system = "C:/Windows/Temp";
         
         else:
            system = "/home/user/shared";
         
         listdir = os.listdir(system)
         
         for file in listdir:
            file_number = str(count)+" "+file+"\n";
            file_list += file_number
            count+=1
            
         connection.sendall(str.encode(file_list))
              
      elif request == "EXIT":
         connection.sendall(str.encode("Bye bye"))
         exit()
         
      elif  "DOWN" in request:
         request = str(request)
         file =  request.split(" ")[1]
         if file in file_list:
            file = system+"/"+file;  
            file_read = open(file, 'r')
            connection.sendall(str.encode(file_read.read()))
         
      else:
         connection.sendall(str.encode("I dont understand :("))   
   connection.close()

#conexao cliente e criacao da thread do cliente
while True:
    Client, address = ServerSocket.accept()
    print('Connected to: ' + address[0] + ':' + str(address[1]))
    x = start_new_thread(threaded_client, (Client, ))
ServerSocket.close()