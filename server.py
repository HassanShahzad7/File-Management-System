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
# Mazimum size of a UDP datagram - 64Kbytes
MAX_SIZE_BYTES = 65535 

def serverprog():
    # gets the local host name from which server program is initiaited
    host = socket.gethostname() 
    # binding the port to port 95
    port = 95 
    # UDP
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
    # binding hostname and port number
    s.bind((host, port)) 
    # count initialized to 0 will be incremented when a new user is registered but not yet implemented
    count = 0

    while True:
        #receives data from client.py
        clientsocket, address = s.recvfrom(MAX_SIZE_BYTES) 
        print("Connection from " + str(address) + " has been established.")
        # decodes data from client
        data = pickle.loads(clientsocket) 
         #increments counter by 1; whenever a new connection is established
        count += 1
        print('The client at {} says {!r}'.format(address, data[0]))
        print(data)
        
        # checks for the data entered by the user and performs function on it
        
        # creates file 
        if data[0] == '1':

            a = data[1]
            b = data[2]
            # calls addFile func from file.py and pass the data sent from client
            mydir.addFile(a, b) 
            b = "File Created!!"
            # shows the file names
            a = mydir.getFiles() 
            k = [a]
            # data encoding
            da = pickle.dumps(k) 
            #sends data to client
            s.sendto(da, address) 

        # Writes to the file
        if data[0] == '2':
            a = data[1]
            b = data[2]
            d = data[3]
            # writes to file by calling writeFile funtion in file.py
            mydir.writeFile(a, b, d) 
            print("text written")
            z = "Text written to File"
            k = [z]
            m = pickle.dumps(k)
            #sends data to client
            s.sendto(m, address) 

        # Deletes the file
        if data[0] == '3':
            a = data[1]
            mydir.delFile(a)
            c = "File Deleted"
            k = [c]
            m = pickle.dumps(k)
            #sends data to client
            s.sendto(m, address) 

        # Creates the Directory
        if data[0] == '4':
            a = data[1]
            mydir.addChildDir(a)
            a = "Directory Added"
            k = [a]
            m = pickle.dumps(k)
            #sends data to client
            s.sendto(m, address) 

        if data[0] == '5':
            a = data[1]
            b = mydir.chDir(a)
            c = "Directory Status: "
            print(b)
            k = [c, b]
            m = pickle.dumps(k)
            #sends data to client
            s.sendto(m, address) 

        if data[0] == '6':
            a = data[1]
            x = "File Contents: "
            time.sleep(3)
            mydir.read(a)
            k = [x]
            m = pickle.dumps(k)
            #sends data to client
            s.sendto(m, address) 

        if data[0] == '7':
            a = data[1]
            b = data[2]
            x = "File Truncated: "
            mydir.truncate(a, b)
            k = [x]
            m = pickle.dumps(k)
            #sends data to client
            s.sendto(m, address) 

        if data[0] == '8':
            a = data[1]
            b = data[2]
            c = "File Moved Successfully. "
            mydir.move(a, b)
            k = [c]
            m = pickle.dumps(k)
            #sends data to client
            s.sendto(m, address) 

        if data[0] == '9':
            print(data[1])
            a = "Directory List"
            k = [a]
            m = pickle.dumps(k)
            #sends data to client
            s.sendto(m, address) 

        if data[0] == '10':
            print(data[1])
            a = "Memory Map: "
            k = [a]
            m = pickle.dumps(k)
            #sends data to client
            s.sendto(m, address) 

        if data[0] == '11':
            print(data[1])
            a = "Thank you for visiting us. Hope to see you soon!"
            k = [a]
            m = pickle.dumps(k)
            #sends data to client
            s.sendto(m, address) 

        #sends data to client
        s.sendto(clientsocket, address) 


if __name__ == '__main__':
    # Creates a new thread each time server is called 
    # prevents race condition and read - write problem
    t1 = threading.Thread(target=serverprog, args=()) 
    # starts the thread
    t1.start()
    # joins the thread to previous thread
    t1.join()
