from imports_n_vars import *

class StatusFrame(customtkinter.CTkFrame):
    def __init__(self, *args, master,header_name="Status machine", **kwargs):
        super().__init__(master, *args, **kwargs)
        # add widgets onto the frame...
        self.header_name = header_name
        
        self.fontbold = customtkinter.CTkFont(**fontbold)
        self.fontmedium = customtkinter.CTkFont(**fontmedium)
        
        self.statuslabel = {"corner_radius":8,
                            "font":self.fontbold,
                            "fg_color":("green", "#3e8747")}
        
        self.label = customtkinter.CTkLabel(self,
                                            fg_color=("orange", color), 
                                            corner_radius=8,
                                            text="Status Machine",
                                            font=self.fontbold)
        
        self.label.pack(padx=175, pady=30)
        
        
        self.label = customtkinter.CTkLabel(self,
                                            width=300,
                                            height=50,
                                            **self.statuslabel,
                                            text="Aggregraat")
        
        self.label.pack(padx=0, pady=15)
        
        
        self.label = customtkinter.CTkLabel(self,
                                            width=300,
                                            height=50,
                                            **self.statuslabel, 
                                            text="Compressor")
        
        self.label.pack(padx=0, pady=15)
        
        
        self.label = customtkinter.CTkLabel(self,
                                            width=300,
                                            height=50,
                                            **self.statuslabel,
                                            text="Verlichting")
        
        self.label.pack(padx=0, pady=15)
        
        
        self.label = customtkinter.CTkLabel(self,
                                            width=300,
                                            height=50,
                                            **self.statuslabel, 
                                            text="Schuif")
        
        self.label.pack(padx=0, pady=15)