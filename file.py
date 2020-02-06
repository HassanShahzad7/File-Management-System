#Group Members
#Hassan Shahzad
#Bisma Aslam 
#Mahnoor Abeer
#Qurat Ul Ain
#Zunaira Shafaq

class files:
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

    def writeToFile(self, txt, pgno, offset):
        n = 1024
        fopen = open("F:/labOS/funner.dat", "r+")
        fopen.seek(pgno*1024 + offset)
        if fopen:
            fopen.seek(pgno*1024+offset)
            if offset + len(txt) > 1024:
                buffer = txt
                fopen.write(buffer[0:(1024 - offset)])
                self.mainPage[pgno] = True
                for i in range(n):
                    tmppgno = self.mainPage[i]
                    fopen.seek(tmppgno*1024)
                    fopen.write(buffer[1024-offset+1: len(txt) - (1024-offset)])
                    self.pgoffset[i] = len(txt) - (1024-offset)

                    self.mainPage[i] = True
            else:
                fopen.seek(pgno*1024+offset)
                buffer = txt
                fopen.write(buffer[0:len(txt)])
                self.pgoffset[pgno] = len(txt) +offset


        fopen.close()


#    def moveWithIn(self, pgno, start, size, target):
#        buffer = self.read(pgno, start, size)
#        txt = str(buffer)
#        self.writeToFile(txt, pgno, target)

   # def read(self, pgno):
    #    f = open("F:/labOS/fun.dat", "r+")
     #   f.seek(pgno*1024)
      #  while f:
       #     print(f.read())
        #    if(False):
         #       break
       # f.close()

    def truncae(self, pgno, maximumSize):
        buffer = [0]*maximumSize
        limit = 1024
        count = 0
        f = open("F:/labOS/funner.dat", "r+")
        if f:
            f.seek(pgno*1024+maximumSize)
            for i in range(limit):
                buffer[count] = " "
                f.write(str(buffer[count]))
        f.close()


root = files("Main")
#root.read(2,0,10)
