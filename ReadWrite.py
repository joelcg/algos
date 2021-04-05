def readWrite():
        datFile=open('D:\mbox.txt', 'r')
        writeFile=open('D:\EmailFrom.txt', "w")
        for line in datFile:
#            line=line.rstrip()
            if line.startswith('From:'):
                writeFile.write(line)    
        writeFile.close()
        
readWrite()
