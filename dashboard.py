import customtkinter 
from time import sleep
import os
import sys
import datetime
import config

url = f"http://localhost:{config.PORT}{config.SENDPOINT}"

customtkinter.set_default_color_theme("blue")
customtkinter.set_appearance_mode("dark")

class Tijd(customtkinter.CTkFrame):
    def __init__(self,*args,master,header_name='tijd', **kwargs):
        super().__init__(master, *args, **kwargs)
        self.header_name= header_name

        self.label = self.label = customtkinter.CTkLabel(self, width=120, height=25, fg_color=("light blue", "blue"), corner_radius=8,anchor="center", text="Tijd", font=('Arial', 18))
        self.label.grid(row=0,column=0,padx=80,pady=10)

        self.label = customtkinter.CTkLabel(self, width=120, height=25, corner_radius=8,anchor="center", text="")
        self.label.grid(row=1,column=0,padx=0,pady=80)
        self.time()
    
    def time(self):
        now = datetime.datetime.now()
        tijd=(now.strftime("%A, %B %d %Y %H:%M:%S"))
        self.label.configure(text=f"Tijd : {tijd}", font=('Arial', 18))
        self.after(1000, self.time)


class Afstand(customtkinter.CTkFrame):
    def __init__(self, *args, master ,header_name="Afstand", **kwargs):
        super().__init__(master,*args, **kwargs)
        self.header_name = header_name

        self.label = customtkinter.CTkLabel(self, width=120, height=25, fg_color=("light blue", "blue"), corner_radius=8,anchor="center", text="Afstand tot bodem",font=('Arial', 18))
        self.label.grid(row=0,column=0,padx=80,pady=10)

        self.label = customtkinter.CTkLabel(self, width=120, height=25, corner_radius=8,anchor="center", text="Afstand: nog niet gemeten",font=('Arial', 18))
        self.label.grid(row=1,column=0,padx=0,pady=80)

        self.button = customtkinter.CTkButton(self, text='Start met lezen', command= self.distanceRead,font=('Arial', 18))
        self.button.grid(row=2,column=0,padx=0,pady=20)
    
    def distanceRead(self):
        path = os.path.join(sys.path[0], './Texts/afstand.txt')
        with open(path, 'r') as f:
            distance = f.read().strip()
        self.label.configure(text=f"Afstand : {distance}",font=('Arial', 18))
        # schedule the next update after 5 seconds
        self.after(5000, self.distanceRead)


class Temp(customtkinter.CTkFrame):
    def __init__(self, *args, master, header_name="Temperatuur", **kwargs):
        super().__init__(master,*args, **kwargs)
        self.header_name= header_name

        self.label = customtkinter.CTkLabel(self, width=120, height=25, fg_color=("dark blue", "blue"), corner_radius=8,anchor="center", text="Temperatuur Motorkamer", font=('Arial', 18))
        self.label.grid(row=0,column=0,padx=20,pady=10)


        self.label = customtkinter.CTkLabel(self, width=120, height=25, corner_radius=8,anchor="center", text="Temperatuur: nog niet gemeten", font=('Arial', 18))
        self.label.grid(row=1,column=0,padx=0,pady=80)
        
        
        self.button = customtkinter.CTkButton(self, text='Start met lezen', command= self.tempRead, font=('Arial', 18))
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

        self.label = customtkinter.CTkLabel(self, width=120, height=20, fg_color=("white", "gray75"), corner_radius=8,anchor="center", text="Besturingspaneel", font=('Arial', 18))
        self.label.grid(row=2, column=0, padx=20, pady=10)


class StatusFrame(customtkinter.CTkFrame):
    def __init__(self, *args, master,header_name="Status machine", **kwargs):
        super().__init__(master, *args, **kwargs)
        # add widgets onto the frame...

        self.header_name = header_name
        self.label = customtkinter.CTkLabel(self, width=120, height=25, fg_color=("orange", "orange"), corner_radius=8,anchor="center", text="Status Machine",font=('Arial', 18))
        self.label.grid(row=0, column=0, padx=10, pady=30)
        self.label = customtkinter.CTkLabel(self, width=120, height=25, fg_color=("red", "red"), corner_radius=8,anchor="center", text="Status Aggregraat", font=('Arial', 18))
        self.label.grid(row=1, column=0, padx=10, pady=10)
        self.label = customtkinter.CTkLabel(self, width=120, height=25, fg_color=("green", "green"), corner_radius=8,anchor="center", text="Status Compressor", font=('Arial', 18))
        self.label.grid(row=2, column=0, padx=10, pady=10)
        self.label = customtkinter.CTkLabel(self, width=120, height=25, fg_color=("green", "green"), corner_radius=8,anchor="center", text="Status Verlichting", font=('Arial', 18))
        self.label.grid(row=3, column=0, padx=10, pady=10)
        self.label = customtkinter.CTkLabel(self, width=120, height=25, fg_color=("green", "green"), corner_radius=8,anchor="center", text="Status Schuif", font=('Arial', 18))
        self.label.grid(row=4, column=0, padx=10, pady=10)
        
      


