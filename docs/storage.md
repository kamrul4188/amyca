# storage

- Module Name : storage
- This module is to mange storage data to hard disk to back up.

## StorageManager
```python
StorageManager(self, file_path)
```
this class used to read data from the data file and write data back to the data file.
### load_tasks
```python
StorageManager.load_tasks(self)
```

This function is to lead task list date from storage.
:return: task object list.

### load_deadline
```python
StorageManager.load_deadline(self)
```

This function is to load deadline object data form storage.
:return: deadline object list.

### load_resource
```python
StorageManager.load_resource(self)
```

This function is to load resource object date form storage.
:return: resource object list.

### load_cost
```python
StorageManager.load_cost(self)
```

This function is to load cost object data from storage.
:return: cost object list.

### save_data
```python
StorageManager.save_data(self, data)
```

This function is to store data into storage.
:param data: data to be storage.
:return: confirmation

