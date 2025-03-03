import os
from datetime import datetime
import shutil


class MetaProcessor():
    def __init__(self, folder_path):
        self.folder_path = folder_path


    def printDir(self):
        print(self.folder_path)

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

        attr_dict = []
        
        for name in os.listdir(self.folder_path):
            
            filepath = os.path.join(self.folder_path, name)
            
            #main library that holds stats
            stats = os.stat(filepath)
            
            attrs = {
            'File Name': name,
            'Size (KB)': self.sizeFormat(stats.st_size),
            'Creation Date': self.timeConvert(stats.st_birthtime),
            'Modified Date': self.timeConvert(stats.st_mtime),
            'Last Access Date': self.timeConvert(stats.st_atime)
            }
            
            attr_dict.append(attrs)
            
        return attr_dict
          

    def sortByModDate(self):
        attr_list = self.createFileRecords()
        sorted_list = sorted(attr_list, key=lambda x: x['Modified Date'])
        return sorted_list
    

    def addNewName(self):
        sorted_files_list = self.sortByModDate()
        file_no = 0
        for file_attrs_dict in sorted_files_list:
            sorted_files_list[file_no]['New File Name'] = str(file_no + 1) + '.jpg'  
            file_no += 1
        return sorted_files_list


    def renameFiles(self):
        sorted_files_list = self.addNewName()
        
        '''
        path_for_renamed = os.path.join(self.folder_path, "sorted")
        if not os.path.exists(path_for_renamed):
            os.makedirs(path_for_renamed)'''
        
        for root, dir, files in os.walk(self.folder_path):
            for file in files:
                for dic in sorted_files_list:
                    if dic["File Name"] == file:
                        os.rename(os.path.join(self.folder_path, file), os.path.join(self.folder_path, dic['New File Name']))
                                    