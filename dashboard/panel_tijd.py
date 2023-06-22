from imports_n_vars import *

class Tijd(customtkinter.CTkFrame):
    def __init__(self,*args,master,header_name='tijd', **kwargs):
        super().__init__(master, *args, **kwargs)
        self.header_name= header_name
        
        self.font = customtkinter.CTkFont(size=40)
        
        self.tijdlabel = customtkinter.CTkLabel(self,
                                            anchor="center",
                                            text="",
                                            font=self.font)
        
        self.tijdlabel.place(x=640, y=25)
        
        self.filling = customtkinter.CTkLabel(self,
                                              text="")
        
        self.filling.pack(padx=1000, pady=40)
        
        if os.getcwd().split("\\")[-1]=='Picoboot':
            self.logo=customtkinter.CTkImage(Image.open("dashboard/images/logo.png"), size=(110,110))
        else:
            print(os.getcwd())
            self.logo=customtkinter.CTkImage(Image.open("images/logo.png"), size=(110,110))
        self.logowindow=customtkinter.CTkLabel(master=self,image=self.logo, text="")
        self.logowindow.place(x=0,y=0)
        
        self.time()
    
    def time(self):
        tijd = translate()
        self.tijdlabel.configure(text=f"{tijd}")
        self.after(1000, self.time)