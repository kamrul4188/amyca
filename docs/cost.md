# cost

- Module Name : cost
- This module to create cost object for amyca

## Cost
```python
Cost(self, description, cost)
```
This class is to create cost object
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
Cost.get_description(self)
```

This function is to call to get details of cost object
:return: description

### get_cost
```python
Cost.get_cost(self)
```

This function is to call to get amount of cost ($) of cost object
:return: cost ($)

### as_csv
```python
Cost.as_csv(self)
```

This function is to call to get cost object as format for .csv storage
:return: cost object as csv format

