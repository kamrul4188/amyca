# Here some common python systex using into project

## Lists
* Creating List 
```python
friends = [] # an empty list
fruits = ['apple', 'banana', 'orange'] # a list containing 3 string items
values = [0, 3.4, 'High', True] # a list containing items of different types
everything = [friends, fruits, values] # a list containing other lists
```
* The code below shows how to use **del** to delete items in a list.
```python
spam = ['foo', 45.0, True]
del spam[-1] # delete last item
```
* use the **len** function to find the number of items in a list.
```python
spam = ['a','b']
print('Length is:', len(spam))
```
* use the **+** operator to combine multiple lists into a new list.
```python
girls = ['Amy', 'Betsy', 'Clara']
boys = ['Adam', 'Ben']
friends = girls + boys
```
* use the * operator to create a new list by replicating an existing list multiple times.
```python
steps = ['left', 'right']
walking = steps*3
``` 
* use **in** or **not in** to check `if` an item is in a list.
```python
valid_responses = ['Yes', 'No', 'Maybe']
response = ''
while response not in valid_responses:
  response = input('What is your response?')
print('Your response:', response)

current_drinks = ['Tea', 'Coffee']
suggested_drink = input('Suggest a new drink:')
if suggested_drink in current_drinks:
  print(suggested_drink, 'is already in the list')
```
* The **enumerate** function can help you easily maintain an iteration counter while traversing a list.
```python
pets = ['Cats', 'Dogs', 'Hamsters']
for i, animal in enumerate(pets):
  print(i+1, 'Can I buy '+ animal +'?')
```
## Methods
> Methords is a function on object. when apply methon on object, the original object not change but it's return new object
`<object>.<methord>`
### List Methods
| Method | Description |
|-------------|-------------------|
| `index()` |	finds the index of an item in a list |
| `append()` | adds an item to the end of the list |
| `insert()` | inserts an item to a specific position in the list |
| `remove()` | removes the specified item from the list |
|`sort()`	| sorts items in the list |
