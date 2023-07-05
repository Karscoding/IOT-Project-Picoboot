from imports_n_vars import *
url = f'http://localhost:5000/get'
auth="TeamH1"
class LightsMaster(customtkinter.CTkFrame):    
    def __init__(self, *args, master, header_name="Lampen Besturing", **kwargs):
        super().__init__(master, *args, **kwargs)
        # add widgets onto the frame...
        self.header_name = header_name
        
        self.font = customtkinter.CTkFont(**fonthuge)

        
        self.label = customtkinter.CTkLabel(self,
                                            corner_radius=8,
                                            anchor="center", 
                                            text="Passeerlichten / Hoofdverlichting", 
                                            font=self.font)

        self.label.pack(padx=20, pady=20)

class PLights(customtkinter.CTkFrame):    
    def __init__(self, *args, master, header_name="Lampen Besturing", **kwargs):
        super().__init__(master, *args, **kwargs)
        # add widgets onto the frame...
        text={Reader("ControlMode")}
        if text == {"Handmatig"}:
            self.header_name = header_name
            
            self.font = customtkinter.CTkFont(**fonthuge)


            self.radio_button_var = customtkinter.StringVar(value="")
            
            self.radiobutton = {"hover_color":color,
                                "border_width_checked":13,
                                "font":self.font,
                                "variable":self.radio_button_var,
                                "command":self.call_to_write}

            self.radio_button_1 = customtkinter.CTkRadioButton(self, 
                                                            text="   Bakboord   ",
                                                            **self.radiobutton,
                                                            value="Links")
            
            self.radio_button_1.pack(padx=40, pady=30)
            
            
            self.radio_button_2 = customtkinter.CTkRadioButton(self, 
                                                            text="  Stuurboord ",
                                                            **self.radiobutton,
                                                            value="Rechts")
            
            self.radio_button_2.pack(padx=40, pady=30)
            
            
            self.radio_button_2 = customtkinter.CTkRadioButton(self, 
                                                            text=" Passeer UIT ", 
                                                            **self.radiobutton,
                                                            value="Uit")
            
            self.radio_button_2.pack(padx=40, pady=30)
        elif text == {'Automatisch'}:
            self.font= customtkinter.CTkFont(**fonthuge)
            self.label = customtkinter.CTkLabel(self, 
                                        width=120, 
                                        height=25, 
                                        corner_radius=8,
                                        anchor="center", 
                                        text="besturing staat\n op automatisch",
                                        font=self.font)
            self.label.pack(padx=20,pady=125)
            choises = ["Rechts","Links"]
            Writer("InstructionPass",random.choice(choises))
            return    

    def call_to_write(self):
        """Sends value to opdracht.txt"""
        lights = self.radio_button_var.get()
        Writer("InstructionPass", lights)
        self.after(1000, self.call_to_write)
        
        
class MainLights(customtkinter.CTkFrame):    
    def __init__(self, *args, master, header_name="Lampen Besturing", **kwargs):
        super().__init__(master, *args, **kwargs)
        # add widgets onto the frame...
        self.header_name = header_name
        
        self.font = customtkinter.CTkFont(**fonthuge)


        self.radio_button_var = customtkinter.StringVar(value="")
        
        self.radiobutton = {"hover_color":color,
                            "border_width_checked":13,
                            "font":self.font,
                            "variable":self.radio_button_var,
                            "command":self.call_to_write}
        
        self.radio_button_3 = customtkinter.CTkRadioButton(self, 
                                                           text="Verlichting AAN",
                                                           **self.radiobutton,
                                                           value="Aan")
        
        self.radio_button_3.pack(padx=40, pady=39)
        
        
        self.radio_button_3 = customtkinter.CTkRadioButton(self, 
                                                           text="Verlichting UIT",
                                                           **self.radiobutton,
                                                           value="Uit")
        
        self.radio_button_3.pack(padx=40, pady=39)
        
    def call_to_write(self):
        """Sends value to opdracht.txt"""
        lights = self.radio_button_var.get()
        Writer("InstructionAll", lights)
        self.after(1000, self.call_to_write)