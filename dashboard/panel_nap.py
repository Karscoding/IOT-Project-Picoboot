from imports_n_vars import *

class NAPINPUT(customtkinter.CTkFrame):
    def __init__(self, *args, master, header_name="Nap input", **kwargs):
        super().__init__(master, *args, **kwargs)
        self.header_name = header_name
        
        self.fontbold = customtkinter.CTkFont(**fontbold)
        self.fontmedium = customtkinter.CTkFont(**fontmedium)
        

        self.entry = customtkinter.CTkEntry(self, 
                                            width=200, 
                                            height=50, 
                                            corner_radius=10,
                                            font=self.fontbold)
                
        self.entry.pack(padx=0, pady=20)
        

        

        self.napbutton = customtkinter.CTkButton(self, 
                                                 text="Nap Instellen", 
                                                 command= self.send_nap, 
                                                 width=110, 
                                                 height=40,
                                                 fg_color=color,
                                                 hover_color=color,
                                                 border_width=0, 
                                                 corner_radius=8, 
                                                 font=self.fontbold)
        
        self.napbutton.pack(padx=40, pady=10)
        
        self.napvalue=self.entry.get()
        self.Errorlabel = customtkinter.CTkLabel(self, 
                                                 width=120,
                                                 text_color='#FFFFFF' ,
                                                 height=25, 
                                                 corner_radius=8, 
                                                 anchor="center", 
                                                 text= "", 
                                                 font=self.fontmedium)
        
        self.Errorlabel.pack(padx=0, pady=20)


    def send_nap(self):
        path = os.path.join(sys.path[0], '../Texts/nap.txt')
        nap=self.entry.get()
        if float(nap) >= -1 and float(nap) <=1:
            self.Errorlabel.configure(text_color='#FFFFFF', text=f"NAP is : {nap}")
            with open(path, 'w') as f:
                f.write(nap)
                f.close() 
        else:
            self.Errorlabel.configure(text_color='#FF0000', text=f"NAP waarde error")