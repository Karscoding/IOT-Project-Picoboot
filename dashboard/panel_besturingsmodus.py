from imports import *

class Besturingsmodus(customtkinter.CTkFrame):
    def __init__(self, *args, header_name="Besturingsmodus", **kwargs):
        super().__init__(*args, **kwargs)
        
        self.header_name = header_name

        self.label = customtkinter.CTkLabel(self, 
                                            width=120, 
                                            height=25, 
                                            fg_color=("light blue", "blue"), 
                                            corner_radius=8,
                                            anchor="center", 
                                            text="Besturingsmodus",
                                            font=('Arial', 18))

        self.label.pack(padx=10, pady=10)

        self.radio_button_var = customtkinter.StringVar(value="")

        self.radio_button_1 = customtkinter.CTkRadioButton(self, 
                                                           text="Handmatig", 
                                                           value="Handmatig", 
                                                           variable=self.radio_button_var, 
                                                           font=('Arial', 18))
        
        self.radio_button_1.pack(padx=10, pady=50)
        
        
        self.radio_button_2 = customtkinter.CTkRadioButton(self, 
                                                           text="Automatisch", 
                                                           value="Automatisch", 
                                                           variable=self.radio_button_var, 
                                                           font=('Arial', 18))
        
        self.radio_button_2.pack(padx=10, pady=50)