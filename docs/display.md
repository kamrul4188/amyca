# display

- Module Name : display
- This module is created to POP-UP display in GUI

## GreetingScreen
```python
GreetingScreen(self)
```
This class is to create greeting pop-up screen to display greeting message
### start
```python
GreetingScreen.start(self)
```

This is function to start mainloop of greeting window.
:return: True

### stop
```python
GreetingScreen.stop(self)
```

This function is to kill greeting window
:return: GUI window destroy

## MessageScreen
```python
MessageScreen(self, title, message)
```
This class is to create a pop-up GUI screen to display message
### update_message_area
```python
MessageScreen.update_message_area(self, message)
```

This function is to update message area on message screen.
:param message: message to display

### start
```python
MessageScreen.start(self)
```

This function is to call mainloop method to stat gui window.
:return: mainloop()

