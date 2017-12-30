import os
''' Not using Absolute paths os.path.join(dir,item) results in checking the file's/dir's with 
current working directory.
'''

def recursive_lister(dir,count):
    list_a = os.listdir(dir)
    list_a.sort()
    for item in list_a:
        if item[0] != ".":  #Excluding Hidden Items
            if os.path.isfile(os.path.join(dir,item)):
                item_stats = os.stat(os.path.join(dir,item))
                print "_ _ _"*count + item + "(F)" + "[" + str(item_stats.st_size) + "]"
            elif os.path.isdir(os.path.join(dir,item)):
                print "_ _ _"*count + item + "(D)"
                recursive_lister(os.path.join(dir,item),(count+1))
            else:
                print "_ _ _"*count + item + "(U)"


home = os.path.expanduser("~")
file_a = os.getcwd()
recursive_lister(home,0)
print os.path.join(home,"PycharmProjects")