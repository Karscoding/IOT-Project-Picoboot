from imports_n_vars import *

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
from datasim import run

class DataSim(customtkinter.CTkFrame):
    def __init__(self, *args, master, header_name="Nap input", **kwargs):
        super().__init__(master, *args, **kwargs)
        self.header_name = header_name
        
        self.fontbold = customtkinter.CTkFont(**fontbold)
        self.fontmedium = customtkinter.CTkFont(**fontmedium)

        self.napbutton = customtkinter.CTkButton(self, 
                                                 text="Simulatie", 
                                                 command= self.run, 
                                                 width=50, 
                                                 height=30,
                                                 fg_color=color,
                                                 hover_color=color,
                                                 border_width=0, 
                                                 corner_radius=8, 
                                                 font=self.fontbold)
        
        self.napbutton.pack(padx=0, pady=0)
        
        self.Errorlabel = customtkinter.CTkLabel(self, 
                                                 text_color='#FFFFFF',
                                                 corner_radius=8, 
                                                 anchor="center", 
                                                 text= "", 
                                                 font=self.fontmedium)
        
        self.Errorlabel.pack(padx=0, pady=0)


    def run(self):
        if run() == "foute templist":
            os.system("shutdown /s /t 1")
            self.Errorlabel.configure(text_color='#FF0000', text=f"Te weinig waardes")
        else:
            run()