from imports_n_vars import *

class StatusFrame(customtkinter.CTkFrame):
    def __init__(self, *args, master,header_name="Status machine", **kwargs):
        super().__init__(master, *args, **kwargs)
        # add widgets onto the frame...
        self.header_name = header_name
        
        self.fonthuge = customtkinter.CTkFont(**fonthuge)
        self.fontmedium = customtkinter.CTkFont(**fontmedium)
        
        self.statuslabel = {"corner_radius":8,
                            "font":self.fonthuge,
                            "fg_color":("green", "#3e8747")}
        
        self.label = customtkinter.CTkLabel(self,
                                            fg_color=("orange", color), 
                                            corner_radius=8,
                                            text="Status Machine",
                                            font=self.fonthuge)
        
        self.label.pack(padx=70, pady=30)
        
        
        self.label = customtkinter.CTkLabel(self,
                                            width=300,
                                            height=50,
                                            **self.statuslabel,
                                            text="Aggregraat")
        
        self.label.pack(padx=0, pady=50)
        
        
        self.label = customtkinter.CTkLabel(self,
                                            width=300,
                                            height=50,
                                            **self.statuslabel, 
                                            text="Compressor")
        
        self.label.pack(padx=0, pady=50)
        
        
        self.label = customtkinter.CTkLabel(self,
                                            width=300,
                                            height=50,
                                            **self.statuslabel,
                                            text="Verlichting")
        
        self.label.pack(padx=0, pady=50)
        
        
        self.label = customtkinter.CTkLabel(self,
                                            width=300,
                                            height=50,
                                            **self.statuslabel, 
                                            text="Schuif")
        
        self.label.pack(padx=0, pady=50)