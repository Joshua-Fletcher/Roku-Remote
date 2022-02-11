import socket
import requests

initiateIP = '239.255.255.250'
initiatePort = '1900'
buffer_size = 1024

initiateMessage = \
    'M-SEARCH * HTTP/1.1\r\n' + \
    'Host: ' + initiateIP + ':' + initiatePort + '\r\n' + \
    'Man: "ssdp:discover"\r\n' + \
    "ST : roku:ecp\r\n\r\n"


def sendInitiateMessage():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.sendto(initiateMessage,(initiateIP,initiatePort))
    response = client_socket.recv(buffer_size)
    return response

def splitResponse(response):
    responseAfterSplit = response.split('\r\n')
    return responseAfterSplit.split()


responseHTTP = sendInitiateMessage()
parsedResponse = splitResponse(responseHTTP)
print(parsedResponse)

