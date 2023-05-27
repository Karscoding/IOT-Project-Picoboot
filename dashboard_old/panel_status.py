from imports import *

class StatusFrame(customtkinter.CTkFrame):
    def __init__(self, *args, master,header_name="Status machine", **kwargs):
        super().__init__(master, *args, **kwargs)
        # add widgets onto the frame...
        self.header_name = header_name
        
        self.label = customtkinter.CTkLabel(self, 
                                            width=120, 
                                            height=25, 
                                            fg_color=("orange", "orange"), 
                                            corner_radius=8,
                                            anchor="center", 
                                            text="Status Machine",
                                            font=('Arial', 18))
        
        self.label.grid(row=0, column=0, padx=10, pady=30)
        
        
        self.label = customtkinter.CTkLabel(self, 
                                            width=120, 
                                            height=25, 
                                            fg_color=("red", "red"), 
                                            corner_radius=8,
                                            anchor="center", 
                                            text="Status Aggregraat", 
                                            font=('Arial', 18))
        
        self.label.grid(row=1, column=0, padx=10, pady=10)
        
        
        self.label = customtkinter.CTkLabel(self, 
                                            width=120, 
                                            height=25, 
                                            fg_color=("green", "green"), 
                                            corner_radius=8,
                                            anchor="center", 
                                            text="Status Compressor", 
                                            font=('Arial', 18))
        
        self.label.grid(row=2, column=0, padx=10, pady=10)
        
        
        self.label = customtkinter.CTkLabel(self, 
                                            width=120, 
                                            height=25, 
                                            fg_color=("green", "green"), 
                                            corner_radius=8,
                                            anchor="center", 
                                            text="Status Verlichting", 
                                            font=('Arial', 18))
        
        self.label.grid(row=3, column=0, padx=10, pady=10)
        
        
        self.label = customtkinter.CTkLabel(self, 
                                            width=120, 
                                            height=25, 
                                            fg_color=("green", "green"), 
                                            corner_radius=8,
                                            anchor="center", 
                                            text="Status Schuif", 
                                            font=('Arial', 18))
        
        self.label.grid(row=4, column=0, padx=10, pady=10)