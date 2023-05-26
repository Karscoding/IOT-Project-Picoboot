from imports import *

class Tijd(customtkinter.CTkFrame):
    def __init__(self,*args,master,header_name='tijd', **kwargs):
        super().__init__(master, *args, **kwargs)
        self.header_name= header_name

        self.label = self.label = customtkinter.CTkLabel(self, 
                                                         width=120, 
                                                         height=25, 
                                                         fg_color=("light blue", "blue"), 
                                                         corner_radius=8,
                                                         anchor="center", 
                                                         text="Tijd",
                                                         font=('Arial', 18))
        
        self.label.pack(padx=20,pady=10)


        self.label = customtkinter.CTkLabel(self,
                                            width=120, 
                                            height=25, 
                                            corner_radius=8,
                                            anchor="center", 
                                            text="")
        
        self.label.pack(padx=0,pady=10)
        
        self.time()
    
    def time(self):
        now = datetime.datetime.now()
        tijd = (now.strftime("%A, %B %d %Y %H:%M:%S"))
        self.label.configure(text=f"Tijd : {tijd}", font=('Arial', 18))
        self.after(1000, self.time)