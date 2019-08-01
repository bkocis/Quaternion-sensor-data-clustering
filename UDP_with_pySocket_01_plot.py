import socket
import time
import select

"""
https://www.binarytides.com/programming-udp-sockets-in-python/
https://docs.python.org/3/howto/sockets.html
https://stackoverflow.com/questions/18743962/python-send-udp-packet


good advice on the case of blocking sockets / socket read

https://stackoverflow.com/questions/2719017/how-to-set-timeout-on-pythons-socket-recv-method


"""
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def sigmoid(x):
	return 1/(1+np.e**(-x))


def plot_2d(ax,dws,x,y,z):
	ax[0].plot(x,y,'ro', ms=10,alpha=0.3)
	ax[1].plot(x,z,'bo')
	ax[2].plot(z,y,'go')

	# plotting / showing clf is needed to clear the plot -latency issue
	#	plt.pause( sp )
	#	plt.show() 
#	plt.draw()
	plt.pause( sp )
	#plt.clf()
	#fig.canvas.draw()
	fig.canvas.renderer.clear()
	
#	ax[0].set_xlim(x[-dws],x[-1])

def plot_3d(x,y,z):
	ax = fig.add_subplot(111, projection='3d')
	ax.scatter(x, y, z)#, c=c, marker=m)
	plt.pause( sp )
	#plt.clf()
	#fig.canvas.draw()
	fig.canvas.renderer.clear()


def plot_X_gyro_axis_mod1(c, dws, sp, x,y,z ):
	while 1:
		c+=1
		d = ser.readline().decode().strip()
		print(d)

		# formatting the data string 
		d = d.split()[1:6:2]
		d = np.array(d, dtype=float)

		x = np.append(x,c)
		y = np.append(y,d[0])
		x = x[-dws:]
		y = y[-dws:]

		#plt.xlim(x[-dws],x[-1])
		plt.xlim([0,360])
		plt.ylim([0,360])
		plot_2d(x,y)

def plot_X_gyro_axis_mod2(c, dws, sp, x,y,z ):
	while 1:
		c+=1
		d = ser.readline().decode().strip()
		print(d)

		# formatting the data string 
		d = d.split()[1:6:2]
		d = np.array(d, dtype=float)

		x = np.append(x,c)
		y = np.append(y,d[0])
		x = x[-dws:]
		y = y[-dws:]

		#plt.xlim(x[-dws],x[-1])
#		plt.xlim([0,360])
#		plt.ylim([0,360])
		plot_2d(x,y)

def plot_X_gyro_axis_mod3(c, dws, sp, x,y,z ):
	while 1:
		c+=1
		d = ser.readline().decode().strip()
		print(d)

		# formatting the data string 
		d = d.split()[1:6:2]
		d = np.array(d, dtype=float)

		x = np.append(x,c)
		y = np.append(y,d[0])
		x = x[-dws:]
		y = y[-dws:]

		plt.xlim(x[-dws],x[-1])
		plot_2d(x,y)

def plot_XY_gyro_axis_mod1(c, dws, sp, x,y,z ):
	while 1:
		c+=1
		d = ser.readline().decode().strip()
		print(d)

		# formatting the data string 
		d = d.split()[1:6:2]
		d = np.array(d, dtype=float)

		#x = np.append(x,c)
		x = np.append(x,d[1])
		y = np.append(y,d[0])
		x = x[-dws:]
		y = y[-dws:]

		plot_2d(x,y)

def plot_XY_gyro_axis_mod2(c, dws, sp, x,y,z ):
	while 1:
		c+=1
		d = ser.readline().decode().strip()
		print(d)

		# formatting the data string 
		d = d.split()[1:6:2]
		d = np.array(d, dtype=float)

		#x = np.append(x,c)
		x = np.append(x,d[0])
		y = np.append(y,d[1])
		#x = x[-dws:]
		#y = y[-dws:]

		plot_2d(x,y)


def plot_xyz(x,y,z):

		plt.plot(x,y,'ro--')#, ms=10, alpha=0.3)
		plt.plot(z,x,'bo--')#, ms=20, alpha= 0.1)
		plt.plot(y,z,'go--')#, ms=20, alpha=0.1)
		
		plt.xlim([-360,360])
		plt.ylim([-360,360])

		plt.draw()
		plt.pause( sp )
		plt.clf()
def plot_qx_qy_qz(qx,qy,qz):

		plt.plot(qx,qy,'ro--')#, ms=10, alpha=0.3)
		plt.plot(qz,qx,'bo--')#, ms=20, alpha= 0.1)
		plt.plot(qy,qz,'go--')#, ms=20, alpha=0.1)
		
		plt.xlim([-1.2,1.2])
		plt.ylim([-1.2,1.2])

		plt.draw()
		plt.pause( sp )
		plt.clf()

def plot_qx_qy_qz_abs(qx,qy,qz):

		plt.plot(abs(qx),abs(qy),'ro--')#, ms=10, alpha=0.3)
		plt.plot(abs(qz),abs(qx),'bo--')#, ms=20, alpha= 0.1)
		plt.plot(abs(qy),abs(qz),'go--')#, ms=20, alpha=0.1)
		
		plt.xlim([-0.2,1.2])
		plt.ylim([-0.2,1.2])

		plt.draw()
		plt.pause( sp )
		plt.clf()

