import socket
import threading
from datetime import datetime, date, time, timezone

PORT = 5051
HEADER = 64 #LENGHT DEL MENSAJE
SERVER = "192.168.40.128" #InfosecB
#SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "DESCONECTADO"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
	print(f"[NUEVA CONEXION] {addr} conectado.")
	
	connected = True
	while connected:
		msg_length = conn.recv(HEADER).decode(FORMAT)
		if msg_length:	
			msg_length = int(msg_length)
			msg = conn.recv(msg_length).decode(FORMAT)  #espera a que algo llego a traves del socket
			if msg == DISCONNECT_MESSAGE:
				connected = False
			print(f"[{addr}] {msg}")
			now = datetime.now().isoformat()
			msjeRbdo = "Mensaje recibido el " + now
			conn.send(msjeRbdo.encode(FORMAT))
		
	conn.close()

def start():
	server.listen() #esperando conexiones
	print("[ESPERANDO] Servidor espera a {SERVER}")
	while True:
		conn, addr = server.accept()  #espera conexion y almacena la direccion y el objetvo socket
		thread = threading.Thread(target=handle_client, args=(conn, addr))
		thread.start()
		print(f"[CONEXIONES ACTIVAS] {threading.activeCount() - 1}")

print("Iniciando...")
start()


