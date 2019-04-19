# deadline

- Module Name     : deadline
- Parent Module   : todo
- This module is to create deadline task object for Amyca.

## Deadline
```python
Deadline(self, description, status, by)
```
This class create deadline object
### TYPE_KEY
str(object='') -> str
str(bytes_or_buffer[, encoding[, errors]]) -> str

Create a new string object from the given object. If encoding or
errors is specified, then the object must expose a data buffer
that will be decoded using the given encoding and error handler.
Otherwise, returns the result of object.__str__() (if defined)
or repr(object).
encoding defaults to sys.getdefaultencoding().
errors defaults to 'strict'.
### as_string
```python
Deadline.as_string(self)
```

This function is to call to get printable as string of deadline object
Suitable to commandline print function.
:return: deadline as string

### get_as_string
```python
Deadline.get_as_string(self)
```

This function is to call to get string to display of deadline object.
Suitable for GUI display.
:return: deadline as string

### as_csv
```python
Deadline.as_csv(self)
```
Return the details of todo object as a list,
suitable to be stored in a csv file.

