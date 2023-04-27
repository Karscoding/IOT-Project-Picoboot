import customtkinter 
from time import sleep
import os
import sys
import datetime
import config
import requests
import json
import threading

url = f"http://localhost:{config.PORT}{config.SENDPOINT}"

customtkinter.set_default_color_theme("blue")
customtkinter.set_appearance_mode("light")


class Tijd(customtkinter.CTkFrame):
    def __init__(self,*args,master,header_name='tijd', **kwargs):
        super().__init__(master, *args, **kwargs)
        self.header_name= header_name

        self.label = self.label = customtkinter.CTkLabel(self, width=120, height=25, fg_color=("dark gray", "gray75"), corner_radius=8,anchor="center", text="Tijd")
        self.label.grid(row=0,column=0,padx=80,pady=10)

        self.label = customtkinter.CTkLabel(self, width=120, height=25, corner_radius=8,anchor="center", text="")
        self.label.grid(row=1,column=0,padx=0,pady=80)
        self.time()
    
    def time(self):
        now = datetime.datetime.now()
        tijd=(now.strftime("%A, %B %d %Y %H:%M:%S"))
        self.label.configure(text=f"Tijd : {tijd}")
        self.after(1000, self.time)


class Afstand(customtkinter.CTkFrame):
    def __init__(self, *args, master ,header_name="Afstand", **kwargs):
        super().__init__(master,*args, **kwargs)
        self.header_name = header_name

        self.label = customtkinter.CTkLabel(self, width=120, height=25, fg_color=("dark gray", "gray75"), corner_radius=8,anchor="center", text="Afstand tot bodem")
        self.label.grid(row=0,column=0,padx=80,pady=10)

        self.label = customtkinter.CTkLabel(self, width=120, height=25, corner_radius=8,anchor="center", text="Afstand: nog niet gemeten")
        self.label.grid(row=1,column=0,padx=0,pady=80)

        self.button = customtkinter.CTkButton(self, text='Start met lezen', command= self.distanceRead)
        self.button.grid(row=2,column=0,padx=0,pady=20)
    
    def distanceRead(self):
        path = os.path.join(sys.path[0], './Texts/afstand.txt')
        with open(path, 'r') as f:
            distance = f.read().strip()
        self.label.configure(text=f"Afstand : {distance}")
        # schedule the next update after 5 seconds
        self.after(5000, self.distanceRead)


class Temp(customtkinter.CTkFrame):
    def __init__(self, *args, master, header_name="Temperatuur", **kwargs):
        super().__init__(master,*args, **kwargs)
        self.header_name= header_name

        self.label = customtkinter.CTkLabel(self, width=120, height=25, fg_color=("dark gray", "gray75"), corner_radius=8,anchor="center", text="Temperatuur Motorkamer")
        self.label.grid(row=0,column=0,padx=20,pady=10)


        self.label = customtkinter.CTkLabel(self, width=120, height=25, corner_radius=8,anchor="center", text="Temperatuur: nog niet gemeten")
        self.label.grid(row=1,column=0,padx=0,pady=80)
        

        self.button = customtkinter.CTkButton(self, text='Start met lezen', command= self.tempRead)
        self.button.grid(row=2,column=0,padx=0,pady=20)
        

    def tempRead(self):
        path = os.path.join(sys.path[0], './Texts/temp.txt')
        with open(path, 'r') as f:
            temp = f.read().strip()
        self.label.configure(text=f"Temperatuur : {temp}")
        # schedule the next update after 5 seconds
        self.after(5000, self.tempRead)


class ControlPanel(customtkinter.CTkFrame):    
    def __init__(self, *args, master, header_name="Besturingspaneel", **kwargs):
        super().__init__(master, *args, **kwargs)
        # add widgets onto the frame...
        self.header_name = header_name

        self.label = customtkinter.CTkLabel(self, width=120, height=25, fg_color=("white", "gray75"), corner_radius=8,anchor="center", text="Besturingspaneel")
        self.label.grid(row=2, column=0, padx=20, pady=10)


class StatusFrame(customtkinter.CTkFrame):
    def __init__(self, *args, master,header_name="Status machine", **kwargs):
        super().__init__(master, *args, **kwargs)
        # add widgets onto the frame...

        self.header_name = header_name
        self.label = customtkinter.CTkLabel(self, width=120, height=25, fg_color=("orange", "gray75"), corner_radius=8,anchor="center", text="Status Machine")
        self.label.grid(row=0, column=0, padx=10, pady=30)
        self.label = customtkinter.CTkLabel(self, width=120, height=25, fg_color=("red", "gray75"), corner_radius=8,anchor="center", text="Status Aggregraat")
        self.label.grid(row=1, column=0, padx=0, pady=10)
        self.label = customtkinter.CTkLabel(self, width=120, height=25, fg_color=("green", "gray75"), corner_radius=8,anchor="center", text="Status Compressor")
        self.label.grid(row=2, column=0, padx=0, pady=10)
        self.label = customtkinter.CTkLabel(self, width=120, height=25, fg_color=("green", "gray75"), corner_radius=8,anchor="center", text="Status Verlichting")
        self.label.grid(row=3, column=0, padx=0, pady=10)
        self.label = customtkinter.CTkLabel(self, width=120, height=25, fg_color=("green", "gray75"), corner_radius=8,anchor="center", text="Status Voorschuif")
        self.label.grid(row=4, column=0, padx=0, pady=10)
        self.label = customtkinter.CTkLabel(self, width=120, height=25, fg_color=("green", "gray75"), corner_radius=8,anchor="center", text="Status Achterschuif")
        self.label.grid(row=5, column=0, padx=0, pady=10)


