import os
import shutil
import datetime

sourcepath = 'C:/Users/Default/Pictures' #set this to the source directory
sortedpath = 'C:/Users/Default/Pictures' #set this to the final location directory

for root, dirs, files in os.walk(sourcepath):
    for name in files:
        if name == 'Thumbs.db':
            continue
        time = os.path.getctime(root+'/'+name)
        time = datetime.date.fromtimestamp(time)
        path = sortedpath+'/'+str(time.year)+'/'+str(time.month)+'/'+str(time.day)
        if not os.path.exists(path):
            os.makedirs(path)
        path = path + '/' + name
        shutil.move(root+'/'+name, path)