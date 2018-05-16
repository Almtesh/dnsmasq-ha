# Inspired from https://gist.github.com/syedrakib/d71c463fc61852b8d366

from Crypto.Cipher import AES
from hashlib import sha256

padding_character = bytes ('\0', 'UTF-8')


def generate_aes_key_from_secret (secret):
	'''
	This function generates a secret for AES based on secret
	secret must be bytes
	'''
	if type (secret) != bytes:
		raise (TypeError ('secret must be bytes'))
	secret_key = sha256 (secret).digest ()
	return (secret_key)


def encrypt (message, secret):
	'''
	Encrypt a message with the secret
	secret and message must be bytes
	'''
	if type (message) != bytes:
		raise (TypeError ('message must be bytes'))
	cipher = AES.new (generate_aes_key_from_secret (secret))
	padded = message + (padding_character * ((16-len (message)) % 16))
	encrypted = cipher.encrypt (padded)
	return (encrypted)


def decrypt (message, secret):
	'''
	Decrypt message with the secret
	secret and message must be bytes
	'''
	if type (message) != bytes:
		raise (TypeError ('message must be bytes'))
	cipher = AES.new (generate_aes_key_from_secret (secret))
	decrypted = cipher.decrypt (encrypted_msg)
	unpadded = decrypted.rstrip (padding_character)
	return (unpadded)


if __name__ == '__main__':
	'''
	You can use this block as exemple
	'''
	private_msg = bytes ('Test message', 'UTF-8')
	secret = bytes ('Test secret', 'UTF-8')
	
	encrypted_msg = encrypt (private_msg, secret)
	decrypted_msg = decrypt (encrypted_msg, secret)
	
	print (decrypted_msg)