"""This module is for create password as hash"""
import os
import binascii
import hashlib


class Password:
	MINIMUM_LENGTH = 6

	@staticmethod
	def check_minimum_length(password):
		if len(password) >= Password.MINIMUM_LENGTH:
			return True
		else:
			raise ValueError('Minimum length of pwd should be 6. ')

	@classmethod
	def hash(cls, password):
		"""Hash a pwd for storing."""
		cls.password = cls.check_minimum_length(password)
		salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
		password_hash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'), salt, 100000)
		password_hash = binascii.hexlify(password_hash)
		return (salt + password_hash).decode('ascii')

	@classmethod
	def verify(cls, stored_password, provided_password):
		"""Verify a stored pwd against one provided by user"""
		salt = stored_password[:64]
		stored_password = stored_password[64:]
		assert isinstance(salt, object)
		password_hash = hashlib.pbkdf2_hmac('sha512', provided_password.encode('utf-8'), salt.encode('ascii'), 100000)
		password_hash = binascii.hexlify(password_hash).decode('ascii')
		return password_hash == stored_password

