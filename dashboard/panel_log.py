from imports_n_vars import *

class HistoryLog(customtkinter.CTkFrame):    
    def __init__(self, *args, master, header_name="Log", **kwargs):
        super().__init__(master, *args, **kwargs)
        self.header_name=header_name
        
        self.fontbold = customtkinter.CTkFont(**fontbold)
        self.fontmedium = customtkinter.CTkFont(**fontsmall)
        
        
        self.label = customtkinter.CTkLabel(self, 
                                            fg_color=("light blue", color), 
                                            corner_radius=8,
                                            anchor="center", 
                                            text="Log", 
                                            font=self.fontbold)

        self.label.pack(padx=108, pady=20)
        
        
        self.logbox = customtkinter.CTkLabel(self,
                                             font=self.fontmedium,
                                             text="26 Mei 19:02 - Uitgelogd\n26 Mei 10:11 - Noodstop")
        
        self.logbox.pack(padx=20, pady=20)