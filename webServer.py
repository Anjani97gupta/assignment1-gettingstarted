# import socket module
from socket import *
# In order to terminate the program
import sys

def webServer(port=13331):
    serverSocket = socket(AF_INET, SOCK_STREAM)

    # Prepare a server socket
    serverSocket.bind(("", 13331))


    # Fill in start
    serverSocket.listen(1)
    # Fill in end

    while True:
        # Establish the connection

        print('Ready to serve...')
        connectionSocket, addr =  serverSocket.accept() # Fill in start -are you accepting connections?     #Fill in end
        try:
            message = connectionSocket.recv(1024) # Fill in start -a client is sending you a message   #Fill in end
            filename = message.split()[1]

            # opens the client requested file.
            # Plenty of guidance online on how to open and read a file in python. How should you read it though if you plan on sending it through a socket?
            f = open(filename[1:])
            outputdata = f.read()
            f.close()
            # fill in start #fill in end)                     # fill in end

            connectionSocket.send('HTTP/1.1 200 OK\r\n'.encode())  # http OK message
            #outputdata =b"Content-Type: text/html; charset=UTF-8\r\n"
            # Fill in start -This variable can store your headers you want to send for any valid or invalid request.
            # Content-Type above is an example on how to send a header as bytes
            # Fill in end


            # Send an HTTP header line into socket for a valid request. What header should be sent for a response that is ok?
            # Note that a complete header must end with a blank line, creating the four-byte sequence "\r\n\r\n" Refer to https://w3.cs.jmu.edu/kirkpams/OpenCSF/Books/csf/html/TCPSockets.html
            # Fill in start

            # Fill in end
            # connectionSocket.send(outputdata)
            # connectionSocket.close()

            # Send the content of the requested file to the client
            for i in range(0, len(outputdata)):  # for line in file
            # Fill in start - send your html file contents #Fill in end
                connectionSocket.send(outputdata[i].encode())
            connectionSocket.send("\r\n".encode())
            connectionSocket.close()  # closing the connection socket

        except IOError:
    # Send response message for invalid request due to the file not being found (404)
    # Fill in start
            connectionSocket.send("HTTP/1.1 404 Not Found\r\n\r\n".encode())
            connectionSocket.close()
    # Fill in end

    # Close client socket
    # Fill in start

    # Fill in end

    # Commenting out the below, as its technically not required and some students have moved it erroneously in the While loop. DO NOT DO THAT OR YOURE GONNA HAVE A BAD TIME.
    serverSocket.close()
    sys.exit()  # Terminate the program after sending the corresponding data


if __name__ == "__main__":
    webServer(13331)