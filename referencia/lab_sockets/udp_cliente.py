import socket
import threading
from datetime import datetime

ENCODE = "UTF-8"
HOST = '127.0.0.1'   # Endereco IP do Servidor
PORT = 5000          # Porta que o Servidor esta
MAX_BYTES = 65535    # Quantidade de Bytes a serem ser recebidos
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverDest = (HOST, PORT)

def client():
    username = registerUsername()
    while True:
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
        username = raw_input('Digite seu nome de usuario:\n')
        encodedUsername = username.encode(ENCODE)

        sock.sendto('1:' + str([username]), serverDest)

        data, address = sock.recvfrom(MAX_BYTES)
        response = data.decode(ENCODE).split(':')

        isAccepted = response[0] == '2'
        print(response[1])

    return username

def messageSender():
    message = raw_input('Digite a mensagem que voce quer enviar:\n')
    destiny = raw_input('Digite o nome do usuario receptor:\n')
    encodedData = ('3:' + str([message, destiny])).encode(ENCODE)

    sock.sendto(encodedData, serverDest)

    data, address = sock.recvfrom(MAX_BYTES)
    response = data.decode(ENCODE).split(':')

    print(response[1])

def resolveServerMessages():
    data, address = sock.recvfrom(MAX_BYTES)
    response = data.decode(ENCODE)

    print(response)

def printUserlist():

    sock.sendto('2:[]'.encode(ENCODE), serverDest)
    data, address = sock.recvfrom(MAX_BYTES)
    response = str(data.decode(ENCODE))

    userlist = eval(response.split(':')[1])
    for u in userlist:
        print(u.decode(ENCODE))

client()