#Group Members
#Hassan Shahzad


import socket
from file import files
from tree import directories
import pickle
import threading
import time
mydir = directories("main")
myfile = files("mainer")
MAX_SIZE_BYTES = 65535 # Mazimum size of a UDP datagram - 64Kbytes

def serverprog():
    host = socket.gethostname() # gets the local host name from which server program is initiaited
    port = 95 # binding the port to port 95
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
    s.bind((host, port)) # binding hostname and port number
    count = 0 # count initialized to 0 will be incremented when a new user is registered but not yet implemented

    while True:
        clientsocket, address = s.recvfrom(MAX_SIZE_BYTES) #receives data from client.py
        print("Connection from " + str(address) + " has been established.")
        data = pickle.loads(clientsocket) # decodes data from client
        count += 1 #increments counter by 1; whenever a new connection is established
        print('The client at {} says {!r}'.format(address, data[0]))
        print(data)
        
        # checks for the data entered by the user and performs function on it
        
        # creates file 
        if data[0] == '1':

            a = data[1]
            b = data[2]
            mydir.addFile(a, b) # calls addFile func from file.py and pass the data sent from client
            b = "File Created!!"
            a = mydir.getFiles() # shows the file names
            k = [a]
            da = pickle.dumps(k) # data encoding
            s.sendto(da, address) #sends data to client

        # Writes to the file
        if data[0] == '2':
            a = data[1]
            b = data[2]
            d = data[3]
            mydir.writeFile(a, b, d) # writes to file by calling writeFile funtion in file.py
            print("text written")
            z = "Text written to File"
            k = [z]
            m = pickle.dumps(k)
            s.sendto(m, address) #sends data to client

        # Deletes the file
        if data[0] == '3':
            a = data[1]
            mydir.delFile(a)
            c = "File Deleted"
            k = [c]
            m = pickle.dumps(k)
            s.sendto(m, address) #sends data to client

        # Creates the Directory
        if data[0] == '4':
            a = data[1]
            mydir.addChildDir(a)
            a = "Directory Added"
            k = [a]
            m = pickle.dumps(k)
            s.sendto(m, address) #sends data to client

        if data[0] == '5':
            a = data[1]
            b = mydir.chDir(a)
            c = "Directory Status: "
            print(b)
            k = [c, b]
            m = pickle.dumps(k)
            s.sendto(m, address) #sends data to client

        if data[0] == '6':
            a = data[1]

            x = "File Contents: "
            time.sleep(3)
            mydir.read(a)
            k = [x]
            m = pickle.dumps(k)
            s.sendto(m, address) #sends data to client

        if data[0] == '7':
            a = data[1]
            b = data[2]
            x = "File Truncated: "
            mydir.truncate(a, b)
            k = [x]
            m = pickle.dumps(k)
            s.sendto(m, address) #sends data to client

        if data[0] == '8':
            a = data[1]
            b = data[2]
            c = "File Moved Successfully. "
            mydir.move(a, b)
            k = [c]
            m = pickle.dumps(k)
            s.sendto(m, address) #sends data to client

        if data[0] == '9':
            print(data[1])
            a = "Directory List"
            k = [a]
            m = pickle.dumps(k)
            s.sendto(m, address) #sends data to client

        if data[0] == '10':
            print(data[1])
            a = "Memory Map: "
            k = [a]
            m = pickle.dumps(k)
            s.sendto(m, address) #sends data to client

        if data[0] == '11':
            print(data[1])
            a = "Thank you for visiting us. Hope to see you soon!"
            k = [a]
            m = pickle.dumps(k)
            s.sendto(m, address) #sends data to client

        s.sendto(clientsocket, address) #sends data to client


if __name__ == '__main__':
    # Creates a new thread each time server is called 
    # prevents race condition and read - write problem
    t1 = threading.Thread(target=serverprog, args=()) 
    # starts the thread
    t1.start()
    # joins the thread to previous thread
    t1.join()
