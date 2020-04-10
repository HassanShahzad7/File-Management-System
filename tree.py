
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
        #calling offsetcalcFile to get the offset returned by the function
        a = self.offsetcalcFile()
        # converting the offset to integer
        b = int(a) 
        # equating c to the page num
        c = self.pageallocF() 
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

    # a method to convert the file name or directory name entered by the user into a key-value pair and write into the file
    def dictToText(self, fname, pg, off): 
        # takes filename and appends it with ":" and page number on which the file's data is stored
        a = fname + ":" + str(pg) 
        # each entry is given a size of 16 bytes in the text file so that the files can be accessed easily
        b = off * 16 
        # writing the data to text file
        self.myfile.writeToFile(a, 0, b) 

    # returns the name of files
    def pagenumberFile(self): 
        self.getFiles()

    # calculates offset, by which we mean that where the next the file data will be written on the text file
    def offsetcalcFile(self): 
        #opens funner.dat for read and write mode, Note: if you are using this method for the first time then use "w+" to first create the file
        file = open("F:/labOS/funner.dat", "r+") 
        # each page size equated to 16 bytes
        page_size = 16 
        # total .dat file contains 64 pages each of 256 bytes, in order to move from one page to another we equate it to 256
        page_num = 256 
        #moving the file pointer to read the contents
        file.seek(page_num * page_size) 
        #reads and outputs the contents
        a = file.read(page_size) 
        print(a)
        return a

    def offsetAdd(self):
        #takes in offset i.e the page number of file and add '1' to it each time for the next file to be entered
        a = self.offsetcalcFile() 
        b = int(a)
        b += 1
        return b

    #deletes the file
    def delFile(self, filename): 
        file = open("F:/labOS/funner.dat", "r+")
        #takes the length of file
        u = len(filename) 
        #equating k to files already stored
        k = self.numberofFiles() 
        pgnum = 0
        for i in range(k):
            #moving the pointer each time with 16 bytes
            file.seek(i * 16) 
            #reads the file
            a = file.read(u) 
            if a == filename:
                #if file founds it then overwrites the file data entered in the table with blank spaces, meaning that the file is removed
                print("file found") 
                self.myfile.writeToFile("                ", 0, file.seek(i * 16))
         #also deletes the file from Memory Map
        self.delFfromMM(filename)

    # Creates a new directory
    def addChildDir(self, dirname):
        # returns the number of directories already made
        a = self.numberofDirs()
        b = int(a)
        # multiplied by 16 as of number of Bytes in each page
        c = b * 16
        # writes directory name to the funner.dat
        self.myfile.writeToFile(dirname, 1, c)

    # returns the number of directories in the file
    def numberofDirs(self):
        file = open("F:/labOS/funner.dat", "r+")
        page_size = 16
        counter = 0
        # total number of pages = 64
        page_num = 64
        # accesses the pages from idx 64 to 128 i.e page number 2 in the text file
        while page_num in range(128):
            # moves the file pointer
            file.seek(page_num * page_size)
            # reads the file 
            a = file.read(page_size)
            # checks whether the entry in the page is empty, if empty then breaks the loop
            # Note there are 16 number of empty spaces, as each entry takes 16 specific bytes
            if a == "                ":
                break
            # if there is a specific entry then increment both counter and page num
            else:
                counter += 1
                page_num += 1
        print(counter)
        return counter

    # deletes the directory given
    def delChildDir(self, dirname):
        file = open("F:/labOS/funner.dat", "r+")
        u = len(dirname)
        # returns the number of directories
        k = self.numberofDirs()
        offset = 0
        i = 64
        j = i + k
        while i in range(j):
            file.seek(i * 16)
            a = file.read(u)
            # if directory found then delete the file by overwriting with blank spaces
            if a == dirname:
                self.myfile.writeToFile("                ", 1, offset*16)
            i += 1
            offset += 1
        # also deletes the directory from the memory map
        self.deldirfromMM(dirname)

    # returns the file names
    def getFiles(self):
        file = open("F:/labOS/funner.dat", "r+")
        page_size = 16
        page_num = 0
        # returns the number of files 
        k = self.numberofFiles()
        for page_num in range(k):
            # moves the file pointer towards the file name and prints its name
            file.seek(page_num * page_size)
            a = file.read(page_size)
            print(a)

    # returns the number of files created
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

    # method to allocate file number to each file
    # each file number tells on which respective page the file data has been entered
    def pageallocF(self):
        a = self.numberofFiles()
        b = int(a)
        # incremented by 5 as bcz first 4 pages are used up by file names, directory names and directory structure
        c = b + 5
        print(c)
        return c

    # returns the directories names
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

    # returns the memory map
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

    # method to calculate the offset for memory map
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

    # deletes the file name from memory map
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
            # slices b as first 16 bytes occupied by the memory map contains directory name
            # basically the following actually removes the name from the memory map i.e removes the pointer from directory to filename
            # it does not erases content of the file
            b = a[16:16+u]
            if b == filename:
                self.myfile.writeToFile("                ", 2, counter+16)
            page_num += 1
            counter += 32
    
    # moves the file from one directory to another directory
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

    # deletes the directory name from memory map 
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

    # checks the page number associated with the file mentioned
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

    # reads the contents of the file
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

    # truncates / trims the contents of the file upto maxsize limit
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

    # writes to file
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

        # check whether the specific directory is present or not
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

    # moves the text within the file from a specific range to a specific place 
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

        
        print(c)



root = directories("hsk")


