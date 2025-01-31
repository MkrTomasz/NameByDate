import os
from datetime import datetime


class MetaProcessor():
    def __init__(self, source_dir):
        self.source_dir = source_dir

    #convert from numerical timestamp to date YYYY-MM-DD
    def timeConvert(self, time_value):
        time_value = time_value
        new_time_format = datetime.fromtimestamp(time_value)
        return new_time_format.date()

    #convert size from numerical to KB with 2 decimal places
    def sizeFormat(self, size):
        new_size_format = format(size/1024, ".2f")
        return new_size_format + " KB"


    def createFileRecords(self):

        firstDict = {}
        
        for name in os.listdir(self.source_dir): 
            
            filepath = os.path.join(self.source_dir, name)
            
            #main library that holds stats
            stats = os.stat(filepath)
            
            attrs = {
                'File Name': name,
                'Size (KB)': self.sizeFormat(stats.st_size),
                'Creation Date': self.timeConvert(stats.st_birthtime),
                'Modified Date': self.timeConvert(stats.st_mtime),
                'Last Access Date': self.timeConvert(stats.st_atime),            
            }
                
            firstDict[name] = attrs 
        
        return firstDict 


    def printDir(self):
        dictOfDicts = self.createFileRecords()

        for n, a in dictOfDicts.items():
        
            print(f"Displaying for file: '{n}':")
            for i, j in a.items():
                print(f"{i}: {j}")
            print()
