import socket
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_credentials = ('127.0.0.1', 10000)
print >>sys.stderr, "Starting server on %s and port %s" % server_credentials
sock.bind(server_credentials)

sock.listen(1)

while True:
	print >>sys.stderr, "Waiting for connection"
	connection, client_adress = sock.accept()
	try:
		print >>sys.stderr, "Connection from ", client_adress
		while True:
			data = connection.recv(64)
			print >>sys.stderr, "Received: ", data
			if data:
				connection.sendall(data)
			else:
				break
	finally:
		connection.close()