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
import hashlib
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
from panel_livesim import Livesim, diepte, Schuif,zand
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
            (1 t/ 4 else Error
            
            
            ! Page Numbers : !
            Inlogpagina        - 0
            VerlichtingsPagina - 1
            Operationeel       - 2
            Machine            - 3
            LiveSim            - 4
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
            
            elif self.current_page ==4:
                self.livesim.destroy()
                self.zand.destroy()
                self.schuif.destroy()
                self.afstand.destroy()


            if pageTo == 1:
                self.light_master = LightsMaster(master=self, header_name="Lampen Besturing")
                self.plight = PLights(master=self.light_master)
                self.lights_control = MainLights(master=self.light_master)
                
                self.light_master.place(x=260, y=190)
                self.plight.pack(padx=75, pady=75, side=customtkinter.LEFT)
                self.lights_control.pack(padx=75, pady=75, side=customtkinter.RIGHT)
                
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
                self.afstand.place(x=160, y=132)
                self.noodstop.place(x=160, y=653)
                self.log.place(x=1300, y=340)
                self.datasim.place(x=1000,y=16)
                
                self.current_page = 2
            
            elif pageTo == 3:
                self.Status = StatusFrame(master=self, header_name="Status machine")

                self.Status.place(x=160, y=132)
                
                self.current_page = 3
            
            elif pageTo ==4:
                diepteafstand=Reader("Diepte")
                mainy=300-((diepteafstand-2)*75)

                self.livesim=Livesim(master=self,header_name="LiveSim")
                self.zand=zand(master=self,header_name="zand")
                self.schuif=Schuif(master=self,header_name="schuif")
                self.afstand=diepte(master=self,header_name="diepte",hoogte=750-mainy-200)

                self.livesim.place(x=200,y=mainy)
                self.zand.place(x=200,y=750)
                self.schuif.place(x=1200,y=mainy+200)
                self.afstand.place(y=mainy+200,x=800)

                self.current_page=4
                def update():
                    if self.current_page!=4:
                        return
                    else:
                        try:
                            self.livesim.destroy()
                            self.zand.destroy()
                            self.schuif.destroy()
                            self.afstand.destroy()

                            diepteafstand=Reader("Diepte")
                            mainy=300-((diepteafstand-2)*75)

                            self.livesim=Livesim(master=self,header_name="LiveSim")
                            self.zand=zand(master=self,header_name="zand")
                            self.schuif=Schuif(master=self,header_name="schuif")
                            self.afstand=diepte(master=self,header_name="diepte",hoogte=750-mainy-200)

                            self.livesim.place(x=200,y=mainy)
                            self.zand.place(x=200,y=750)

                            if mainy> 250:
                                self.schuif.place(x=1200,y=460)
                            else:
                                self.schuif.place(x=1200,y=mainy+200)
                            self.afstand.place(y=mainy+200,x=800)

                            self.current_page=4
                            sleep(5)
                            update()
                        except:
                            ""
                Thread(target=update).start()

            else:
                raise ValueError(f"Foute pagina nummer gegeven")
        
        self.geometry('1600x900')
        self.resizable(width=0, height=0)
        self.title("Baggerboot Control Panel")
        
        
        self.login_attempts = 0
        
        
        self.current_page = 0
        
        
        self.tijd= Tijd(master=self,header_name="Tijd")

        self.tijd.place(x=0,y=0)
        
        
        self.tab_bar = customtkinter.CTkFrame(master=self)
        
        self.lights_tab = customtkinter.CTkButton(master=self.tab_bar,
                                                  width=100,
                                                  height=100,
                                                  text="V",
                                                  font=self.fontbold,
                                                  command= lambda: PageChange(self, 1))
        
        self.operations_tab = customtkinter.CTkButton(master=self.tab_bar,
                                                  width=100,
                                                  height=100,
                                                  text="O",
                                                  font=self.fontbold,
                                                  command= lambda: PageChange(self, 2))
        
        self.machine_tab = customtkinter.CTkButton(master=self.tab_bar,
                                                  width=100,
                                                  height=100,
                                                  text="M",
                                                  font=self.fontbold,
                                                  command= lambda: PageChange(self, 3))
        
        self.livesim_tab= customtkinter.CTkButton(master=self.tab_bar,
                                                  width=100,
                                                  height=100,
                                                  text="LS",
                                                  font=self.fontbold,
                                                  command=lambda: PageChange(self,4)
                                                  )


        tijd=translate()
        
        
        def Login():
            """
            Functie wordt opgeroepen bij het klikken van inlog knop.
            Deze functie zal alle inlog dingen weghalen en alles van de dashboard plaatsen.
            
            ! Als je een nieuw paneel toevoegt zet hem hier in ! 
            
            """
            userInput = self.loginfield.get()
            var = userInput.encode('utf-8')
            hashedInput = hashlib.sha1(var).hexdigest()
            if self.login_attempts >= 4:
                self.Errorlabel.configure(text="Te veel pogingen")
                self.login_button.configure(command=None)
            
            elif hashedInput == "7110eda4d09e062aa5e4a390b0a572ac0d2c0220":
                self.tab_bar.place(x=0, y=113)
                self.lights_tab.pack(padx=20, pady=50)
                self.operations_tab.pack(padx=20, pady=50)
                self.machine_tab.pack(padx=20, pady=50)
                self.livesim_tab.pack(padx=20,pady=50)
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