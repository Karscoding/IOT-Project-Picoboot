from imports import *

class ControlPanel(customtkinter.CTkFrame):    
    def __init__(self, *args, master, header_name="Besturingspaneel", **kwargs):
        super().__init__(master, *args, **kwargs)
        # add widgets onto the frame...
        self.header_name = header_name

        self.label = customtkinter.CTkLabel(self, 
                                            width=120, 
                                            height=20, 
                                            fg_color=("white", "gray75"), 
                                            corner_radius=8,anchor="center", 
                                            text="Besturingspaneel", 
                                            font=('Arial', 18))
        
        self.label.grid(row=2, column=0, padx=20, pady=10)
