import socket, sys, platform

#criação socket
ClientSocket = socket.socket()
host = '127.0.0.1'
port = 1233

print('Waiting for connection')
#tentativa de conexão no socket
try:
    ClientSocket.connect((host, port))
except socket.error as e:
    print(str(e))

Response = ClientSocket.recv(1024)
system = ""
#loop para recebimento e envio de mensagens
while True:
    Input = input('Say Something: ')
    ClientSocket.send(str.encode(Input))
    Response = ClientSocket.recv(1024)
    
    #caso download para salvar o arquivo no local do client
    if "DOWN" in Input:
        #caso windows
        if platform.system() == "Windows":
            system = "C:/Windows/Temp";
        #caso linux
        else:
            system = "/home/user/shared";
            
        file = open(system+"/"+"revice_"+Input.split(" ")[1], "w+")
        file.write(Response.decode('utf-8'))
        file.close()
        print("Arquivo gravado no diretório "+ system)
        continue
        
    print(Response.decode('utf-8'))
    #caso conexao finalizada
    if Response.decode('utf-8') == "Bye bye":
        sys.exit()
    

ClientSocket.close()