# File-Management-System
A Basic File Management System made in Python without system calls.
This File System contains two files client.py and server.py.
Supports mutual exclusion of file access through multiple threads. Only one user is able to edit a file at a time.
Solves race condition problem by making sure that the file when chosen to be read cannot be written.
A user cannot access more than 5 files at a time, if he does he will have to wait, giving access to other users.
Client.py: 
      The main UI available to the user to choose options. Sends requests to Server.py to perform operations. 
      Gives error when server is not available.
      Ability to run on different machine.
      Bind on port 95.
Server.py:
      Receives requests from Client.py and establishes the connection and performs the operation and returns the result.
      Able to respond multiple requests at the same time by multi threads.
      Ability to run on different machine.
      Bind on port 95.
Following are the functionalities provided by it:
1) Creating a new file.
2) Deleting a file.
3) Creating a directory.
4) Checking Direcory if it exists.
5) Moving the file from one directory to another.
6) Writing contents to file.
7) Reading contents of file by either reading the whole file or reading specific contents.
8) Move contents within file.
9) Truncates contents of the file.
10) Showing memory map i.e directory structure.
