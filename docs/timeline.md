# timeline

- Module Name: timeline
- This module is to crate timeline object

## TimeLine
```python
TimeLine(self, description, status, start_date, end_date)
```
This class is to add Timeline object
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
### get_as_string
```python
TimeLine.get_as_string(self)
```

This function to get timeline object as string.
Suitable to display into gui.
:return: timeline object as string

### as_csv
```python
TimeLine.as_csv(self)
```

This function is to get timeline object as csv format
:return: as csv

### format_to_datetime
```python
TimeLine.format_to_datetime(self, date)
```

This function is to convert input date into datetime format.
:param date: input date
:return: datetime

### datetime_to_print_format
```python
TimeLine.datetime_to_print_format(self, date)
```

This function in to convert date into printable format from datetime format.
:param date:
:return:

### duration_datetime
```python
TimeLine.duration_datetime(self, start_date, end_date)
```

This function is to get duration between two days
:param start_date: stating date
:param end_date: end date
:return: duration

### due_to_start
```python
TimeLine.due_to_start(self, date)
```

This function is to get duration of date from today.
:param date: input date
:return: duration from today

### due_to_end
```python
TimeLine.due_to_end(self, date)
```

This function is to get duration form today
:param date: input date
:return: duration from today

### get_start_date
```python
TimeLine.get_start_date(self)
```

This function is get starting date of timeline object.
:return: date

### get_end_date
```python
TimeLine.get_end_date(self)
```

This function is to get end date of timeline object.
:return: date.

### get_duration
```python
TimeLine.get_duration(self)
```

This function is to get duration of timeline object between stat date and end date.
:return: duration.

