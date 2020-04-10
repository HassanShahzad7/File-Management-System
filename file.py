#Group Members
#Hassan Shahzad

#Implementing files class
class files:
    '''initializing filename, pages, ptr, mainPage and pgOffset
    filename is initialized to an empty string
    pages is an empty dictionary
    mainPage consists of 1024 unintialized pages
    pgOffset is a list of 1024 uninitialized number of entries 
    '''
    filename = "" 
    pages = {}
    ptr = 0
    mainPage = [False] * 1024
    pgoffset = [0] * 1024

    namer = ""

    def __init__(self, name):
        self.namer = name

    def renameFile(self, newName):
        self.filename = newName

    def getName(self):
        return self.filename

    # Method to write to the main text file funner.dat
    def writeToFile(self, txt, pgno, offset):
        n = 1024
        # Customize file open location for your own self
        fopen = open("F:/labOS/funner.dat", "r+") 
        # moves the pointer of file towards the page number specified, as each page consists of 1024 bytes to it is multiplied by 1024
        # the product is then added with offset to start writing to the file from the offset specified
        fopen.seek(pgno*1024 + offset) 
        # if file exists then open
        if fopen:
            fopen.seek(pgno*1024+offset)
            # checks whether sum of offset and len(txt) is greater than 1024 means that it actually checks whether the data inputed
            # by the user is greater than 1024 bytes.
            # for example: the word "Hassan" contains 6 letters hence it contains 6 Bytes so it will false the following condition
            if offset + len(txt) > 1024:
                buffer = txt
                # writes to file to the buffer array from 0 index to the difference of 1024 and offset
                fopen.write(buffer[0:(1024 - offset)])
                self.mainPage[pgno] = True
                # loops till 1024 - size of Byte
                for i in range(n):
                    # initialized tmppg no to the respective mainPage
                    tmppgno = self.mainPage[i]
                    # moves the pointer as of Byte size
                    fopen.seek(tmppgno*1024)
                    # Writes to the file by slicing such that it starts writing from difference of 1024-offset+1 and ends at the 
                    # position returned by the difference of len(txt) and 1024-offset
                    fopen.write(buffer[1024-offset+1: len(txt) - (1024-offset)])
                    self.pgoffset[i] = len(txt) - (1024-offset)
                    
                    self.mainPage[i] = True
            # else if the length of text entered by the user is less than 1024
            else:
                fopen.seek(pgno*1024+offset)
                buffer = txt
                fopen.write(buffer[0:len(txt)])
                self.pgoffset[pgno] = len(txt) +offset


        fopen.close()

    # method to truncate the file
    def truncae(self, pgno, maximumSize):
        buffer = [0]*maximumSize
        limit = 1024
        count = 0
        # opens the file for read and append
        f = open("F:/labOS/funner.dat", "r+")
        if f:
            # moves the pointer
            f.seek(pgno*1024+maximumSize)
            # instead of trimming the file it actually overwrites the file with empty spaces
            for i in range(limit):
                buffer[count] = " "
                f.write(str(buffer[count]))
        f.close()


root = files("Main")
#root.read(2,0,10)
