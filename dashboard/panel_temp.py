from imports import *

class Temp(customtkinter.CTkFrame):
    def __init__(self, *args, master, header_name="Temperatuur", **kwargs):
        super().__init__(master,*args, **kwargs)
        self.header_name= header_name

        self.label = customtkinter.CTkLabel(self, 
                                            width=120, 
                                            height=25, 
                                            fg_color=("dark blue", "blue"),
                                            corner_radius=8,anchor="center", 
                                            text="Temperatuur Motorkamer", 
                                            font=('Arial', 18))
        
        self.label.pack(padx=20,pady=10)


        self.label = customtkinter.CTkLabel(self, 
                                            width=120, 
                                            height=25, 
                                            text_color='#FFFFFF',
                                            corner_radius=8,
                                            anchor="center", 
                                            text="Temperatuur: nog niet gemeten",
                                            font=('Arial', 18))
        
        self.label.pack(padx=0,pady=80)
        
        
        self.button = customtkinter.CTkButton(self, 
                                              text='Start met lezen', 
                                              command=self.tempRead, 
                                              font=('Arial', 18))
        
        self.button.pack(padx=0,pady=20)
        

    def tempRead(self):
        path = os.path.join(sys.path[0], '../Texts/temp.txt')
        with open(path, 'r') as f:
            temp = float(f.read().strip())
        if temp > 50:
            self.label.configure(text_color='#FF0000', text=f"Temperatuur : {temp}")     
        elif temp <= 20:
            self.label.configure(text_color='#333FFF', text=f"Temperatuur : {temp}")
        else:
            self.label.configure(text_color='#FFFFFF', text=f"Temperatuur : {temp}")
        # schedule the next update after 5 seconds
        self.after(3000, self.tempRead)