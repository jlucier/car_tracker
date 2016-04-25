import socket               # Import socket module
import time
import urllib2, json
API_URL = 'http://54.173.46.77/'

def send_ip(name, ip_address):
	headers = {'IP': str(ip_address), 'NAME': str(name)}
	req = urllib2.Request(API_URL+'add', headers=headers)
	return json.load(urllib2.urlopen(req))

def get_ips():
	req = urllib2.Request(API_URL+'get')
	return json.load(urllib2.urlopen(req))

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
print host
port = 12501               # Reserve a port for your service.
s.bind((host, port))        # Bind to the port

s.listen(25)                 # Now wait for client connection.

send_ip("Alex", s.getsockname()[0])

t_end = time.time() + 60
while time.time() < t_end:

   c, addr = s.accept()     # Establish connection with client.
   print 'Got connection from', addr
   c.send('Thank you for connecting')
   msg = c.recv(4096)
   print msg

c.close()                # Close the connection
