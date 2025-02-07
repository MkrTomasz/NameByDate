from MainPackage.MetaExtract import MetaProcessor

#pass source path into MetaProcessor
output = MetaProcessor("F:/pytun/test NameByDate")

#test access to file creation date
#print(output.createFileRecords())

#test sorting dict of items found in folder by modification date
#print(output.sortByModDate())

#test renaming files in the dict
#print(output.renameInDict())

#test files renaming
output.renameFiles()
