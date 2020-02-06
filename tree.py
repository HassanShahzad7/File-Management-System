#Group Members
#Hassan Shahzad


import json


class directories:
    from file import files
    myfile = files("mainer")
    child = []
    namer = ""

    def __init__(self, name):
        self.namer = name

    def getName(self):
        return self.namer

    def addFile(self, name, txt):
        a = self.offsetcalcFile() #calling offsetcalcFile to get the offset returned by the function
        b = int(a) # converting the offset to integer
        c = self.pageallocF() # equating c to the page num
        d = int(c)
        e = b + 1
        f = str(e)
        g = self.offsetMM()
        h = int(g)
        i = h * 32
        j = i + 16
        self.myfile.writeToFile(f, 4, 0)
        self.dictToText(name, d, b)
        self.myfile.writeToFile(txt, d, 0)
        self.myfile.writeToFile("main          ~ ", 2, i)
        self.myfile.writeToFile(name, 2, j)

    def dictToText(self, fname, pg, off): # a method to convert the file name or directory name entered by the user into a key-value pair and write into the file
        a = fname + ":" + str(pg) # takes filename and appends it with ":" and page number on which the file's data is stored
        b = off * 16 # each entry is given a size of 16 bytes in the text file so that the files can be accessed easily
        self.myfile.writeToFile(a, 0, b) # writing the data to text file

    def pagenumberFile(self): # returns the name of files
        self.getFiles()

    def offsetcalcFile(self): # calculates offset, by which we mean that where the next the file data will be written on the text file
        file = open("F:/labOS/funner.dat", "r+") #opens funner.dat for read and write mode, Note: if you are using this method for the first time then use "w+" to first create the file
        page_size = 16 # each page size equated to 16 bytes
        page_num = 256 # total .dat file contains 64 pages each of 256 bytes, in order to move from one page to another we equate it to 256
        file.seek(page_num * page_size) #moving the file pointer to read the contents
        a = file.read(page_size) #reads and outputs the contents
        print(a)
        return a

    def offsetAdd(self):
        a = self.offsetcalcFile() #takes in offset i.e the page number of file and add '1' to it each time for the next file to be entered
        b = int(a)
        b += 1
        return b

    def delFile(self, filename): #deletes the file
        file = open("F:/labOS/funner.dat", "r+")
        u = len(filename) #takes the length of file
        k = self.numberofFiles() #equating k to files already stored
        pgnum = 0
        for i in range(k):
            file.seek(i * 16) #moving the pointer each time with 16 bytes
            a = file.read(u) #reads the file
            if a == filename:
                print("file found") #if file founds it then overwrites the file data entered in the table with blank spaces, meaning that the file is removed
                self.myfile.writeToFile("                ", 0, file.seek(i * 16))

        self.delFfromMM(filename) #also deletes the file from Memory Map


    def addChildDir(self, dirname):
        a = self.numberofDirs()
        b = int(a)
        c = b * 16
        self.myfile.writeToFile(dirname, 1, c)

    def numberofDirs(self):
        file = open("F:/labOS/funner.dat", "r+")
        page_size = 16
        counter = 0
        page_num = 64
        while page_num in range(128):
            file.seek(page_num * page_size)
            a = file.read(page_size)
            if a == "                ":
                break
            else:
                counter += 1
                page_num += 1
        print(counter)
        return counter

    def delChildDir(self, dirname):
        file = open("F:/labOS/funner.dat", "r+")
        u = len(dirname)
        k = self.numberofDirs()
        offset = 0
        i = 64
        j = i + k
        while i in range(j):
            file.seek(i * 16)
            a = file.read(u)
            if a == dirname:
                self.myfile.writeToFile("                ", 1, offset*16)
            i += 1
            offset += 1
        self.deldirfromMM(dirname)

    def getFiles(self):
        file = open("F:/labOS/funner.dat", "r+")
        page_size = 16
        page_num = 0
        k = self.numberofFiles()
        for page_num in range(k):
            file.seek(page_num * page_size)
            a = file.read(page_size)
            print(a)

    def numberofFiles(self):
        file = open("F:/labOS/funner.dat", "r+")
        page_size = 16
        counter = 0
        for page_num in range(64):
            file.seek(page_num * page_size)
            a = file.read(page_size)
            if a == "                ":
                break
            else:
                counter += 1
        return counter

    def pageallocF(self):
        a = self.numberofFiles()
        b = int(a)
        c = b + 5
        print(c)
        return c

    def getChildren(self):
        file = open("F:/labOS/funner.dat", "r+")
        page_size = 16
        counter = 0
        page_num = 64
        while page_num in range(128):
            file.seek(page_num * page_size)
            a = file.read(page_size)
            if a == "                ":
                break
            else:
                print(a)
                page_num += 1

    def memoryMap(self):
        file = open("F:/labOS/funner.dat", "r+")
        page_size = 32
        counter = 0
        page_num = 64
        while page_num in range(256):
            file.seek(page_num * page_size)
            a = file.read(page_size)
            if a == "                                ":
                break
            else:
                print(a)
                counter += 1
                page_num += 1
        return counter

    def offsetMM(self):
        file = open("F:/labOS/funner.dat", "r+")
        page_size = 32
        counter = 0
        page_num = 64
        while page_num in range(256):
            file.seek(page_num * page_size)
            a = file.read(page_size)
            if a == "                                ":
                break
            else:
                counter += 1
                page_num += 1
        return counter

    def delFfromMM(self, filename):
        file = open("F:/labOS/funner.dat", "r+")
        page_size = 32
        counter = 0
        page_num = 64
        u = len(filename)
        k = self.offsetMM()
        m = int(k)
        j = m * 16
        while page_num in range(256):
            file.seek(page_num * page_size)
            a = file.read(page_size)
            b = a[16:16+u]
            if b == filename:
                self.myfile.writeToFile("                ", 2, counter+16)
            page_num += 1
            counter += 32

    def move(self, srcFilename, destDirectory):
        file = open("F:/labOS/funner.dat", "r+")
        page_size = 32
        counter = 0
        count = 0
        page_num = 64
        u = len(srcFilename)
        k = self.offsetMM()
        m = int(k)
        j = m * 16
        while page_num in range(256):
            file.seek(page_num * page_size)
            a = file.read(page_size)
            b = a[16:16 + u]
            c = len(destDirectory)
            d = a[0:c]
            x = 0
            y = 0
            f = len(destDirectory)
            e = 14 - f
            g = len(srcFilename)
            h = 16 - g
            i = 16 + g
            if b == srcFilename:
                self.myfile.writeToFile("              ", 2, counter)
                self.myfile.writeToFile(destDirectory, 2, counter)
                while e > x:
                    f += 1
                    self.myfile.writeToFile(" ", 2, f)
                    x += 1
                self.myfile.writeToFile("~ ", 2, 14)
                self.myfile.writeToFile(srcFilename, 2, counter + 16)
                while h > y:
                    i += 1
                    self.myfile.writeToFile(" ", 2, i)

                    y += 1

            page_num += 1
            counter += 32

    def deldirfromMM(self, dirname):
        file = open("F:/labOS/funner.dat", "r+")
        page_size = 32
        counter = 0
        page_num = 64
        u = len(dirname)
        k = self.offsetMM()
        m = int(k)
        j = m * 16 - 16
        while page_num in range(256):
            file.seek(page_num * page_size)
            a = file.read(page_size)
            c = len(dirname)
            d = a[0:c]
            if d == dirname:
                self.myfile.writeToFile("                                ", 2, j)
            page_num += 1

    def checkFileForPage(self, filename):
        file = open("F:/labOS/funner.dat", "r+")
        offset = 16
        u = len(filename)
        k = ""
        m = ""
        j = 0
        for page_num in range(64):
            file.seek(page_num * offset)
            a = file.read(offset)
            b = a[0:u]
            if b == filename:
                for i in a:
                    if i == ":":
                        k = a[j:]
                    j += 1
            m = k[1:]
        return m

    def read(self, filename):
        file = open("F:/labOS/funner.dat", "r+")
        a = self.checkFileForPage(filename)
        b = int(a)
        offset = 16
        page = b * 64
        limit = page + 64
        c = ""
        while page in range(limit):
            file.seek(page * offset)
            a = file.read(offset)
            c += a
            page += 1
        print(c)

    def truncate(self, filename, maxsize):
        file = open("F:/labOS/funner.dat", "r+")
        a = self.checkFileForPage(filename)
        b = int(a)
        offset = 0
        page = b * 64
        limit = page + maxsize
        t = 64 - maxsize
        trun = page + 64
        while page in range(limit):
            file.seek(1)
            page += 1
            offset += 1

        while limit in range(trun):
            file.seek(limit * 16)
            self.myfile.writeToFile("                ", b, offset)
            limit += 1
            offset += 16

    def writeFile(self, filename, position, text):
        file = open("F:/labOS/funner.dat", "r+")
        a = self.checkFileForPage(filename)
        b = int(a)
        offset = 0
        page = b * 64
        limit = page + position
        while page in range(limit):
            file.seek(1)
            page += 1
            offset += 1
        file.seek(limit)
        self.myfile.writeToFile(text, b, position)

    def chDir(self, dirname):
        file = open("F:/labOS/funner.dat", "r+")
        page_size = 16
        count = len(dirname)
        page_num = 64
        c = ""
        while page_num in range(128):
            file.seek(page_num * page_size)
            a = file.read(page_size)
            b = a[0:count]
            if a == "                ":
                break
            else:
                if b == dirname:
                    c += "Directory Available. "
                page_num += 1
        if not c:
            c += "Directory not Available. "
        return c

    def movewithin(self, filename, start, size, target):
        file = open("F:/labOS/funner.dat", "r+")
        a = self.checkFileForPage(filename)
        b = int(a)
        offset = 0
        c = ""
        page = b * 64 + start
        limit = page + size
        end = page + 64
        while page in range(limit):
            file.seek(page)
            c += file.read(1)
            self.myfile.writeToFile(" ", b, start)
            file.seek(1)
            page += 1
            offset += 1

        #self.myfile.writeToFile(c, b, target)
        print(c)



root = directories("hsk")
#root.movewithin("pokemon.zip", 5, 30, 170)


