import os
from datetime import datetime


class MetaProcessor():
    def __init__(self, folder_path):
        self.folder_path = folder_path

    #convert from numerical timestamp to date YYYY-MM-DD
    def timeConvert(self, time_value):
        time_value = time_value
        new_time_format = datetime.fromtimestamp(time_value)
        return new_time_format

    #convert size from numerical to KB with 2 decimal places
    def sizeFormat(self, size):
        new_size_format = format(size/1024, ".2f")
        return new_size_format + " KB"

    #create dict that holds file name as a key and modificaiton date as a value
    def createFileRecords(self):

        attr_dict = {}
        
        for name in os.listdir(self.folder_path): 
            
            filepath = os.path.join(self.folder_path, name)
            
            #main library that holds stats
            stats = os.stat(filepath)
            
            attr_dict[name] = self.timeConvert(stats.st_mtime)
        
        return attr_dict 
          

    def sortByModDate(self):
        attr_dict = self.createFileRecords()
        sorted_dict = dict(sorted(attr_dict.items(), key=lambda item: item[1]))
        return sorted_dict
    

    def renameInDict(self):
        sorted_dict = self.sortByModDate()
        renamed_dict = self.sortByModDate()
        number_for_name = 1
        #assign new names as dict values -> "old name": "new name" 
        for key in sorted_dict:
            sorted_dict[key] = str(number_for_name) + ".jpg"
            number_for_name += 1

        renamed_dict = dict((sorted_dict[key], value) for (key, value) in renamed_dict.items())
        return renamed_dict

    #to be amended 
    def renameFiles(self):
        renamed_dict = self.renameInDict()
        for root, dirs, files in os.walk(path):
            for file in files:
                new_file = file
                new_file = new_file.lower()
                for key, value in character_dictionary.items():
                    new_file = new_file.replace(key, value)
                #os.rename(os.path.join(root, file), os.path.join(root, new_file))