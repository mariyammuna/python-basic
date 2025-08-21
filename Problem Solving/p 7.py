# from os import listdir
# from os.path import isfile , join

# files_list = [f for f in listdir('/users') if isfile(join('/home', f))]


from os import listdir
from os.path import isfile, join

path = '/home/muna'
files_list = [f for f in listdir(path) if isfile(join(path, f))]

print(files_list)