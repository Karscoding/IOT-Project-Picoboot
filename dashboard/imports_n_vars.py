import customtkinter 
from time import sleep
from PIL import Image, ImageTk
import os
import sys
import datetime
from function_filewrite import WritetoFile

#Color Variable
color="#00A0AC"

#Font Dictionaries
fontbold={"family":"Roboto",
          "size":30,
          "weight":"bold"}

fontmedium={"family":"Roboto",
          "size":24}

fontsmall={"family":"Roboto",
           "size":20}

#Server Config Variables
SENDPOINT='/input'
PORT= '5000'