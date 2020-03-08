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
MAX_SIZE_BYTES = 65535 # Mazimum size of a UDP datagram

def serverprog():
    host = socket.gethostname()
    port = 95
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host, port))
    count = 0

    while True:
        clientsocket, address = s.recvfrom(MAX_SIZE_BYTES)
        print("Connection from " + str(address) + " has been established.")
        data = pickle.loads(clientsocket)
        count += 1
        print('The client at {} says {!r}'.format(address, data[0]))
        print(data)
        if data[0] == '1':

            a = data[1]
            b = data[2]
            mydir.addFile(a, b)
            b = "File Created!!"
            a = mydir.getFiles()
            k = [a]
            da = pickle.dumps(k)
            s.sendto(da, address)

        if data[0] == '2':
            a = data[1]
            b = data[2]
            d = data[3]
            mydir.writeFile(a, b, d)
            print("text written")
            z = "Text written to File"
            k = [z]
            m = pickle.dumps(k)
            s.sendto(m, address)

        if data[0] == '3':
            a = data[1]
            mydir.delFile(a)
            c = "File Deleted"
            k = [c]
            m = pickle.dumps(k)
            s.sendto(m, address)

        if data[0] == '4':
            a = data[1]
            mydir.addChildDir(a)
            a = "Directory Added"
            k = [a]
            m = pickle.dumps(k)
            s.sendto(m, address)

        if data[0] == '5':
            a = data[1]
            b = mydir.chDir(a)
            c = "Directory Status: "
            print(b)
            k = [c, b]
            m = pickle.dumps(k)
            s.sendto(m, address)

        if data[0] == '6':
            a = data[1]

            x = "File Contents: "
            time.sleep(3)
            mydir.read(a)
            k = [x]
            m = pickle.dumps(k)
            s.sendto(m, address)

        if data[0] == '7':
            a = data[1]
            b = data[2]
            x = "File Truncated: "
            mydir.truncate(a, b)
            k = [x]
            m = pickle.dumps(k)
            s.sendto(m, address)

        if data[0] == '8':
            a = data[1]
            b = data[2]
            c = "File Moved Successfully. "
            mydir.move(a, b)
            k = [c]
            m = pickle.dumps(k)
            s.sendto(m, address)

        if data[0] == '9':
            print(data[1])
            a = "Directory List"
            k = [a]
            m = pickle.dumps(k)
            s.sendto(m, address)

        if data[0] == '10':
            print(data[1])
            a = "Memory Map: "
            k = [a]
            m = pickle.dumps(k)
            s.sendto(m, address)

        if data[0] == '11':
            print(data[1])
            a = "Thank you for visiting us. Hope to see you soon!"
            k = [a]
            m = pickle.dumps(k)
            s.sendto(m, address)

        s.sendto(clientsocket, address)


if __name__ == '__main__':
    t1 = threading.Thread(target=serverprog, args=())
    t1.start()
    t1.join()
