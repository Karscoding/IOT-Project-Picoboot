import customtkinter 
from tkinter import messagebox
from time import sleep
from PIL import Image, ImageTk
import os
import sys
import datetime
from threading import Thread
import requests
import json
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
from translate import translate
from jsonhandler import Writer, Reader

#Color Variable
color="#00A0AC"

#Font Dictionaries
fonthuge={"family":"Roboto",
          "size":48,
          "weight":"bold"}

fontbold={"family":"Roboto",
          "size":30,
          "weight":"bold"}

fontmedium={"family":"Roboto",
          "size":24}

fontsmall={"family":"Roboto",
           "size":16}

#Server Config Variables
SENDPOINT='/input'
PORT= '5000'