class ProgressFrame(customtkinter.CTkFrame):
    def __init__(self, *args, master,header_name="Warmlopen starten:", **kwargs):
        super().__init__(master, *args, **kwargs)
        # add widgets onto the frame...
        
        self.header_name = header_name
        self.label = customtkinter.CTkLabel(self, width=120, height=25, fg_color=("dark gray", "gray75"), corner_radius=8,anchor="center", text="Timer (5 minuten)")
        self.label.grid(row=0, column=0, padx=0, pady=10)

        self.progressbar = customtkinter.CTkProgressBar(self, height=20)
        self.progressbar.grid(row=1, column=0, padx=20, pady=80)
        self.progressbar.set(0)
        self.progressbar._border_width=(1)
        self.progressbar._progress_color=("green")
        self.progressbar._border_color=("black")
        self.progressbar._mode=("determinate")
        self.progressbar._determinate_speed=(1/300)

        def start_progress_bar():
            self.progressbar.start()
        
        self.button_1 =customtkinter.CTkButton(self, text="Start", border_width=0,corner_radius=8,width=120,height=32,command=start_progress_bar)
        self.button_1.grid(row=2, column=0, padx=0, pady=10)


class RadioButtonFrame(customtkinter.CTkFrame):
    def __init__(self, *args, header_name="RadioButtonFrame", **kwargs):
        super().__init__(*args, **kwargs)
        
        self.header_name = header_name

        self.label = customtkinter.CTkLabel(self, width=120, height=25, fg_color=("dark gray", "gray75"), corner_radius=8,anchor="center", text="Besturingsmodus")

        self.label.grid(row=0, column=0, padx=10, pady=10)

        self.radio_button_var = customtkinter.StringVar(value="")

        self.radio_button_1 = customtkinter.CTkRadioButton(self, text="Handmatig", value="Handmatig", variable=self.radio_button_var)
        self.radio_button_1.grid(row=1, column=0, padx=10, pady=10)
        self.radio_button_2 = customtkinter.CTkRadioButton(self, text="Automatisch", value="Automatisch", variable=self.radio_button_var)
        self.radio_button_2.grid(row=2, column=0, padx=10, pady=10)

        def get_value():
            """ returns selected value as a string, returns an empty string if nothing selected """
            return self.radio_button_var.get()
        self.frame_1_button = customtkinter.CTkButton(self, text="Selecteer", command=get_value)
        self.frame_1_button.grid(row=3, column=0, padx=20, pady=30)

  

    def set_value(self, selection):
        """ selects the corresponding radio button, selects nothing if no corresponding radio button """
        self.radio_button_var.set(selection)
       
   
#Lights control panel
class LightsControl(customtkinter.CTkFrame):    
    def __init__(self, *args, master, header_name="Lampen Besturing", **kwargs):
        super().__init__(master, *args, **kwargs)
        # add widgets onto the frame...
        self.header_name = header_name

        self.label = customtkinter.CTkLabel(self, width=120, height=25, fg_color=("dark gray", "gray75"), corner_radius=8,anchor="center", text="Besturingsmodus")

        self.label.grid(row=0, column=0, padx=10, pady=10)

        self.radio_button_var = customtkinter.StringVar(value="")

        self.radio_button_1 = customtkinter.CTkRadioButton(self, text="Bakboord", value="Bakboord", variable=self.radio_button_var)
        self.radio_button_1.grid(row=1, column=0, padx=10, pady=10)
        self.radio_button_2 = customtkinter.CTkRadioButton(self, text="Stuurboord", value="Stuurboord", variable=self.radio_button_var)
        self.radio_button_2.grid(row=2, column=0, padx=10, pady=10)

        #Deze functie zal elke 2 seconden de ingevulde waarde sturen
        #Misschien handig om deze functie alleen te runnen als de waarde wordt veranderd...
        def send_value():
            """
            Sends value to app.py"""
            while True:
                lights = self.radio_button_var.get()
                requests.post(url, json=lights)
                sleep(2)
                
        threading.Thread(target=send_value).start()
             
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.geometry('1280x720')
        self.title("placeholder dashboard")

        self.tijd= Tijd(master=self,header_name="Tijd")
        self.tijd.grid(row=1, column=0, padx=20,pady=20)

        self.my_frame = ProgressFrame(master=self, header_name="Warmlopen starten:")
        self.my_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew") 
        
        self.radio_button_frame_1 = RadioButtonFrame(self, header_name="Besturingsmodus")
        self.radio_button_frame_1.grid(row=0, column=1, padx=20, pady=20)
        
        self.my_frame2 = StatusFrame(master=self, header_name="Status machine")
        self.my_frame2.grid(row=0, column=2, padx=20, pady=20)
        
        self.temp = Temp(master=self,header_name="temp")
        self.temp.grid(row=0, column=3, padx=20,pady=20)

        self.afstand = Afstand(master=self, header_name='afstand')
        self.afstand.grid(row=0,column = 4 , padx=20, pady=20)
        
        self.light_control = LightsControl(master=self, header_name="Lampen Besturing")
        self.light_control.grid(row=1, column=1, padx=20, pady=20)


if __name__ == "__main__":
    app=App()
    app.mainloop()