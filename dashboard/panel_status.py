from imports import *

class StatusFrame(customtkinter.CTkFrame):
    def __init__(self, *args, master,header_name="Status machine", **kwargs):
        super().__init__(master, *args, **kwargs)
        # add widgets onto the frame...
        self.header_name = header_name
        
        self.fontbold = customtkinter.CTkFont(family=fontname, size=30, weight="bold")
        self.fontmedium = customtkinter.CTkFont(family=fontname, size=26)
        
        self.label = customtkinter.CTkLabel(self, 
                                            width=120, 
                                            height=25, 
                                            fg_color=("orange", color), 
                                            corner_radius=8,
                                            anchor="center", 
                                            text="Status Machine",
                                            font=self.fontbold)
        
        self.label.pack(padx=75, pady=20)
        
        
        self.label = customtkinter.CTkLabel(self, 
                                            width=120, 
                                            height=25, 
                                            fg_color=("red", "#3F8748"), 
                                            corner_radius=8,
                                            anchor="center", 
                                            text="Aggregraat", 
                                            font=self.fontmedium)
        
        self.label.pack(padx=75, pady=10)
        
        
        self.label = customtkinter.CTkLabel(self, 
                                            width=120, 
                                            height=25, 
                                            fg_color=("green", "#3F8748"), 
                                            corner_radius=8,
                                            anchor="center", 
                                            text="Compressor", 
                                            font=self.fontmedium)
        
        self.label.pack(padx=75, pady=10)
        
        
        self.label = customtkinter.CTkLabel(self, 
                                            width=120, 
                                            height=25, 
                                            fg_color=("green", "#3F8748"), 
                                            corner_radius=8,
                                            anchor="center", 
                                            text="Verlichting", 
                                            font=self.fontmedium)
        
        self.label.pack(padx=75, pady=10)
        
        
        self.label = customtkinter.CTkLabel(self, 
                                            width=120, 
                                            height=25, 
                                            fg_color=("green", "#3F8748"), 
                                            corner_radius=8,
                                            anchor="center", 
                                            text="Schuif", 
                                            font=self.fontmedium)
        
        self.label.pack(padx=75, pady=10)