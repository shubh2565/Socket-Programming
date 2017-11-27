import socket
import sys

# create socket (allows two computers to connect)
def socket_create():
	try:
		global host
		global port
		global s
		host = ''
		port = 9999
		s = socket.socket()
	except socket.error as msg:
		print('Socket creation error: ' + str(msg))


# binds socket to port and wait for connection from client
def socket_bind():
	try:
		global port
		global host
		global s
		print('Binding socket to port: ' + str(port))
		s.bind((host, port))
		s.listen(5)
	except socket.error as msg:
		print('Socket binding error: ' + str(msg) + '\nRetrying...')
		socket_bind()


# establishes a connection with client (socket must be listening for them)
def socket_accept():
	conn, address = s.accept()
	print('Connection has been established |' + 'IP' + address[0] + '| Port' + str(address[1]))
	send_commands(conn)
	conn.close()


# sends commands to the client
def send_commands(conn):
	while True:
		cmd = input()
		if cmd == 'quit':
			conn.close()
			s.close()
			sys.exit()
		if len(str.encode(cmd)) > 0:
			conn.send(str.encode(cmd))
			client_response = str(conn.recv(1024), 'utf-8')
			print(client_response, end = '')


# calling different functions
def main():
	socket_create()
	socket_bind()
	socket_accept()


main()

