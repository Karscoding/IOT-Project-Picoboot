from imports import *

class Tijd(customtkinter.CTkFrame):
    def __init__(self,*args,master,header_name='tijd', **kwargs):
        super().__init__(master, *args, **kwargs)
        self.header_name= header_name
        
        self.font = customtkinter.CTkFont(family=fontname, size=fontsizebold, weight="bold")
        
        self.tijdlabel = customtkinter.CTkLabel(self,
                                            anchor="center", 
                                            text="",
                                            font=self.font)
        
        self.tijdlabel.pack(ipadx=615, ipady=25)
        
        self.logo=customtkinter.CTkImage(Image.open("images/logo.png"), size=(80,80))
        self.logowindow=customtkinter.CTkLabel(master=self,image=self.logo, text="")
        self.logowindow.place(x=0,y=0)
        
        self.time()
    
    def time(self):
        now = datetime.datetime.now()
        tijd = (now.strftime("%A, %B %d %Y %H:%M:%S"))
        self.tijdlabel.configure(text=f"{tijd}")
        self.after(1000, self.time)