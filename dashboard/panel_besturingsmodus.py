from imports_n_vars import *

class Besturingsmodus(customtkinter.CTkFrame):
    def __init__(self, *args, header_name="Besturingsmodus", **kwargs):
        super().__init__(*args, **kwargs)
        
        self.header_name = header_name
        
        self.fontbold = customtkinter.CTkFont(**fontbold)
        self.fontmedium = customtkinter.CTkFont(**fontmedium)

        self.radio_button_var = customtkinter.StringVar(value="")

        self.radio_button_1 = customtkinter.CTkRadioButton(self, 
                                                           text="Handmatig", 
                                                           value="Handmatig", 
                                                           variable=self.radio_button_var, 
                                                           command=self.call_to_write,
                                                           font=self.fontbold)
        
        self.radio_button_1.pack(padx=10, pady=20, side=customtkinter.LEFT)
        
        
        self.radio_button_2 = customtkinter.CTkRadioButton(self, 
                                                           text="Automatisch", 
                                                           value="Automatisch", 
                                                           variable=self.radio_button_var, 
                                                           command=self.call_to_write,
                                                           font=self.fontbold)
        
        self.radio_button_2.pack(padx=10, pady=20, side=customtkinter.RIGHT)
        
    def call_to_write(self):
        """Sends value to opdracht.txt"""
        mode = self.radio_button_var.get()
        Writer("ControlMode", mode)
        self.after(1000, self.call_to_write)