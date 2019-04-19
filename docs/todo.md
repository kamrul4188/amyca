# todo

- Module name : todo
- This module is to create todo object.

## ToDo
```python
ToDo(self, description, status)
```
This class to create todo object
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
### mark_as_done
```python
ToDo.mark_as_done(self)
```
This function is to set task status (True) as done
### mark_as_pending
```python
ToDo.mark_as_pending(self)
```
This function is reset task status (False) as pending
### as_string
```python
ToDo.as_string(self)
```

This is to get todo object as printable string
Suitable to commandline print.
:return: dodo obj as string

### get_status
```python
ToDo.get_status(self)
```

This function is to get status of todo object
:return: status -> True

### get_status_as_icon
```python
ToDo.get_status_as_icon(self)
```

This function is to get status icon of todo object
:return:

### get_as_string
```python
ToDo.get_as_string(self)
```

This function is to get name/details of todo object as string
:return: description

### get_str
```python
ToDo.get_str()
```

This function ist to get todo object as string
:return: as string

### as_csv
```python
ToDo.as_csv(self)
```
Return the details of todo object as a list,
suitable to be stored in a csv file.
:return: as csv

