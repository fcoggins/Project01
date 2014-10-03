import os
import shutil
import string


for letter in string.ascii_lowercase:
    os.makedirs("folders/" + letter)

for file in os.listdir("original_files"):
    letter = file[0]
    shutil.copy("original_files/" + file, "folders/" + letter) 