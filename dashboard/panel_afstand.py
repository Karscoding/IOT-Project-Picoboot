from imports_n_vars import *

class Afstand(customtkinter.CTkFrame):
    def __init__(self, *args, master ,header_name="Afstand", **kwargs):
        super().__init__(master,*args, **kwargs)
        self.header_name = header_name
        
        self.fontbold = customtkinter.CTkFont(family=fontname, size=fontsizebold, weight="bold")
        self.fontmedium = customtkinter.CTkFont(family=fontname, size=fontsizemed)

        # self.label = customtkinter.CTkLabel(self, 
        #                                     width=120, 
        #                                     height=25, 
        #                                     fg_color=("light blue", "blue"), 
        #                                     corner_radius=8,anchor="center", 
        #                                     text="Afstand tot bodem",
        #                                     font=('Arial', 18))
        
        # self.label.pack(padx=80,pady=10)
        

        self.label = customtkinter.CTkLabel(self, 
                                            width=120, 
                                            height=25, 
                                            corner_radius=8,
                                            anchor="center", 
                                            text="Afstand: nog niet gemeten",
                                            font=self.fontbold)
        
        self.label.pack(padx=60,pady=10)
        
        self.icon=customtkinter.CTkImage(Image.open("images/DepthSymbol.png"), size=(40,40))
        self.iconwindow=customtkinter.CTkLabel(master=self,image=self.icon, text="")
        self.iconwindow.place(x=10,y=20)
        

        # self.button = customtkinter.CTkButton(self, 
        #                                       text='Start met lezen', 
        #                                       command=self.distanceRead,
        #                                       font=('Arial', 18))
        
        # self.button.pack(padx=0,pady=20)
    
    
    def distanceRead(self):
        path = os.path.join(sys.path[0], '../Texts/afstand.txt')
        
        with open(path, 'r') as f:
            distance = f.read().strip()
            
        self.label.configure(text=f"{distance}")
        
        # schedule the next update after 5 seconds
        self.after(5000, self.distanceRead)