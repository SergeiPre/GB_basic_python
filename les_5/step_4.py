import os
full_path = os.psth.jpin(dir_path_root, file_name)

with open(full_path, 'r') as in_file, open('new_copy.txt', 'w') as cop_file:
    cop_file.write(in_file.read())


print(os.path.exists(full_path))

import shutil

shutil.copy(full_path, 'new_cop.txt')


