import os
from datetime import datetime

#convert from numerical timestamp to date YYYY-MM-DD
def timeConvert(time_value):
  time_value = time_value
  new_time_format = datetime.fromtimestamp(time_value)
  return new_time_format.date()

#convert size from numerical to KB with 2 decimal places
def sizeFormat(size):
    new_size_format = format(size/1024, ".2f")
    return new_size_format + " KB"


def createFileRecords(source_dir):

    firstDict = {}
    
    for name in os.listdir(source_dir): 
        
        filepath = os.path.join(source_dir, name)
        
        #main library that holds stats
        stats = os.stat(filepath)
        
        attrs = {
            'File Name': name,
            'Size (KB)': sizeFormat(stats.st_size),
            'Creation Date': timeConvert(stats.st_birthtime),
            'Modified Date': timeConvert(stats.st_mtime),
            'Last Access Date': timeConvert(stats.st_atime),            
        }
               
        firstDict[name] = attrs 
    
    return firstDict 


def printDir(source_dir):
    dictOfDicts = createFileRecords(source_dir)

    for n, a in dictOfDicts.items():
    
        print(f"Displaying for file: '{n}':")
        for i, j in a.items():
            print(f"{i}: {j}")
        print()


#if __name__ == "__main__":
   
    #printDir('')