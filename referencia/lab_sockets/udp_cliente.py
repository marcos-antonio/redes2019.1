import socket
import threading
from datetime import datetime

ENCODE = "UTF-8"
HOST = '127.0.0.1'
PORT = 5000
MAX_BYTES = 65535
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverDest = (HOST, PORT)

def client():
    username = registerUsername()
    threading.Thread(target=resolveServerMessages).start()
    waitForCommands()

def waitForCommands():
    print('Comandos possiveis\n')
    print('1 - Enviar mensagem\n')
    print('2 - Listar usuarios\n')
    comando = raw_input('Digite o numero do comando desejado: \n')

    if comando == '1':
        messageSender()
    elif comando == '2':
        printUserlist()
    else:
        print('Comando invalido')

def registerUsername():
    isAccepted = False
    username = ''
    while isAccepted == False:
        username = str(raw_input('Digite seu nome de usuario:\n'))
        encodedUsername = username.encode(ENCODE)

        sock.sendto('1:' + str([username]), serverDest)

        data, address = sock.recvfrom(MAX_BYTES)
        response = data.decode(ENCODE).split(':')

        isAccepted = response[0] == '2'
        print(response[1])

    return username

def messageSender():
    message = str(raw_input('Digite a mensagem que voce quer enviar:\n'))
    destiny = str(raw_input('Digite o nome do usuario receptor:\n'))
    encodedData = ('3:' + str( [message, destiny])).encode(ENCODE)

    sock.sendto(encodedData, serverDest)

def resolveServerMessages():
    while True:
        data, address = sock.recvfrom(MAX_BYTES)
        response = data.decode(ENCODE).split(':')
        responseAction = response[2]
        printableResponseCodes = ['1', '3']
        userACtivatedResponseCodes = ['1', '2']

        if (responseAction in printableResponseCodes):
            print(response[1])
        elif (responseAction == '2'):
            userlist = eval(response[1])
            print('Usuarios cadastrados')
            for u in userlist:
                print(u.decode(ENCODE))
        else:
            print('Resposta do servidor nao identificada')
            waitForCommands()

        if (responseAction in userACtivatedResponseCodes):
            waitForCommands()


def printUserlist():

    sock.sendto('2:[]'.encode(ENCODE), serverDest)

client()