"""
Module Name : password
This is module is to create plain text password to hash to storage.
"""

import os
import binascii
import hashlib


class Password:
	"""class for password"""
	MINIMUM_LENGTH = 6

	@staticmethod
	def check_minimum_length(password):
		"""
		This function is to check password length. set minimum length is 6.
		:param password: password that check length
		:return: True if is minimum length 6.
		"""
		if len(password) >= Password.MINIMUM_LENGTH:
			return True
		else:
			raise ValueError('Minimum length of pwd should be 6. ')

	@classmethod
	def hash(cls, password):
		"""
		This function is to generate hash of provided password by apply sha hash algorithm.
		:param password: password is to generate hash .
		:return: password hash.
		"""
		cls.password = cls.check_minimum_length(password)
		salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
		password_hash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'), salt, 100000)
		password_hash = binascii.hexlify(password_hash)
		return (salt + password_hash).decode('ascii')

	@classmethod
	def verify(cls, stored_password, provided_password):
		"""
		This function is to verify a password with password stored
		:param stored_password: the password is stored
		:param provided_password: password is to verify
		:return: bool
		"""
		salt = stored_password[:64]
		stored_password = stored_password[64:]
		assert isinstance(salt, object)
		password_hash = hashlib.pbkdf2_hmac('sha512', provided_password.encode('utf-8'), salt.encode('ascii'), 100000)
		password_hash = binascii.hexlify(password_hash).decode('ascii')
		return password_hash == stored_password


if __name__ == '__name__':
	pass
