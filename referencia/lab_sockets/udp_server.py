import socket
from datetime import datetime

ENCODE = "UTF-8"
MAX_BYTES = 65535
PORT = 5000
HOST = ''
userlist = {}
orig = (HOST, PORT)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(orig)

def server():
    while True:
        data, address = sock.recvfrom(MAX_BYTES)
        data = data.decode(ENCODE).split(':')
        text = ''
        code = 5
        action = data[0]
        data = eval(data[1])


        if (action == '1'):
            if registerUser(data[0], address) == True:
                text = 'Usuario cadastrado com sucesso'
                code = 2
            else:
                code = 4
                text = 'Usuario ja cadastrado'
        elif (action == '2'):
            code = 2
            text = str(list(userlist.keys()))
        elif (action == '3'):
            if sendMessage(data[0], data[1]) == True:
                code = 2
                text = 'Mensagem enviada'
            else:
                code = 4
                text = 'Usuario nao encontrado'
        text = (str(code) + ':' + text).encode(ENCODE)
        sock.sendto(text, address)


def registerUser(username, data):
    if userlist.get(username) == None:
        userlist[username] = data
        return True
    else:
        return False

def sendMessage(message, destiny):
    destinyAddress = userlist.get(destiny)
    if destinyAddress == None:
        return False
    else:
        message = ('2:' + message).encode(ENCODE)
        sock.sendto(message, destinyAddress)
        return True

server()