import socket
import time

SERVER_HOST = "0.0.0.0"
SERVER_PORT = 8080

serverScoket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
serverScoket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serverScoket.bind((SERVER_HOST, SERVER_PORT))
serverScoket.listen(5)

print(f"Listening on port {SERVER_PORT} ...")


while True: 
    time.sleep(1)
    clientSocket, clientAddress = serverScoket.accept()
    print(f"clientSocket - {clientSocket}, clientAddress - {clientAddress}")
    request = clientSocket.recv(1500).decode()
    header = request.split('\n')
    firstHeaderComponent = header[0].split()

    httpMethod = firstHeaderComponent[0]
    path = firstHeaderComponent[1]
    print(f"httpMethod-{httpMethod}")
    print(f"path-{path}")

    respone = ''
    if httpMethod =='GET':
        if path == '/':
            fileOpen = open("index.html")
            data = fileOpen.read()
            fileOpen.close()

            respone = 'HTTP/1.1 200 OK \n\n' + data

    else :
        respone = 'HTTP/1.1 405 method not allowed \n\nAllow Only Get Method.'

    clientSocket.sendall(respone.encode())
    clientSocket.close()