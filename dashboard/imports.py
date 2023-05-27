import customtkinter 
from time import sleep
from PIL import Image, ImageTk
import os
import sys
import datetime
from function_filewrite import WritetoFile

fontbold={"family":"Roboto",
          "size":26,
          "weight":"bold"}

fontmedium={"family":"Roboto",
          "size":18}

fontname="Roboto"
fontsizebold=26
fontsizemed=18

color="#00A0AC"

SENDPOINT='/input'
PORT= '5000'