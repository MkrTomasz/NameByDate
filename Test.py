from MainPackage.MetaExtract import MetaProcessor

#pass source path into MetaProcessor
output = MetaProcessor("C:/Users/Lenovo/OneDrive/Desktop/test")

#test access to file creation date
#print(output.createFileRecords())

#test sorting dict of items found in folder by modification date
#print(output.sortByModDate())

#test renaming files in the dict
print(output.addNewName())

#test files renaming
#output.renameFiles()

'''303301.jpg
828920.png
tapeciarnia.pl-242395_dark_souls.jpg'''
