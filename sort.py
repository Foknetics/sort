"""sort.py sorts files in the sourcepath into the sortedpath with year/day/month folders."""

import os
import shutil
import datetime

# set this to the source directory
sourcepath = 'C:/Users/Default/Pictures'
# set this to the final location directory
sortedpath = 'C:/Users/Default/Pictures'

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