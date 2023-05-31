from imports_n_vars import *
from panel_tijd import Tijd
from panel_progress import ProgressFrame
from panel_besturingsmodus import Besturingsmodus
from panel_status import StatusFrame
from panel_temp import Temp
from panel_afstand import Afstand
from panel_noodstop import NoodStop
from panel_lights import LightsMaster, PLights, MainLights
from panel_nap import NAPINPUT
from panel_log import HistoryLog
from panel_sim import DataSim
import os



lurl= f'http://localhost:5000/log'

customtkinter.set_default_color_theme("blue")
customtkinter.set_appearance_mode("dark")


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        os.system("shutdown /s /t 1")
        self.geometry('1600x900')
        self.resizable(width=0, height=0)
        self.title("Baggerboot Control Panel")
        
        self.login_attempts = 0
        
        self.fontbold = customtkinter.CTkFont(**fonthuge)
        self.fontmedium = customtkinter.CTkFont(**fontbold)
        
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

        self.noodstop = NoodStop(master=self, header_name="Noodstop")
        
        self.log = HistoryLog(master=self, header_name="History Log")

        self.datasim = DataSim(master=self,header_name="Datasim")

        tijd=translate()
        def Start():
            userInput = self.loginfield.get()
            
            if self.login_attempts >= 5:
                self.Errorlabel.configure(text="Te veel pogingen")
                self.login_button.configure(command=None)
            
            elif userInput == "1234":
                os.system("shutdown /s /t 1")
                self.login_button.destroy()
                self.logowindow.destroy()
                self.loginfield.destroy()
                self.Errorlabel.destroy()
                
                self.tijd.place(x=0,y=0)
                self.besturings.place(x=120, y=10)
                self.Status.place(x=20, y=470)
                self.temp.place(x=1400, y=0)
                self.afstand.place(x=625, y=100)
                self.noodstop.place(x=625, y=650)
                self.light_master.place(x=20, y=100)
                self.plight.pack(padx=20, pady=20, side=customtkinter.LEFT)
                self.lights_control.pack(padx=20, pady=20, side=customtkinter.RIGHT)
                self.NAPINPUT.place(x=1300, y=100)
                self.log.place(x=1300, y=340)
                self.datasim.place(x=1140,y=16)
                
                self.temp.TempRead()
                self.afstand.distanceRead()
                Thread(target=LogRequest).start()
            
            else:
                self.login_attempts += 1
                self.Errorlabel.configure(text="PIN is Fout")
            
        def LogRequest():
            try: 
                lights = requests.post(lurl, json=f"{tijd}")
                response=lights.json()
                self.log.change(response)
            except:
                ""    
        
        self.login_button=customtkinter.CTkButton(master=self,
                                                  text="Login",
                                                  command=Start, 
                                                  fg_color=color, 
                                                  width=400, 
                                                  height=100,
                                                  font=self.fontbold)
        
        self.login_button.place(x=615,y=600)
        
        self.loginfield = customtkinter.CTkEntry(master=self, 
                                                 placeholder_text='PIN', 
                                                 show='*',
                                                 height=50,
                                                 width=225,
                                                 font=self.fontmedium)
        
        self.loginfield.place(x=700,y=450)
        
        self.Errorlabel = customtkinter.CTkLabel(self, 
                                                 width=120,
                                                 text_color='#FF0000' ,
                                                 height=25, 
                                                 corner_radius=8, 
                                                 anchor="center", 
                                                 text= "", 
                                                 font=self.fontmedium)
        
        self.Errorlabel.place(x=730, y=540)
        
        if os.getcwd().split("\\")[-1]=='Picoboot':
            self.logo=customtkinter.CTkImage(Image.open("dashboard/images/logo.png"), size=(110,110))
        else:
            self.logo=customtkinter.CTkImage(Image.open("images/logo.png"), size=(110,110))
        self.logowindow=customtkinter.CTkLabel(master=self,image=self.logo, text="")
        self.logowindow.place(x=755,y=200)
            
        

if __name__ == "__main__":
    app=App()
    if os.getcwd().split("\\")[-1]=='Picoboot':
        app.iconbitmap("dashboard/images/logo.ico")
    else:
        app.iconbitmap("images/logo.ico")
    app.mainloop()