class ProgressFrame(customtkinter.CTkFrame):
    def __init__(self, *args, master,header_name="Warmlopen starten:", **kwargs):
        super().__init__(master, *args, **kwargs)
        # add widgets onto the frame...
        
        self.header_name = header_name
        self.label = customtkinter.CTkLabel(self, width=120, height=25, fg_color=("light blue", "blue"), corner_radius=8,anchor="center", text="Timer (5 minuten)", font=('Arial', 18))
        self.label.grid(row=0, column=0, padx=20, pady=10)

        self.progressbar = customtkinter.CTkProgressBar(self, height=20)
        self.progressbar.grid(row=1, column=0, padx=20, pady=80)
        self.progressbar.set(0)
        self.progressbar._border_width=(1)
        self.progressbar._progress_color=("green")
        self.progressbar._border_color=("black")
        self.progressbar._fg_color=("blue")
        self.progressbar._mode=("determinate")
        self.progressbar._determinate_speed=(1/300)

        def start_progress_bar():
            self.progressbar.start()
        
        
        self.button_1 =customtkinter.CTkButton(self, text="Start", border_width=0,corner_radius=8,width=120,command=start_progress_bar, font=('Arial', 18))
        self.button_1.grid(row=2, column=0, padx=0, pady=20)


class Besturingsmodus(customtkinter.CTkFrame):
    def __init__(self, *args, header_name="Besturingsmodus", **kwargs):
        super().__init__(*args, **kwargs)
        
        self.header_name = header_name

        self.label = customtkinter.CTkLabel(self, width=120, height=25, fg_color=("light blue", "blue"), corner_radius=8,anchor="center", text="Besturingsmodus",font=('Arial', 18))

        self.label.grid(row=0, column=0, padx=10, pady=10)

        self.radio_button_var = customtkinter.StringVar(value="")

        self.radio_button_1 = customtkinter.CTkRadioButton(self, text="Handmatig", value="Handmatig", variable=self.radio_button_var, font=('Arial', 18))
        self.radio_button_1.grid(row=1, column=0, padx=10, pady=20)
        self.radio_button_2 = customtkinter.CTkRadioButton(self, text="Automatisch", value="Automatisch", variable=self.radio_button_var, font=('Arial', 18))
        self.radio_button_2.grid(row=2, column=0, padx=10, pady=50)
        


       
   
#Lights control panel
class LightsControl(customtkinter.CTkFrame):    
    def __init__(self, *args, master, header_name="Lampen Besturing", **kwargs):
        super().__init__(master, *args, **kwargs)
        # add widgets onto the frame...
        self.header_name = header_name

        self.label = customtkinter.CTkLabel(self, width=120, height=25, fg_color=("light blue", "blue"), corner_radius=8,anchor="center", text="Richting", font=('Arial', 18))

        self.label.grid(row=0, column=0, padx=10, pady=10)

        self.radio_button_var = customtkinter.StringVar(value="")

        self.radio_button_1 = customtkinter.CTkRadioButton(self, text="Bakboord", value="Bakboord", variable=self.radio_button_var, command=self.send_value)
        self.radio_button_1.grid(row=1, column=0, padx=10, pady=20)
        self.radio_button_2 = customtkinter.CTkRadioButton(self, text="Stuurboord", value="Stuurboord", variable=self.radio_button_var,command=self.send_value)
        self.radio_button_2.grid(row=2, column=0, padx=10, pady=20)
        self.radio_button_2 = customtkinter.CTkRadioButton(self, text="Uit", value="Uit", variable=self.radio_button_var,command=self.send_value)
        self.radio_button_2.grid(row=3, column=0, padx=10, pady=20)

    def send_value(self):
        """Sends value to opdracht.txt"""
        path = os.path.join(sys.path[0], './Texts/opdracht.txt')
        lights = self.radio_button_var.get()
        with open(path, 'w') as f:
            f.write(lights)
            f.close()    

class NAPINPUT(customtkinter.CTkFrame):
    def __init__(self, *args, master, header_name="Nap input", **kwargs):
        super().__init__(master, *args, **kwargs)
        self.header_name = header_name

        self.label = customtkinter.CTkLabel(self, width=120, height=25, fg_color=("light blue", "blue"), corner_radius=8,anchor="center", text="Nap input", font=('Arial', 18))

        self.label.grid(row=0, column=0, padx=10, pady=10)


        self.entry = customtkinter.CTkEntry(self, width=80, height=25, corner_radius=10)
                
        self.entry.grid(row=1, column=0, padx=10, pady=20)

        self.napvalue=self.entry.get()

        self.napbutton = customtkinter.CTkButton(self, text="Nap versturen", command= self.send_nap, width=80, height=20, border_width=0, corner_radius=8)
        self.napbutton.grid(row=2, column=0, padx=10, pady=20)

    def send_nap(self):
        path = os.path.join(sys.path[0], './Texts/nap.txt')
        nap=self.entry.get()
        with open(path, 'w') as f:
            f.write(nap)
            f.close()    
             
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.geometry('1280x720')
        self.title("placeholder dashboard")

        self.tijd= Tijd(master=self,header_name="Tijd")
        self.tijd.grid(row=1, column=0, padx=20,pady=20)

        self.my_frame = ProgressFrame(master=self, header_name="Warmlopen starten:")
        self.my_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew") 
        
        self.radio_button_frame_1 = Besturingsmodus(self, header_name="Besturingsmodus")
        self.radio_button_frame_1.grid(row=0, column=1, padx=20, pady=20)
        
        self.my_frame2 = StatusFrame(master=self, header_name="Status machine")
        self.my_frame2.grid(row=1, column=2, padx=20, pady=20)
        
        self.temp = Temp(master=self,header_name="temp")
        self.temp.grid(row=0, column=2, padx=20,pady=20)

        self.afstand = Afstand(master=self, header_name='afstand')
        self.afstand.grid(row=0,column = 3 , padx=20, pady=20)
        
        self.light_control = LightsControl(master=self, header_name="Lampen Besturing")
        self.light_control.grid(row=1, column=1, padx=20, pady=20)

        self.NAPINPUT = NAPINPUT(master=self, header_name="Nap input")
        self.NAPINPUT.grid(row=1, column=3, padx=20, pady=20)


if __name__ == "__main__":
    app=App()
    app.mainloop()