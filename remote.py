import socket
import requests

initiateIP = '239.255.255.250'
initiatePort = '1900'
buffer_size = 1024
keyInput = ""

initiateMessage = \
    'M-SEARCH * HTTP/1.1\r\n' + \
    'Host: ' + initiateIP + ':' + initiatePort + '\r\n' + \
    'Man: "ssdp:discover"\r\n' + \
    "ST : roku:ecp\r\n\r\n"

initialMessage = initialMessage.encode('utf-8')

def sendInitiateMessage():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_socket.sendto(initiateMessage,(initiateIP,initiatePort))
    response, server_address = client_socket.recvfrom(buffer_size)
    return response.decode('utf-8')

def reconstructMessage(response):
    joinMessage = ''.join([str(elem) for elem in response])
    splitMessage = joinMessage.split('\r\n')
    return splitMessage

responseHTTP = sendInitiateMessage()
responseMessageArray = reconstructMessage(responseHTTP)
serverLocation = responseMessageArray[6][10:34]

while keyInput != "stop":
    keyInput = input("Input stop/select/left/right/up/down/back: ")
    if keyInput == "stop" or keyInput == "select" or keyInput == "left" or keyInput == "right" or keyInput == "up" or keyInput == "down" or keyInput == "back":
        requests.post(serverLocation + '/keypress/' + keyInput)
    else:
        print("INVALID INPUT")
 
print("--No Longer Listening--")



