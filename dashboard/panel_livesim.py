from imports_n_vars import *

class Livesim(customtkinter.CTkFrame):
    def __init__(self,*args,master,header_name='LiveSim', **kwargs):
        super().__init__(master, *args, **kwargs)
        self.header_name= header_name
    	
        #onzichtbare achtergrond
        self.configure(fg_color="transparent")

        if os.getcwd().split("\\")[-1]=='Picoboot':
            self.logo=customtkinter.CTkImage(Image.open("dashboard/images/drabboot.png"), size=(1200,200))
        else:
            self.logo=customtkinter.CTkImage(Image.open("images/drabboot.png"), size=(1200,200))
        
        #boot
        self.boot = customtkinter.CTkLabel(self, 
                                            width=1200, 
                                            height=200, 
                                            #bg_color="#5c000c",
                                            text="",
                                            font=customtkinter.CTkFont(size=40),
                                            image=self.logo
                                            )
        self.boot.pack()

class zand(customtkinter.CTkFrame):
    def __init__(self,*args,master,header_name='zand', **kwargs):
        super().__init__(master, *args, **kwargs)
        self.header_name= header_name

        if os.getcwd().split("\\")[-1]=='Picoboot':
            self.logo=customtkinter.CTkImage(Image.open("dashboard/images/zand.png"), size=(1200,200))
        else:
            self.logo=customtkinter.CTkImage(Image.open("images/zand.png"), size=(1200,200))
        #zand
        self.zand = customtkinter.CTkLabel(self, 
                                            width=1200, 
                                            height=200, 
                                            #bg_color="#968200",
                                            image=self.logo,
                                            text="Zand",
                                            font=customtkinter.CTkFont(size=40)
                                            )
        self.zand.pack()


class Schuif(customtkinter.CTkFrame):
    def __init__(self,*args,master,header_name='Schuif', **kwargs):
        super().__init__(master, *args, **kwargs)
        self.header_name= header_name
        #schuif
        self.schuif = customtkinter.CTkLabel(self, 
                                            width=50, 
                                            height=300, 
                                            bg_color="black",
                                            text="schuif",
                                            font=customtkinter.CTkFont(size=40)
                                            )
        self.schuif.pack()


class diepte(customtkinter.CTkFrame):
    def __init__(self,*args,master,header_name='diepte',hoogte, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.header_name = header_name

        if os.getcwd().split("\\")[-1]=='Picoboot':
            self.logo=customtkinter.CTkImage(Image.open("dashboard/images/DepthSymbol.png"), size=(50,hoogte))
        else:
            self.logo=customtkinter.CTkImage(Image.open("images/DepthSymbol.png"), size=(50,hoogte))

        #afstand
        self.afstand = customtkinter.CTkLabel(self, 
                                            width=50, 
                                            height=hoogte,
                                            #bg_color="#300e32",
                                            text=f"Afstand:NA",
                                            image=self.logo,
                                            font=customtkinter.CTkFont(size=40)
                                            )
        self.distanceRead()
        self.afstand.pack()

    def distanceRead(self):
        try:
            self.afstand.configure(text=f"Diepte : {Reader('Diepte')}")
            # schedule the next update after 5 seconds
            self.after(5000, self.distanceRead)
        except:
            self.after(5000,self.distanceRead)