# resource

- Module Name : resource
- This is module is to create resource object for Amyca

## Resource
```python
Resource(self, description, quantity)
```
Class to generate resource object
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
### get_description
```python
Resource.get_description(self)
```

This function is to get name/details of resources objects
:return: description

### get_quantity
```python
Resource.get_quantity(self)
```

This function is to get quantity of resource object
:return: quantity

### as_csv
```python
Resource.as_csv(self)
```

This function is to get resource object as string in csv format
Suitable to storage into .csv file
:return: obj as list

