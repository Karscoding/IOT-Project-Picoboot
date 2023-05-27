from imports import *

class Besturingsmodus(customtkinter.CTkFrame):
    def __init__(self, *args, header_name="Besturingsmodus", **kwargs):
        super().__init__(*args, **kwargs)
        
        self.header_name = header_name
        
        self.fontbold = customtkinter.CTkFont(family=fontname, size=fontsizebold, weight="bold")
        self.fontmedium = customtkinter.CTkFont(family=fontname, size=fontsizemed)

        self.label = customtkinter.CTkLabel(self, 
                                            width=120, 
                                            fg_color=("light blue", color), 
                                            corner_radius=8,
                                            anchor="center", 
                                            text="Besturingsmodus",
                                            font=self.fontbold)

        self.label.pack(padx=10, pady=20)

        self.radio_button_var = customtkinter.StringVar(value="")

        self.radio_button_1 = customtkinter.CTkRadioButton(self, 
                                                           text="Handmatig", 
                                                           value="Handmatig", 
                                                           variable=self.radio_button_var, 
                                                           font=('Arial', 18))
        
        self.radio_button_1.pack(padx=10, pady=20)
        
        
        self.radio_button_2 = customtkinter.CTkRadioButton(self, 
                                                           text="Automatisch", 
                                                           value="Automatisch", 
                                                           variable=self.radio_button_var, 
                                                           font=('Arial', 18))
        
        self.radio_button_2.pack(padx=10, pady=20)