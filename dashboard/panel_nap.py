from imports import *

class NAPINPUT(customtkinter.CTkFrame):
    def __init__(self, *args, master, header_name="Nap input", **kwargs):
        super().__init__(master, *args, **kwargs)
        self.header_name = header_name
        
        self.label = customtkinter.CTkLabel(self, 
                                            width=160, 
                                            height=25, 
                                            fg_color=("light blue", "blue"), 
                                            corner_radius=8,
                                            anchor="center", 
                                            text="Nap input", 
                                            font=('Arial', 18))
        
        self.label.grid(row=0, column=0, padx=10, pady=10)


        self.entry = customtkinter.CTkEntry(self, 
                                            width=120, 
                                            height=25, 
                                            corner_radius=10)
                
        self.entry.grid(row=1, column=0, padx=10, pady=40)
        

        self.napvalue=self.entry.get()
        self.Errorlabel = customtkinter.CTkLabel(self, 
                                                 width=120,
                                                 text_color='#FFFFFF' ,
                                                 height=25, 
                                                 corner_radius=8, 
                                                 anchor="center", 
                                                 text= "nap invoeren!", 
                                                 font=('Arial', 18), )
        
        self.Errorlabel.grid(row=2, column=0, padx=10, pady=10)
        

        self.napbutton = customtkinter.CTkButton(self, 
                                                 text="Nap versturen", 
                                                 command= self.send_nap, 
                                                 width=120, 
                                                 height=20, 
                                                 border_width=0, 
                                                 corner_radius=8, 
                                                 font=('Arial', 18) )
        
        self.napbutton.grid(row=3, column=0, padx=10, pady=10)


    def send_nap(self):
        path = os.path.join(sys.path[0], './Texts/nap.txt')
        nap=self.entry.get()
        if float(nap) >= -1 and float(nap) <=1:
            self.Errorlabel.configure(text_color='#FFFFFF', text=f"NAP is : {nap}")
            with open(path, 'w') as f:
                f.write(nap)
                f.close() 
        else:
            self.Errorlabel.configure(text_color='#FF0000', text=f"NAP waarde error")