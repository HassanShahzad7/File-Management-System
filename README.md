# File-Management-System
A Basic File Management System made in Python *without system calls*.
* This File System contains two files client.py and server.py.
* Supports mutual exclusion of file access through multiple threads. Only one user is able to edit a file at a time.
* Solves *race condition problem* by making sure that the file when chosen to be read cannot be written.


### Client.py: 
      The main UI available to the user to choose options. Sends requests to Server.py to perform operations. 
      Gives error when server is not available.
      Ability to run on different machine.
      Bind on port 95.
### Server.py:
      Receives requests from Client.py and establishes the connection and performs the operation and returns the result.
      Able to respond multiple requests at the same time by multi threads.
      Ability to run on different machine.
      Bind on port 95.

### Functionalties
Following are the functionalities provided by it:
* Creating a new file.
* Deleting a file.
* Creating a directory.
* Checking Direcory if it exists.
* Moving the file from one directory to another.
* Writing contents to file.
* Reading contents of file by either reading the whole file or reading specific contents.
* Move contents within file.
* Truncates contents of the file.
* Showing memory map i.e directory structure.
