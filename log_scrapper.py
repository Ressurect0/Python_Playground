import os

cwd = os.getcwd()
os.system("cat /var/log/syslog >>"+cwd+"/logs_inspect.txt")
#os.rename("demo.txt","logs.txt")

#print cwd

log_set = set()
file_desc = open(cwd+"/logs_inspect.txt","r")

for line in file_desc.readlines():
    if line.find("USB") != -1: #and line.find("device detected") != -1:
        log_set.add(line[:15])
        #print line

print "USB Devices were attached to your system at: \n"+"\n".join(log_set)
file_desc.close()


