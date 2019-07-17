import socket
import time
import select

"""
https://www.binarytides.com/programming-udp-sockets-in-python/
https://docs.python.org/3/howto/sockets.html
https://stackoverflow.com/questions/18743962/python-send-udp-packet


advice on the case of blocking sockets / socket read

https://stackoverflow.com/questions/2719017/how-to-set-timeout-on-pythons-socket-recv-method


"""

def test_2():
	IP = "XX.XX.XX.XX"	
	port = 8000 #2390

	#sock.bind(('',port))
	while time.time() <time.time()+1:    
		#print('debug 1')
		sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		#print('debug 2')
		sock.sendto(bytes('give_me_my_data',"utf-8"), (IP, port))

		#print('debug 3')
		sock.setblocking(0)
		ready = select.select([sock], [], [], 0.5)
		if ready[0]:
			b = sock.recvfrom(120)

		#print('debug_4')
		if b!=():
			pass
		else:
			print('empty b')
		data = b[0]
		clm = "{}".format(data)
		print(clm)
		time.sleep(0.01)
		#print('debug 5')

if __name__=="__main__":
	test_2()



######
"""
references: 
https://pythontic.com/modules/socket/udp-client-server-example


localIP     = "127.0.0.1"
localPort   = 20001
bufferSize  = 1024

msgFromServer       = "Hello UDP Client"
bytesToSend         = str.encode(msgFromServer)

# Create a datagram socket
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Bind to address and ip
UDPServerSocket.bind((localIP, localPort))

print("UDP server up and listening")
# Listen for incoming datagrams
while(True):
    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
    message = bytesAddressPair[0]
    address = bytesAddressPair[1]
    clientMsg = "Message from Client:{}".format(message)
    clientIP  = "Client IP Address:{}".format(address)
    print(clientMsg)
    print(clientIP)
    # Sending a reply to client
    UDPServerSocket.sendto(bytesToSend, address)


"""
