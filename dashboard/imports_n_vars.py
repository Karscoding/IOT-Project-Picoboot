# - Import bestand -
#
# Dit bestand is een algemeen punt waar alle bestanden in deze folder dezelfde dingen kunnen importen.
# Als we in elk bestand dezelfde imports zouden plaatsen zou je circulair imports krijgen.
# Vandaar dit bestand.
# 
# Je zou waarschijnlijk geen veranderingen hoeven te doen aan dit bestand wanneer je iets wilt toevoegen.
# Maar als je iets wilt importen of een variable hebt en deze in meerder bestanden in deze folder gaat gebruiken.
# Maak het dan hier in aan.
#
# - Picoboot Team 2023 - 
#

import customtkinter 
import random
from tkinter import messagebox, Label
from time import sleep
from PIL import Image, ImageTk
import os
import sys
import datetime
from threading import Thread
import requests
import json
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

import numpy as np
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
from translate import translate
from jsonhandler import Writer, Reader
from CreateDB import app, Temperatuur, Afstand
from EmptyDB import delete
from DatabaseToText import makeup,getdata,writetotext

#Color Variable
color="#00A0AC"

#Font Dictionaries
fonthuge={"family":"Roboto",
          "size":48,
          "weight":"bold"}

fontbold={"family":"Roboto",
          "size":30,
          "weight":"bold"}

fontbig={"family":"Roboto",
         "size":28}

fontmedium={"family":"Roboto",
          "size":24}

fontsmall={"family":"Roboto",
           "size":16}

#Server Config Variables
SENDPOINT='/input'
PORT= '5000'

def highpressure(object):
    messagebox.showinfo("Waarschuwing","Druk op de schuif word te hoog, schuif omhoog")
    try:
        object.label.configure(text=f"Error gekregen, schuif tijdelijk omhoog.")
        object.swapped=2
    except:
        pass

def enginetoohot(object):
    messagebox.showinfo("Waarschuwing","Motor is te warm, schuif omhoog en minder snehlheid")
    try:
        object.label.configure(text=f"Error gekregen, schuif tijdelijk omhoog.")
        object.swapped=2
    except:
        pass
    
