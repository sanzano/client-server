import socket
from datetime import datetime, date, time, timezone

IP_MAQ_1 = "192.168.40.128"
IP_MAQ_2 = "192.168.40.133"
IP_MAQ_3 = "192.168.40.134"
IP_MAQ_4 = "192.168.40.135"


PORT = 5051
HEADER = 64 #LENGHT DEL MENSAJE
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "DESCONECTADO"
#SERVER = "192.168.40.128" #Infosec1
#SERVER = "192.168.40.132" #Infosec2
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

def send(msg):
	message = msg.encode(FORMAT)
	msg_length = len(message)
	send_length = str(msg_length).encode(FORMAT)
	send_length += b' ' *(HEADER - len(send_length))
	client.send(send_length)
	client.send(message)
	print(client.recv(2048).decode(FORMAT))

while True:
	opcion = input("A que maquina te quieres conectar: ")
	match opcion:
		case "1":
			SERVER = IP_MAQ_1
		case "2":
			SERVER = IP_MAQ_2
		case "3":
			SERVER = IP_MAQ_3
		case "4":	
			SERVER = IP_MAQ_4
		case _:
			SERVER = socket.gethostbyname(socket.gethostname())
	ADDR = (SERVER, PORT)
	client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	client.connect(ADDR)			
	mensaje = input("Escribe aqui tu mensaje. Pon salir para terminar conexion: ")
	if mensaje == "salir":
		send(DISCONNECT_MESSAGE)
		break
	else:
		now = datetime.now().isoformat()
		print("Mensaje enviado el " + now)
		send(mensaje + " Hora: " + now)
		


