from imports_n_vars import *

class Temp(customtkinter.CTkFrame):
    def __init__(self, *args, master, header_name="Temperatuur", **kwargs):
        super().__init__(master,*args, **kwargs)
        self.header_name= header_name
        
        self.fontbold = customtkinter.CTkFont(**fontbold)
        self.fontmedium = customtkinter.CTkFont(**fontmedium)

        # self.label = customtkinter.CTkLabel(self, 
        #                                     width=120, 
        #                                     height=25, 
        #                                     fg_color=("dark blue", color),
        #                                     corner_radius=8,anchor="center", 
        #                                     text="Temperatuur Motorkamer", 
        #                                     font=self.fontbold)
        
        # self.label.pack(padx=20,pady=10)


        self.label = customtkinter.CTkLabel(self, 
                                            width=120, 
                                            height=25, 
                                            text_color='#FFFFFF',
                                            corner_radius=8,
                                            anchor="center", 
                                            text="Temperatuur: nog niet gemeten",
                                            font=self.fontbold)
        
        self.label.pack(padx=70,pady=25)
        
        self.icon=customtkinter.CTkImage(Image.open("images/EngineTemp.png"), size=(40,40))
        self.iconwindow=customtkinter.CTkLabel(master=self,image=self.icon, text="")
        self.iconwindow.place(x=20,y=20)
        
        
        # self.button = customtkinter.CTkButton(self, 
        #                                       text='Start met lezen', 
        #                                       command=self.tempRead, 
        #                                       font=('Arial', 18))
        
        # self.button.pack(padx=0,pady=20)
        

    def tempRead(self):
        path = os.path.join(sys.path[0], '../Texts/temp.txt')
        with open(path, 'r') as f:
            temp = float(f.read().strip())
        if temp > 50:
            self.label.configure(text_color='#FF0000', text=f"{temp}°C")     
        elif temp <= 20:
            self.label.configure(text_color='#333FFF', text=f"{temp}°C")
        else:
            self.label.configure(text_color='#FFFFFF', text=f"{temp}°C")
        # schedule the next update after 5 seconds
        self.after(3000, self.tempRead)