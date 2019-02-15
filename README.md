# TE3201-Software-Engineering Project Monty

### [Full Project Details is here](https://nus-te3201.github.io/2019/admin/te3201-admin.html#project)

## Basic Functionality:

1. Monty interface can be text-based (i.e., no need for a graphical UI)
2. Monty helps with storing and retrieving at least one type of data that is useful to the user. Some examples of different types of data (you can pick one or more of them): details of contacts, todo items, appointments, deadlines, reminders, technical terms to remember, etc. Here is an example interaction between a user and a Monty that deals with TODO items:

      ```Hi, I'm Monty. How can I help you?

      add Return library book
      >>> TODO added: Return library book

      list
      >>> Here are the list of TODOs you have:
      1. Return library book
      2. Do TE3201 exercises
      3. Call back Jina

      delete 2
      >>> TODO deleted: Do TE3201 exercises

      are you single?
      >>> Sorry. I did not understand your request.

      help
      >>> Here are the requests I understand.
      add {TODO description} : adds a TODO to the list
      list : lists all TODOs
      ...
      ```
3. There is no need for Monty to be able to understand natural language sentences. It is fine for the user requests to need to follow a strict format. Defining the request format is part of the project. The example interaction given above is just an example only. Hint: try to design a request format that is easy to remember and type.

4.  Monty should support adding, deleting, listing, searching (by keyword) of data items.
5.  Persistence: The data should be stored in the hard disk so that restarting Monty should not cause a loss of data entered in a previous session.
  5.1 The data files should be in a human-readable format such as .csv (recommended), xml, json, plain text, etc.

## Additional Functionality:

### Some suggestions for additional functionality:

* More attributes for data items e.g., priorities, tags, birthdays
* Multiple data item types e.g., support saving TODOs, appointments, and deadlines
** Support connections between data items e.g., ability to assign a TODO to a contact
* Multi-user support e.g., assume the software is installed in a common computer in your office and allow multiple users to interact with it
* More ways to query data e.g., find contacts that has a birthday in next 2 days, find all TODOs with high priority, etc.
* Any other feature (get approval from prof before implementing)