def plot_qx_qy_qz_abs_2(qx,qy,qz):

		plt.plot(abs(qx),abs(qy),'ro--')#, ms=10, alpha=0.3)
		plt.plot(abs(qx),abs(qz),'r+--')#, ms=10, alpha=0.3)
		plt.plot(abs(qy),abs(qz),'bo--')#, ms=10, alpha=0.3)
		plt.plot(abs(qy),abs(qx),'b+--')#, ms=20, alpha= 0.1)
		plt.plot(abs(qz),abs(qx),'go--')#, ms=20, alpha=0.1)
		plt.plot(abs(qz),abs(qy),'g+--')#, ms=20, alpha=0.1)
		
		plt.xlim([-0.2,1.2])
		plt.ylim([-0.2,1.2])

		plt.draw()
		plt.pause( sp )
		plt.clf()

def plot_qx_qy_qz_sigmoid(qx,qy,qz):

		plt.plot(sigmoid(qx),sigmoid(qy),'ro--')#, ms=10, alpha=0.3)
		plt.plot(sigmoid(qx),sigmoid(qz),'r+--')#, ms=10, alpha=0.3)
		plt.plot(sigmoid(qy),sigmoid(qz),'bo--')#, ms=10, alpha=0.3)
		plt.plot(sigmoid(qy),sigmoid(qx),'b+--')#, ms=20, alpha= 0.1)
		plt.plot(sigmoid(qz),sigmoid(qx),'go--')#, ms=20, alpha=0.1)
		plt.plot(sigmoid(qz),sigmoid(qy),'g+--')#, ms=20, alpha=0.1)
		
		plt.xlim([0.2,0.8])
		plt.ylim([0.2,0.8])

		plt.draw()
		plt.pause( sp )
		plt.clf()

###########################################################################

def test_1(c, dws, sp, x,y,z, qx, qy, qz):
	#IP = "192.168.7.36"	# test in DA_stream
	IP = "192.168.0.113"	# on demolink
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
			b = sock.recvfrom(1024)

		data = b[0]
		#clm = "{}".format(data)
		#print(clm)
		time.sleep(0.01)
		#print('debug 5')

		t, data_x,data_y,data_z, data_qx, data_qy, data_qz, data_qw  = [float(i) for i in data.split()]
	
		labeling_2(data_qx, data_qy,data_qz)	
		
		x = np.append(x,data_x)
		y = np.append(y,data_y)
		z = np.append(z,data_z)
		qx = np.append(qx,data_qx)
		qy = np.append(qy,data_qy)
		qz = np.append(qz,data_qz)

		qx0 = 0# qx[0]
		qy0 = 0#qy[0]
		qz0 = 0#qz[0]

		x = x[-dws:]
		y = y[-dws:]
		z = z[-dws:]
		qx = qx[-dws:] - qx0
		qy = qy[-dws:] - qy0
		qz = qz[-dws:] - qz0
		
		# Euler coordinates OR  Quaternal coordinates
		# plot_xyz(x,y,z)
		# OR
		# plot_qx_qy_qz(qx,qy,qz)		
		plot_qx_qy_qz_abs(qx,qy,qz)		
		# plot_qx_qy_qz_abs_2(qx,qy,qz)		
		# plot_qx_qy_qz_sigmoid(qx,qy,qz)		



def test_2(ax,c, dws, sp, x,y,z, qx, qy, qz):
	#IP = "192.168.7.36"	# test in DA_stream
	IP = "192.168.0.113"	# on demolink
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
			b = sock.recvfrom(1024)

		#print('debug_4')
		if b!=():
			pass
		else:
			print('empty b')
		data = b[0]
		#clm = "{}".format(data)
		#print(clm)
		time.sleep(0.01)
		#print('debug 5')

		t, data_x,data_y,data_z, data_qx, data_qy, data_qz, data_qw = [float(i) for i in data.split()]
		
		x = np.append(x,data_x)
		y = np.append(y,data_y)
		z = np.append(z,data_z)
		qx = np.append(qx,data_qx)
		qy = np.append(qy,data_qy)
		qz = np.append(qz,data_qz)

		qx0 = 0# qx[0]
		qy0 = 0#qy[0]
		qz0 = 0#qz[0]

		x = x[-dws:]
		y = y[-dws:]
		z = z[-dws:]
		qx = qx[-dws:] - qx0
		qy = qy[-dws:] - qy0
		qz = qz[-dws:] - qz0

#		plot_2d(ax,dws,x,y,z)
		plot_2d(ax,dws,qx,qy,qz)


	##	return data


