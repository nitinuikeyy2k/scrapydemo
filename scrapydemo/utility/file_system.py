from datetime import datetime
import os
import media_store as ms

class FileSystem(ms.Store):

    def __init__(self):
        pass

    def create_directory(self, path):
        try:
            os.mkdir(path)
        except OSError:
            print("creation of directory failed %s" %path)
        else:
            #TODO log info that directory has been created
            print("directory has been created %s" %path)

    def get_path(self):
        ''' this method can return the local path or s3 path '''
        return os.getcwd()

    def is_path_exist(self, path):
        return os.path.isdir(path)

file_system = FileSystem()
now = datetime.now()
time = now.strftime("%Y%m%d")
path = os.path.join(file_system.get_path(), time)
if file_system.is_path_exist(path):
    print("Directory already exist %s" %path)
else:
    file_system.create_directory(path)