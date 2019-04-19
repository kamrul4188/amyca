# user

- Module name: user
- This module is to create user object.

## User
```python
User(self, user_name, password, access_level)
```
This class is to create user object
### INDEX_USER_ACCESS_LEVEL
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
### INDEX_USER_NAME
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
### INDEX_USER_PASSWORD
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
### verify
```python
User.verify(name, password)
```

This function is to verify user with database.
:param name: user name
:param password: user password
:return: bool

### remove
```python
User.remove(name, password)
```

This function is to remove user from database.
:param name: user name
:param password: user password
:return: confirmation

### change_password
```python
User.change_password(name, current_password, new_password)
```

This function is to change registered user password.
:param name: usr name
:param current_password: user current password
:param new_password: user new password
:return: confirmation.

### get_total
```python
User.get_total()
```

This function is to get total registered users.
:return: total user

### get_current_user_name
```python
User.get_current_user_name()
```

This function is to get current user login / verify
:return: user name

### get_current_user_access_level
```python
User.get_current_user_access_level()
```

This function is to get current user access level
:return: user level

### get_users
```python
User.get_users()
```

This function is to get all user
:return: user list

### save_as_csv
```python
User.save_as_csv(storage)
```

This function is to save user object into storage
:param storage: path of storage
:return: confirmation

### load_form_csv
```python
User.load_form_csv(storage)
```

This function is to get/load user data from storage
:param storage: path of user data
:return: confirmation

