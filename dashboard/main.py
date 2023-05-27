from imports_n_vars import *
from panel_tijd import Tijd
from panel_progress import ProgressFrame
from panel_besturingsmodus import Besturingsmodus
from panel_status import StatusFrame
from panel_temp import Temp
from panel_afstand import Afstand
from panel_lights import LightsMaster, PLights, MainLights
from panel_nap import NAPINPUT


url = f"http://localhost:{PORT}{SENDPOINT}"

customtkinter.set_default_color_theme("blue")
customtkinter.set_appearance_mode("dark")


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.geometry('1600x900')
        self.resizable(width=0, height=0)
        self.title("Baggerboot Control Panel")
        
        self.tijd=Tijd(master=self,header_name="Tijd")
        self.tijd.place(x=0,y=0)
        

        # self.my_frame = ProgressFrame(master=self, header_name="Warmlopen starten:")
        # self.my_frame.place(x=0,y=100)
        
        
        self.besturings = Besturingsmodus(self, header_name="Besturingsmodus")
        self.besturings.place(x=120, y=10)
        
        
        self.Status = StatusFrame(master=self, header_name="Status machine")
        self.Status.place(x=20, y=470)
        
        
        self.temp=Temp(master=self,header_name="temp")
        self.temp.place(x=1400, y=0)
        self.temp.tempRead()
        

        self.afstand = Afstand(master=self, header_name='afstand')
        self.afstand.place(x=625, y=100)
        self.afstand.distanceRead()
        
        
        self.light_master = LightsMaster(master=self, header_name="Lampen Besturing")
        self.light_master.place(x=20, y=100)
        
        self.plight = PLights(master=self.light_master)
        self.plight.pack(padx=20, pady=20, side=customtkinter.LEFT)
        
        self.lights_control = MainLights(master=self.light_master)
        self.lights_control.pack(padx=20, pady=20, side=customtkinter.RIGHT)
        

        self.NAPINPUT = NAPINPUT(master=self, header_name="Nap Invoer")
        self.NAPINPUT.place(x=1300, y=100)
        

if __name__ == "__main__":
    app=App()
    app.iconbitmap("images/logo.ico")
    app.mainloop()