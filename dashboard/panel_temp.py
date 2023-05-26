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
        
        self.label.grid(row=0,column=0,padx=20,pady=10)


        self.label = customtkinter.CTkLabel(self, 
                                            width=120, 
                                            height=25, 
                                            corner_radius=8,
                                            anchor="center", 
                                            text="Temperatuur: nog niet gemeten",
                                            font=('Arial', 18))
        
        self.label.grid(row=1,column=0,padx=0,pady=80)
        
        
        self.button = customtkinter.CTkButton(self, 
                                              text='Start met lezen', 
                                              command=self.tempRead, 
                                              font=('Arial', 18))
        
        self.button.grid(row=2,column=0,padx=0,pady=20)
        

    def tempRead(self):
        path = os.path.join(sys.path[0], '../Texts/temp.txt')
        with open(path, 'r') as f:
            temp = f.read().strip()
        self.label.configure(text=f"Temperatuur : {temp}")
        # schedule the next update after 5 seconds
        self.after(5000, self.tempRead)