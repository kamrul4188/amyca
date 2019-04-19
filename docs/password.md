# password

- Module Name : password
- This is module is to create plain text password to hash to storage.

## Password
```python
Password(self, /, *args, **kwargs)
```
class for password
### MINIMUM_LENGTH
int([x]) -> integer
int(x, base=10) -> integer

Convert a number or string to an integer, or return 0 if no arguments
are given.  If x is a number, return x.__int__().  For floating point
numbers, this truncates towards zero.

If x is not a number or if base is given, then x must be a string,
bytes, or bytearray instance representing an integer literal in the
given base.  The literal can be preceded by '+' or '-' and be surrounded
by whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.
Base 0 means to interpret the base from the string as an integer literal.
>>> int('0b100', base=0)
4
### check_minimum_length
```python
Password.check_minimum_length(password)
```

This function is to check password length. set minimum length is 6.
:param password: password that check length
:return: True if is minimum length 6.

### hash
```python
Password.hash(password)
```

This function is to generate hash of provided password by apply sha hash algorithm.
:param password: password is to generate hash .
:return: password hash.

### verify
```python
Password.verify(stored_password, provided_password)
```

This function is to verify a password with password stored
:param stored_password: the password is stored
:param provided_password: password is to verify
:return: bool

