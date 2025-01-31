import os
from datetime import datetime

def timeConvert(atime):
  dt = atime
  newtime = datetime.fromtimestamp(dt)
  return newtime.date()

   
def sizeFormat(size):
    newform = format(size/1024, ".2f")
    return newform + " KB"


def createFileRecords(somepath):
    #dictionary
    firstDict = {}
    
    for name in os.listdir(somepath): 
        
        filepath = os.path.join(somepath, name)
        
        #main library that holds stats
        stats = os.stat(filepath)
        
        attrs = {
            'File Name': name,
            'Size (KB)': sizeFormat(stats.st_size),
            'Creation Date': timeConvert(stats.st_ctime),
            'Modified Date': timeConvert(stats.st_mtime),
            'Last Access Date': timeConvert(stats.st_atime),            
        }
               
        firstDict[name] = attrs 
    
    return firstDict 


def printDir(somepath):
    dictOfDicts = createFileRecords(somepath)

    for n, a in dictOfDicts.items():
    
        print(f"Displaying for file: '{n}':")
        for i, j in a.items():
            print(f"{i}: {j}")
        print()


if __name__ == "__main__":
   
    printDir('F:/pytun/NameByDate/test')