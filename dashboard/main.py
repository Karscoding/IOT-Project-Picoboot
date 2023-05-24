from imports import *
from panel_tijd import Tijd
from panel_progress import ProgressFrame
from panel_besturingsmodus import Besturingsmodus
from panel_status import StatusFrame
from panel_temp import Temp
from panel_afstand import Afstand
from panel_lights import LightsControl
from panel_nap import NAPINPUT


url = f"http://localhost:{config.PORT}{config.SENDPOINT}"

customtkinter.set_default_color_theme("blue")
customtkinter.set_appearance_mode("dark")


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
        self.afstand.grid(row=0,column=3 , padx=20, pady=20)
        
        
        self.light_control = LightsControl(master=self, header_name="Lampen Besturing")
        self.light_control.grid(row=1, column=3, padx=20, pady=20)
        

        self.NAPINPUT = NAPINPUT(master=self, header_name="Nap input")
        self.NAPINPUT.grid(row=1, column=1, padx=20, pady=20)
        

if __name__ == "__main__":
    app=App()
    app.mainloop()