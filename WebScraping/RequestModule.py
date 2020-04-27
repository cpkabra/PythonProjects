
#@author Neel Patel
#@file RequestModule.py

import requests
import os, sys
from pathlib import Path


#Steps :
#--------------------------------------------------------------------------------#
#   1. OPTIONAL : Use OS.mkdir to create a directory for IO files                #
#   2. Check for a FileExistsError                                               #
#   3. Use Path(filename) to get the path to create a file                       #
#   4. Use path.write_text("") to initiate the creation                          #
#   5. Use request.get("file_url") to get the request response                   #
#   6. User open(file) to access newly created file in binary write mode         #
#   7. Iterate through request call by using request.iter_content(100000)        #
#   8. write each chunk from request to input_file accessed in binary write mode #
#   9. Close input_file                                                          #
#   10. Close requested or downloaded file                                       #
#--------------------------------------------------------------------------------#

try:
    #Make directory called "IOFiles"
    os.mkdir("IOFiles")
except FileExistsError:
    #The directory already exists
    print("Looks like IOFiles directory already exists!")
#Override created_file if it already exists
created_file = Path("IOFiles/IOFileWrite.txt")

#Initiate the creation of file
created_file.write_text("")
#Get file from online
request_handler = requests.get("https://automatetheboringstuff.com/files/rj.txt")
#Open input file in binary write mode
input_file = open(str(created_file), "wb")
#For every binary chunk in file returned from request_handler
for chunks in request_handler.iter_content(100000):
    #Write it in the input_file
    input_file.write(chunks)

#Close both files
input_file.close()
request_handler.close()
print("Files are closed!")

sys.exit()
