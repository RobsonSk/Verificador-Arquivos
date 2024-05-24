from stat import S_ISREG, ST_MTIME, ST_MODE, ST_SIZE
import os, sys, time
from datetime import datetime
import math
import dirs_list as dirs

LogFile = (r'Caminho\arquivo\log.csv') 
ErrorFile = (r'Caminho\arquivo\Erros.txt')

                  
def convert_size(size_bytes):
   if size_bytes == 0:
       return "0B"
   size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
   i = int(math.floor(math.log(size_bytes, 1024)))
   p = math.pow(1024, i)
   s = round(size_bytes / p, 2)
   return "%s %s" % (s, size_name[i])

os.chdir(r'Diretorio\para\pesquisa') 
dirs = os.listdir() 
for i, value in enumerate(dirs):
    try:
        dirpath = dirs[i]
        entries = (os.path.join(dirpath, fn) for fn in os.listdir(dirpath))
        entries = ((os.stat(path), path) for path in entries)
        entries = ((stat[ST_MTIME], path)
            for stat, path in entries if S_ISREG(stat[ST_MODE]))
        for mdate, path in sorted(entries):
                    strftime = time.localtime(mdate)
                    DTnow = datetime.now()
                    now = DTnow.strftime("%d/%B/%Y %H:%M")
                    split_tail = os.path.dirname(path)
                    head_tail = os.path.split(split_tail) 
                    size = convert_size(os.stat(path).st_size)
                    ext = os.path.splitext(path)
                    file = open(LogFile, 'a')
                    file.write(now + ',' + head_tail[1] + ',' + os.path.basename(path)+ ',' + time.strftime("%d/%B/%Y %H:%M",strftime)+ ','  + size + ',' + ext[1] + ', \n')
                    file.close()
    except FileNotFoundError:
         file = open(ErrorFile, 'a')
         file.write('FileNotFound'+','+ dirpath )
         file.close()
         pass
    except NotADirectoryError:
         file = open(ErrorFile, 'a')
         file.write("NotADirectoryError: " + now + ',' + head_tail[1] + ',' + os.path.basename(path)+ ',' + time.strftime("%d/%B/%Y %H:%M",strftime)+ ','  + size + ',' + ext[1] + ', \n')
         file.close()
         pass
