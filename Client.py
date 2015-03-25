import socket
import time
import threading

IP_direction = raw_input('IP direction: ')
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
user_name = raw_input('User name: ')

def command(cad):
	if cad == '/date':
		print (time.strftime("Hour: %H:%M:%S"))
		print (time.strftime("Date: %I:%M:%S"))


def main():
	try:
		while True:
			print user_name+': ',
			user_message = raw_input()
			if user_message.startswith('/'):
				command(user_message)
			else:
				if user_message.strip() == 'exit()':
					break
				else:
					sock.sendto(user_message,(IP_direction, 8881))
	finally:
		sock.close()

if __name__ == "__main__":
	main()