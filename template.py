import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:') # Message, output or some meta information is stored in log file


list_of_files = [
    "src/__init__.py",
    "src/helper.py",
    "src/prompt.py",
    ".env",
    "setup.py",
    "research/trials.ipynb",
    "app.py",
    "store_index.py",
    "static/.gitkeep",
    "templates/chat.html"

]


for filepath in list_of_files:
   filepath = Path(filepath) # Here path will change automatically that is in linux => there are forward slash(/) and window => there are backward slash(\) in file path
   filedir, filename = os.path.split(filepath) # split will separate the folder and file name

   if filedir !="":
      os.makedirs(filedir, exist_ok=True)
      logging.info(f"Creating directory; {filedir} for the file {filename}")

   if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0): # In my file path if there are no file then I will create an empty file
      with open(filepath, 'w') as f:
         pass
         logging.info(f"Creating empty file: {filepath}")

   else:
      logging.info(f"{filename} is already created")
      
      
    