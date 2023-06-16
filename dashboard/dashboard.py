# - Picoboot Dashboard -
#
# Dit bestand is waar de dashboard in zit.
# Als dit bestand wordt geopend krijg je het dashboard te zien.
# Dit bestand pakt alle andere .py bestanden in deze folder en brengt ze samen.
# 
# Om een nieuwe widget aan te maken is het het beste om het in een nieuw bestand te doen.
# Noem dit bestand panel_<naam>.py.
# Daarna kun je die hier importen en toevoegen zoals de comments verderop zullen aangeven.
# Hou het netjes :)
# 
# - Picoboot Team 2023 -
#


# Imports
from imports_n_vars import *
from panel_tijd import Tijd
from panel_progress import ProgressFrame
from panel_besturingsmodus import Besturingsmodus
from panel_status import StatusFrame
from panel_temp import Temp
from panel_afstand import afst
from panel_noodstop import NoodStop
from panel_lights import LightsMaster, PLights, MainLights
from panel_nap import NAPINPUT
from panel_log import HistoryLog
from panel_sim import DataSim
import os

url = f'http://localhost:5000/log'

customtkinter.set_default_color_theme("blue")
customtkinter.set_appearance_mode("dark")


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        
        # Voor Fullscreen Un-Comment onderstaande tussen de streepjes
        # - - - - - - - - - 
        # self.attributes("-fullscreen",True)
        # - - - - - - - - -
        # End
        
        
        self.fontbold = customtkinter.CTkFont(**fonthuge)
        self.fontmedium = customtkinter.CTkFont(**fontbold)
        
        def PageChange(self, pageTo):
            """
            ! Veranderd de Pagina in beeld. !
            Dit doet hij door middel van self.current_page en pageTo.
            Eerst kijkt hij met current_page op welke page hij op dit moment zit.
            Dan destroy()'d hij alle elements van die pagina zodat het beeld blank is.
            Daarna kijkt hij naar pageTo en plaatst hij elementen van deze genoemde pagina.
            
            
            ! pageTo = integer !
            (1 t/m 3) else Error
            
            
            ! Page Numbers : !
            VerlichtingsPagina - 1
            Operationeel       - 2
            Machine            - 3
            """
            
            if self.current_page == 0:
                self.login_button.destroy()
                self.logowindow.destroy()
                self.loginfield.destroy()
                self.Errorlabel.destroy()
            
            elif self.current_page == 1:
                self.light_master.destroy()
                self.plight.destroy()
                self.lights_control.destroy()
                
            elif self.current_page == 2:
                self.besturings.destroy()
                self.temp.destroy()
                self.afstand.destroy()
                self.noodstop.destroy()
                self.log.destroy()
                self.datasim.destroy()
                
            elif self.current_page == 3:
                self.Status.destroy()
                
            if pageTo == 1:
                self.light_master = LightsMaster(master=self, header_name="Lampen Besturing")
                self.plight = PLights(master=self.light_master)
                self.lights_control = MainLights(master=self.light_master)
                
                self.light_master.place(x=400, y=100)
                self.plight.pack(padx=20, pady=20, side=customtkinter.LEFT)
                self.lights_control.pack(padx=20, pady=20, side=customtkinter.RIGHT)
                
                self.current_page = 1
                
            elif pageTo == 2:
                self.besturings = Besturingsmodus(master=self, header_name="Besturingsmodus")
                self.temp= Temp(master=self,header_name="temp")
                self.afstand = afst(master=self, header_name='afstand')
                self.NAPINPUT = NAPINPUT(master=self, header_name="Nap Invoer")
                self.noodstop = NoodStop(master=self, header_name="Noodstop")
                self.log = HistoryLog(master=self, header_name="History Log")
                self.datasim = DataSim(master=self,header_name="Datasim")
                
                self.besturings.place(x=100, y=10)
                self.temp.place(x=1400, y=0)
                self.afstand.place(x=625, y=100)
                self.noodstop.place(x=625, y=650)
                self.log.place(x=1300, y=340)
                self.datasim.place(x=900,y=16)
                
                self.current_page = 2
            
            elif pageTo == 3:
                self.Status = StatusFrame(master=self, header_name="Status machine")

                self.Status.place(x=500, y=470)
                
                self.current_page = 3
            
            else:
                raise ValueError(f"Foute pagina nummer gegeven")
        
        self.geometry('1600x900')
        self.resizable(width=0, height=0)
        self.title("Baggerboot Control Panel")
        
        
        self.login_attempts = 0
        
        
        self.current_page = 0
        
        
        self.tijd= Tijd(master=self,header_name="Tijd")

        self.tijd.place(x=0,y=0)
        
        
        self.lights_tab = customtkinter.CTkButton(master=self,
                                                  width=100,
                                                  height=100,
                                                  text="V",
                                                  font=self.fontbold,
                                                  command= lambda: PageChange(self, 1))
        
        self.operations_tab = customtkinter.CTkButton(master=self,
                                                  width=100,
                                                  height=100,
                                                  text="O",
                                                  font=self.fontbold,
                                                  command= lambda: PageChange(self, 2))
        
        self.machine_tab = customtkinter.CTkButton(master=self,
                                                  width=100,
                                                  height=100,
                                                  text="M",
                                                  font=self.fontbold,
                                                  command= lambda: PageChange(self, 3))


        tijd=translate()
        
        
        def Login():
            """
            Functie wordt opgeroepen bij het klikken van inlog knop.
            Deze functie zal alle inlog dingen weghalen en alles van de dashboard plaatsen.
            
            ! Als je een nieuw paneel toevoegt zet hem hier in ! 
            
            """
            userInput = self.loginfield.get()
            
            if self.login_attempts >= 4:
                self.Errorlabel.configure(text="Te veel pogingen")
                self.login_button.configure(command=None)
            
            elif userInput == "1234":
                self.lights_tab.place(x=20, y=300)
                self.operations_tab.place(x=20, y=500)
                self.machine_tab.place(x=20, y=700)
                PageChange(self, 2)
                Thread(target=LogRequest).start()
            
            else:
                self.login_attempts += 1
                self.Errorlabel.configure(text="PIN is Fout")
            
        def LogRequest():
            """
            Plaatst een post request naar de app.py Flask Server.
            Hierin worden dingen gelogged.
            """
            try: 
                lights = requests.post(url , json=f"{tijd}")
                response=lights.json()
                self.log.change(response)
            except:
                ""    
        
        self.login_button=customtkinter.CTkButton(master=self,
                                                  text="Login",
                                                  command=Login,
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