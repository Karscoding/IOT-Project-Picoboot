from imports_n_vars import *

class Temp(customtkinter.CTkFrame):
    def __init__(self, *args, master, header_name="Temperatuur", **kwargs):
        super().__init__(master,*args, **kwargs)
        self.header_name= header_name
        
        self.fontbold = customtkinter.CTkFont(**fontbold)
        self.fontmedium = customtkinter.CTkFont(**fontmedium)

        self.label = customtkinter.CTkLabel(self, 
                                            width=120, 
                                            height=25, 
                                            text_color='#FFFFFF',
                                            corner_radius=8,
                                            anchor="center", 
                                            text="Temperatuur: nog niet gemeten",
                                            font=self.fontbold)
        
        self.label.pack(padx=70,pady=25)
        if os.getcwd().split("\\")[-1]=='Picoboot':
            self.icon=customtkinter.CTkImage(Image.open("dashboard/images/EngineTemp.png"), size=(110,110))
        else:
            self.icon=customtkinter.CTkImage(Image.open("images/EngineTemp.png"), size=(40,40))
        self.iconwindow=customtkinter.CTkLabel(master=self,image=self.icon, text="")
        self.iconwindow.place(x=20,y=20)

    def TempRead(self):
        self.label.configure(text=Reader("Temp"))
        self.after(1000, self.TempRead)