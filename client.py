#Group Members
#Hassan Shahzad


import socket
import pickle
from file import files
from tree import directories
mydir = directories("main")
myfile = files("mainer")
MAX_SIZE_BYTES = 65535 # Mazimum size of a UDP datagram


def client():
    c = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    host = socket.gethostname()
    port = 95
    x = input("Enter the IP Address of the machine: ")
    y = input("Enter the username: ")


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

        if int(y) == 1:
            a = input("Enter File name: ")
            d = input("Enter text to be written to file: ")
            b = [y, a, d]
            data = pickle.dumps(b)
            c.send(data)
            addr = c.recv(MAX_SIZE_BYTES)
            datar = pickle.loads(addr)
            print(datar[0])

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
            mydir.read(a)

        if int(y) == 3:
            a = input("Enter file name: ")
            b = [y, a]
            data = pickle.dumps(b)
            c.send(data)
            addr = c.recv(MAX_SIZE_BYTES)
            datar = pickle.loads(addr)
            print(datar[0])

        if int(y) == 4:
            a = input("Enter directory name: ")
            b = [y, a]
            data = pickle.dumps(b)
            c.send(data)
            addr = c.recv(MAX_SIZE_BYTES)
            datar = pickle.loads(addr)
            print(datar[0])

        if int(y) == 5:
            a = input("Enter directory name: ")
            b = [y, a]
            data = pickle.dumps(b)
            c.send(data)
            addr = c.recv(MAX_SIZE_BYTES)
            datar = pickle.loads(addr)
            print(datar[0])
            print(mydir.chDir(a))

        if int(y) == 6:
            a = input("Enter file name: ")
            e = [y, a]
            data = pickle.dumps(e)
            c.send(data)
            addr = c.recv(MAX_SIZE_BYTES)
            datar = pickle.loads(addr)
            mydir.read(a)

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

        if int(y) == 8:
            a = input("Enter Source File Name: ")
            d = input("Enter Destination Directory: ")
            b = [y, a, d]
            data = pickle.dumps(b)
            c.send(data)
            addr = c.recv(MAX_SIZE_BYTES)
            datar = pickle.loads(addr)
            print(datar[0])

        if int(y) == 9:
            a = "Directory Names: "
            b = [y, a]
            data = pickle.dumps(b)
            c.send(data)
            addr = c.recv(MAX_SIZE_BYTES)
            datar = pickle.loads(addr)
            print(datar[0])
            print(datar[1])

        if int(y) == 10:
            a = "Memory Map"
            b = [y, a]
            data = pickle.dumps(b)
            c. send(data)
            addr = c.recv(MAX_SIZE_BYTES)
            datar = pickle.loads(addr)
            print(datar[0])
            mydir.memoryMap()

        if int(y) == 11:
            a = "Exiting program...."
            b = [y, a]
            data = pickle.dumps(b)
            c.send(data)
            addr = c.recv(MAX_SIZE_BYTES)
            datar = pickle.loads(addr)
            print("Exiting program by {}".format(host))
            print(datar[0])
            break

    c.close()


if __name__ == '__main__':
    client()
