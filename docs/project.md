# project

- Module Name: project
- This is one of the core module of Amyca. This module create project object.

Project attributes store various object list are:
 1. Tasks object
 2. Resource object
 3.  Cost object
Those are key object of the project.

## Project
```python
Project(self, name)
```

### add_task
```python
Project.add_task(self, tasks)
```

This function is to add task object into project
:param tasks: task object
:return: confirmation

### add_resources
```python
Project.add_resources(self, resources)
```

This function is to add resource object into project
:param resources: resource object
:return: confirmation

### add_cost
```python
Project.add_cost(self, cost)
```

This function is to add cost object into project
:param cost: cost object
:return: confirmation

### get_name
```python
Project.get_name(self)
```

This is to call project name
:return: project name

### get_id
```python
Project.get_id(self)
```

This function is to call project ID
:return: project ID

### get_tasks
```python
Project.get_tasks(self)
```

This function is to call task object
:return: tasks list

### get_resources
```python
Project.get_resources(self)
```

This function is to call resource
:return: resources list

### get_cost
```python
Project.get_cost(self)
```

This function is to call cost
:return: cost list

### remove_task
```python
Project.remove_task(self, index)
```

This function is call to remove task object as per index entered from task list.
:param index: index of task to remove
:return: confirmation

### remove_resource
```python
Project.remove_resource(self, index)
```

This function is to call to remove resource object as per index entered from resource list.
:param index: index of resource to remove.
:return: confirmation

### remove_cost
```python
Project.remove_cost(self, index)
```

This function is to remove cost object as per idex entered form cost list.
:param index: index of cost to remove.
:return: confirmation

### get_total
```python
Project.get_total()
```

This function is to call for getting number of project object has created.
:return: total project.

