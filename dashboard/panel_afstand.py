from imports_n_vars import *

class Afstand(customtkinter.CTkFrame):
    def __init__(self, *args, master ,header_name="Afstand", **kwargs):
        super().__init__(master,*args, **kwargs)
        self.header_name = header_name
        
        self.fontbold = customtkinter.CTkFont(**fontbold)
        self.fontmedium = customtkinter.CTkFont(**fontmedium)

        self.label = customtkinter.CTkLabel(self, 
                                            width=200, 
                                            height=45, 
                                            fg_color=("light blue", color),
                                            anchor="center", 
                                            text="Diepte",
                                            corner_radius=8,
                                            font=self.fontbold)
        
        self.label.pack(padx=220,pady=10)
        

        self.label = customtkinter.CTkLabel(self, 
                                            width=120, 
                                            height=25, 
                                            corner_radius=8,
                                            anchor="center", 
                                            text="Afstand: nog niet gemeten",
                                            font=self.fontbold)
        
        self.label.pack(padx=0,pady=200)
        
        self.icon=customtkinter.CTkImage(Image.open("images/DepthSymbol.png"), size=(40,40))
        self.iconwindow=customtkinter.CTkLabel(master=self,image=self.icon, text="")
        self.iconwindow.place(x=100,y=220)
        

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