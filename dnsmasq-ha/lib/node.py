'''
Connection to other peers
'''

from ipaddress import ip_address, IPv4Address, IPv6Address
from socket import AF_INET, AF_INET6, SOCK_STREAM, socket
from threading import Thread

default_address = '::'
default_port = 53678
default_timeout = 500

def ipversion (address):
	'''
	Returns address's version
	It can be either 4 for IPv4, or 6 for IPv6, or 0 if this is not a IP address
	'''
	try:
		t = type (ip_address (address))
		if t == IPv4Address:
			return (4)
		if t == IPv6Address:
			return (6)
	except ValueError:
		return (0)


class Listenner (Thread):
	'''
	Listen to incomming connections
	'''
	def __init__ (self, secret, nodes, address = default_address, port = default_port):
		'''
		secret for internode communication
		port for the TCP port
		'''
		Thread.__init__ (self)
		self.secret = secret
		self.nodes = nodes
		self.address = address
		self.port = port
		if ipversion (self.address) == 6:
			self.socket = socket (AF_INET6, SOCK_STREAM)
		elif ipversion (self.address) == 4:
			self.socket = socket (AF_INET, SOCK_STREAM)
		else:
			raise (ConnectionError ('error string for listen address %s' % (self.address)))
	
	def run (self):
		'''
		Method started by threading routine
		'''
		# TODO: manage error while openning port or address
		self.socket.bind ((self.address, self.port))
		self.socket.listen (1)
		while True:
			c, a = self.socket.accept ()
			n = Node (self.secret, adresse = a, socket = c)
			n.start ()
			self.nodes.append (n)

class Node (Thread):
	'''
	Connector another node
	'''
	def __init__ (self, secret, address = None, port = default_port, socket = None, timeout = default_timeout):
		'''
		secret for internode communication
		address for IP (v4 or v6)
		port for the TCP port
		socket is for already openned socket (typically for incomming connections)
		timeout is the maximum time to wait for a answer from a node
		'''
		Thread.__init__ (self)
		if address is None and socket is None:
			raise (ConnectionError ('error string for node with neither socket, nor address'))
		self.secret = secret
		self.address = address
		self.port = port
		self.socket = socket
		self.timeout = timeout
		raise (NotImplementedError ())
	
	def ping (self):
		'''
		“Pings” the node
		This is really usefull only to know if everything is allright, the TCP layer cares about keeping the connection alive
		'''
		raise (NotImplementedError ())
	
	def send_file (self, file_object):
		'''
		Send a file to node
		file_object must be the special File object defined in this project
		'''
		raise (NotImplementedError ())
	
	def get_state (self):
		'''
		Returns node's state
		'''
		raise (NotImplementedError ())
	
	def get_name (self):
		'''
		Returns node's name
		'''
		raise (NotImplementedError ())
	
	def run (self):
		'''
		Method started by the threading routine
		'''
		raise (NotImplementedError ())