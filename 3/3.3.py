#файл с директориями называется 'result.txt'
import os

def write_array(array, file_name):
    """записывает строки из array в файл file_name без циклов"""
    with open(file_name, 'w') as f: 
        f.write('\n'.join(array))

#unpack zip file to current working directory
curr_dir=os.getcwd()
import zipfile
with zipfile.ZipFile('D:\\main.zip', 'r') as zip_ref:
    zip_ref.extractall(curr_dir)

os.chdir(curr_dir+'\\main')
#collecting names of needed directories
dirs=set()
home_path=os.getcwd()
for path, path_dirs, path_files in os.walk(home_path):
    for file in path_files:
        if file[-3:] == '.py':
            dirs.add(path[path.rfind('\\')+1:])
            break
res=list(dirs)
res.sort()

#creating a file with result
os.chdir(curr_dir)
write_array(res, 'result.txt')