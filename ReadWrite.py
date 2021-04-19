def readWrite():
        datFile=open('path', 'r')
        writeFile=open('path', "w")
        for line in datFile:
#            line=line.rstrip()
            if line.startswith('From:'):
                writeFile.write(line)    
        writeFile.close()
        
readWrite()
