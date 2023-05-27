from imports_n_vars import *
from panel_tijd import Tijd
from panel_progress import ProgressFrame
from panel_besturingsmodus import Besturingsmodus
from panel_status import StatusFrame
from panel_temp import Temp
from panel_afstand import Afstand
from panel_lights import LightsMaster, PLights, MainLights
from panel_nap import NAPINPUT
from panel_log import HistoryLog


url = f"http://localhost:{PORT}{SENDPOINT}"

customtkinter.set_default_color_theme("blue")
customtkinter.set_appearance_mode("dark")


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.geometry('1600x900')
        self.resizable(width=0, height=0)
        self.title("Baggerboot Control Panel")
        
        self.fontbold = customtkinter.CTkFont(**fonthuge)
        
        self.tijd=Tijd(master=self,header_name="Tijd")
        

        # self.my_frame = ProgressFrame(master=self, header_name="Warmlopen starten:")
        
        
        self.besturings = Besturingsmodus(master=self, header_name="Besturingsmodus")
        
        
        self.Status = StatusFrame(master=self, header_name="Status machine")
        
        
        self.temp=Temp(master=self,header_name="temp")
        

        self.afstand = Afstand(master=self, header_name='afstand')
        
        
        self.light_master = LightsMaster(master=self, header_name="Lampen Besturing")
        
        self.plight = PLights(master=self.light_master)
        
        self.lights_control = MainLights(master=self.light_master)
        

        self.NAPINPUT = NAPINPUT(master=self, header_name="Nap Invoer")
        
        self.log = HistoryLog(master=self, header_name="History Log")
        
        def Start():
            self.login_button.destroy()
            self.tijd.place(x=0,y=0)
            # self.my_frame.place(x=0,y=100)
            self.besturings.place(x=120, y=10)
            self.Status.place(x=20, y=470)
            self.temp.place(x=1400, y=0)
            self.temp.tempRead()
            self.afstand.place(x=625, y=100)
            self.afstand.distanceRead()
            self.light_master.place(x=20, y=100)
            self.plight.pack(padx=20, pady=20, side=customtkinter.LEFT)
            self.lights_control.pack(padx=20, pady=20, side=customtkinter.RIGHT)
            self.NAPINPUT.place(x=1300, y=100)
            self.log.place(x=1300, y=340)
            
        self.login_button=customtkinter.CTkButton(master=self,
                                                  text="Start",
                                                  command=Start, 
                                                  fg_color=color, 
                                                  width=400, 
                                                  height=100,
                                                  font=self.fontbold)
        
        self.login_button.place(x=615,y=375)
            
        

if __name__ == "__main__":
    app=App()
    app.iconbitmap("images/logo.ico")
    app.mainloop()