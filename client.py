
# client program to send requests to server

import socket
import pickle
from file import files
from tree import directories
mydir = directories("main")
myfile = files("mainer")
MAX_SIZE_BYTES = 65535 # Mazimum size of a UDP datagram - 64KBytes


def client():
    c = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #UDP
    host = socket.gethostname() 
    port = 95
    x = input("Enter the IP Address of the machine: ") #asks IP of machine but not yet implemented
    y = input("Enter the username: ") #asks username of the person but not yet implemented


    while True:
        c.connect((host, port))
        print("-----------------------------------------------")
        print("Welcome to Client Server File System")
        print("-----------------------------------------------")
        print("What would operation would you like to perform?")
        print("1. Create File")
        print("2. Write to File")
        print("3. Delete File")
        print("4. Create Directory")
        print("5. Check Directory")
        print("6. Read File")
        print("7. Truncate File")
        print("8. Move")
        print("9. Move Within File")
        print("10. Memory Map")
        print("11. Exit")
        print("-----------------------------------------------")
        y = input("Enter your choice: ")

	#if user input 1 then file name and text to be written is asked and the data is send to server via pickle.dumps
	#pickle.dumps takes in a list and encodes it in a tuple and sends the data

	#Creates a File
        if int(y) == 1:
            a = input("Enter File name: ")
            d = input("Enter text to be written to file: ")
            b = [y, a, d]
            data = pickle.dumps(b)
            c.send(data) # data is sent
            addr = c.recv(MAX_SIZE_BYTES) # data is received from server.py
            datar = pickle.loads(addr) #data is decoded from server.py
            print(datar[0]) # the first item of the tuple is printed out

	#Write to a File
        if int(y) == 2:
            a = input("Enter File Name: ")
            b = int(input("Enter offset: "))
            d = input("Enter text to be written: ")
            e = [y, a, b, d]
            data = pickle.dumps(e)
            c.send(data)
            addr = c.recv(MAX_SIZE_BYTES)
            datar = pickle.loads(addr)
            print(datar[0])
            mydir.read(a) #the contents of the file entered by the user is printed out

	#Deletes a File
        if int(y) == 3:
            a = input("Enter file name: ")
            b = [y, a]
            data = pickle.dumps(b)
            c.send(data)
            addr = c.recv(MAX_SIZE_BYTES)
            datar = pickle.loads(addr)
            print(datar[0])

	#Creates a Directory
        if int(y) == 4:
            a = input("Enter directory name: ")
            b = [y, a]
            data = pickle.dumps(b)
            c.send(data)
            addr = c.recv(MAX_SIZE_BYTES)
            datar = pickle.loads(addr)
            print(datar[0])

	#Checks a Directory whether that directory is present or not
        if int(y) == 5:
            a = input("Enter directory name: ")
            b = [y, a]
            data = pickle.dumps(b)
            c.send(data)
            addr = c.recv(MAX_SIZE_BYTES)
            datar = pickle.loads(addr)
            print(datar[0])
            print(mydir.chDir(a)) #prints out the result whether the directory is present or not

	# Prints out the contents of the file that is requested
        if int(y) == 6:
            a = input("Enter file name: ")
            e = [y, a]
            data = pickle.dumps(e)
            c.send(data)
            addr = c.recv(MAX_SIZE_BYTES)
            datar = pickle.loads(addr)
            mydir.read(a)

	# Truncates or removes the contents of the file by a specific range and prints out the contents of the file
        if int(y) == 7:
            a = input("Enter file name: ")

            f = int(input("Enter maximum size till you want to truncate: "))
            d = [y, a, f]
            data = pickle.dumps(d)
            c.send(data)
            addr = c.recv(MAX_SIZE_BYTES)
            datar = pickle.loads(addr)
            print(datar[0])
            mydir.read(a)

	# Move the file to a specific directory
        if int(y) == 8:
            a = input("Enter Source File Name: ")
            d = input("Enter Destination Directory: ")
            b = [y, a, d]
            data = pickle.dumps(b)
            c.send(data)
            addr = c.recv(MAX_SIZE_BYTES)
            datar = pickle.loads(addr)
            print(datar[0])

	# Move the contents within the file
	# Not sure whether it works perfect or not
        if int(y) == 9:
            a = "Directory Names: "
            b = [y, a]
            data = pickle.dumps(b)
            c.send(data)
            addr = c.recv(MAX_SIZE_BYTES)
            datar = pickle.loads(addr)
            print(datar[0])
            print(datar[1])

	# Shows all directories created 
        if int(y) == 10:
            a = "Memory Map"
            b = [y, a]
            data = pickle.dumps(b)
            c. send(data)
            addr = c.recv(MAX_SIZE_BYTES)
            datar = pickle.loads(addr)
            print(datar[0])
            mydir.memoryMap()

	# Exists the program
        if int(y) == 11:
            a = "Exiting program...."
            b = [y, a]
            data = pickle.dumps(b)
            c.send(data)
            addr = c.recv(MAX_SIZE_BYTES)
            datar = pickle.loads(addr)
            print("Exiting program by {}".format(host)) # prints out from which hostname was the client was closed
            print(datar[0])
            break

    c.close() #closes the connection


if __name__ == '__main__':
    client()
