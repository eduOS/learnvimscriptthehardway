import re  
import os  
import shutil  
import time  
  
dir = os.getcwd()
  
filelist=[]  
  
filelist=os.listdir(dir)  
  
for i in filelist:  
    ismatch = re.search(r'^\d{2}.',i)
    if ismatch:
        with open(i,'r') as f:
            first_line = f.readline()
            file_name = re.sub(r'\s+', '_', first_line.strip('\n'))
            f.close()
            NewFile=i.replace(i,file_name)
            shutil.move(dir+'/'+i,dir+'/'+i[:3]+NewFile+'.md') 
print 'over'