def test_3(c, dws, sp, x,y,z):
	#IP = "192.168.7.36"	# test in DA_stream
	IP = "192.168.0.113"	# on demolink
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
			b = sock.recvfrom(70)

		#print('debug_4')
		if b!=():
			pass
		else:
			print('empty b')
		data = b[0]
		#clm = "{}".format(data)
		#print(clm)
		time.sleep(0.01)
		#print('debug 5')

		t, data_x,data_y,data_z, data_qx, data_qy, data_qz, data_qw = [float(i) for i in data.split()]
		
		x = np.append(x,data_x)
		y = np.append(y,data_y)
		z = np.append(z,data_z)

		x = x[-dws:]
		y = y[-dws:]
		z = z[-dws:]
		plot_3d(x,y,z)


def labeling_1(qx,qy,qz):

	#plt.plot(abs(qx),abs(qy),'ro--')#, ms=10, alpha=0.3)
	##plt.plot(abs(qz),abs(qx),'bo--')#, ms=20, alpha= 0.1)
	#plt.plot(abs(qy),abs(qz),'go--')#, ms=20, alpha=0.1)

	# UL - your upper-left
	# blue qz-qx space
	# x-axis
	if 0.0<abs(qz)<0.2 and 0.5<abs(qx)<0.7 and 0.7<abs(qy)<1:
		print('Upper Left brushing')

	# UR
	#elif 0.0<abs(qz)<0.2 and 0.2<abs(qx)<0.4 and 0.8<abs(qy)<1:
	elif 0.0<abs(qz)<0.2 and 0.2<abs(qx)<0.4:
		print('Upper Right brushing')

	# LL 
	if 0.7<abs(qz)<0.9 and 0.05<abs(qx)<0.15 and 0.05<abs(qy)<0.15:
		print('Lower Left brushing')

	# LR
	#elif 0.9<abs(qz)<1 and 0.0<abs(qx)<0.1 and 0.0<abs(qy)<0.15:
	elif 0.0<abs(qx)<0.1 and 0.0<abs(qy)<0.15:
		print('Lower Right brushing')
	

	# UR - your upper-right

	# LL - your lower-left

	# LR - your lower-right 


def labeling_2(qx,qy,qz):

	# # plt.plot(abs(qx),abs(qy),'ro--')#, ms=10, alpha=0.3)
	# # plt.plot(abs(qz),abs(qx),'bo--')#, ms=20, alpha= 0.1)
	# # plt.plot(abs(qy),abs(qz),'go--')#, ms=20, alpha=0.1)

	tqx = abs(qx)
	tqy = abs(qy)
	tqz = abs(qz)

	# EAST
	# UL - your upper-left # blue qz-qx space
	if 0.0< tqz <0.2 and 0.5< tqx <0.7 and 0.7< tqy<1:
		print('Upper Left brushing')

	# UR
	#elif 0.0<abs(qz)<0.2 and 0.2<abs(qx)<0.4 and 0.8<abs(qy)<1:
	elif 0.0< tqz <0.2 and 0.2< tqx <0.4:
		print('Upper Right brushing')
	# LL 
	if 0.70< tqz <0.85 and 0.0< tqx <0.15 and 0.0< tqy <0.15:
		print('Lower Left brushing')

	# LR
	#elif 0.9<abs(qz)<1 and 0.0<abs(qx)<0.1 and 0.0<abs(qy)<0.15:
	elif 0.91< tqz <1.0 and  0.0< tqx <0.15 and 0.0< tqy <0.15:
		print('Lower Right brushing')

##
	# UR-2
	if 0.2< tqz <0.4 and 0.9< tqx <1.0 and 0.1< tqy<0.4:
		print('Upper Right 2  brushing')

	# LR-2
	#elif 0.0<abs(qz)<0.2 and 0.2<abs(qx)<0.4 and 0.8<abs(qy)<1:
	elif 0.2< tqz <0.4 and 0.2< tqx <0.4 and 0.0< tqy<0.2 :
		print('Lower Right 2  brushing')

##
##################################################################
##################################################################
##################################################################
##################################################################


if __name__=='__main__':
#	x,y,z = [float(i) for i in test_2().split()]
	# data_window_size
	dws = 40
	# speed - pause delay 
	sp = 0.005# 0.02
	x = np.zeros( dws )
	y = np.zeros( dws )
	z = np.zeros( dws )
	qx = np.zeros( dws )
	qy = np.zeros( dws )
	qz = np.zeros( dws )
	c=0
	
	#plt.ion()
	#plt.show()

	# Modus Plotie:
	# X-axis
	#plot_X_gyro_axis_mod1(c, dws, sp, x,y,z)
	#plot_X_gyro_axis_mod2(c, dws, sp, x,y,z)
	#plot_X_gyro_axis_mod3(c, dws, sp, x,y,z)

	# XY-axis
	#plot_XY_gyro_axis_mod1(c, dws, sp, x,y,z)
	#plot_XY_gyro_axis_mod2(c, dws, sp, x,y,z)

	# test_1
	plt.ion()
	test_1(c,dws,sp,x,y,z, qx, qy, qz)


	# test_2
#	fig, ax = plt.subplots(1,3)
#	test_2(ax,c,dws,sp,x,y,z,qx,qy,qz)

	#test_3 3D
#	fig = plt.figure()
#	test_3(c,dws, sp, x,y,z)

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
