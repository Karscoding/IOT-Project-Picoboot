from imports_n_vars import *

class LightsMaster(customtkinter.CTkFrame):    
    def __init__(self, *args, master, header_name="Lampen Besturing", **kwargs):
        super().__init__(master, *args, **kwargs)
        # add widgets onto the frame...
        self.header_name = header_name
        
        self.font = customtkinter.CTkFont(**fontbold)

        
        self.label = customtkinter.CTkLabel(self, 
                                            width=120, 
                                            height=25, 
                                            fg_color=("light blue", color), 
                                            corner_radius=8,
                                            anchor="center", 
                                            text="Passeerlichten / Hoofdverlichting", 
                                            font=self.font)

        self.label.pack(padx=20, pady=20)

class PLights(customtkinter.CTkFrame):    
    def __init__(self, *args, master, header_name="Lampen Besturing", **kwargs):
        super().__init__(master, *args, **kwargs)
        # add widgets onto the frame...
        self.header_name = header_name
        
        self.font = customtkinter.CTkFont(**fontbold)


        self.radio_button_var = customtkinter.StringVar(value="")

        self.radio_button_1 = customtkinter.CTkRadioButton(self, 
                                                           text="Bakboord",
                                                           hover_color=color,
                                                           border_width_checked=13,
                                                           font=self.font,
                                                           value="L",
                                                           width=20, 
                                                           variable=self.radio_button_var, 
                                                           command=self.call_to_write)
        
        self.radio_button_1.pack(padx=10, pady=20)
        
        
        self.radio_button_2 = customtkinter.CTkRadioButton(self, 
                                                           text="Stuurboord",
                                                           hover_color=color,
                                                           border_width_checked=13,
                                                           font=self.font,
                                                           value="R",
                                                           width=20, 
                                                           variable=self.radio_button_var,
                                                           command=self.call_to_write)
        
        self.radio_button_2.pack(padx=10, pady=20)
        
        
        self.radio_button_2 = customtkinter.CTkRadioButton(self, 
                                                           text="Passeer UIT", 
                                                           hover_color=color,
                                                           border_width_checked=13,
                                                           font=self.font,
                                                           value="P",
                                                           width=20, 
                                                           variable=self.radio_button_var,
                                                           command=self.call_to_write)
        
        self.radio_button_2.pack(padx=10, pady=20)
        

    def call_to_write(self):
        """Sends value to opdracht.txt"""
        lights = self.radio_button_var.get()
        WritetoFile(lights)
        self.after(1000, self.call_to_write)
        
        
class MainLights(customtkinter.CTkFrame):    
    def __init__(self, *args, master, header_name="Lampen Besturing", **kwargs):
        super().__init__(master, *args, **kwargs)
        # add widgets onto the frame...
        self.header_name = header_name
        
        self.font = customtkinter.CTkFont(**fontbold)


        self.radio_button_var = customtkinter.StringVar(value="")
        
        self.radio_button_3 = customtkinter.CTkRadioButton(self, 
                                                           text="Verlichting AAN",
                                                           hover_color=color,
                                                           border_width_checked=13,
                                                           font=self.font, 
                                                           value="X",
                                                           width=20, 
                                                           variable=self.radio_button_var,
                                                           command=self.call_to_write)
        
        self.radio_button_3.pack(padx=10, pady=20)
        
        
        self.radio_button_3 = customtkinter.CTkRadioButton(self, 
                                                           text="Verlichting UIT",
                                                           hover_color=color,
                                                           border_width_checked=13,
                                                           font=self.font, 
                                                           value="U",
                                                           width=20, 
                                                           variable=self.radio_button_var,
                                                           command=self.call_to_write)
        
        self.radio_button_3.pack(padx=10, pady=20)
        
    def call_to_write(self):
        """Sends value to opdracht.txt"""
        lights = self.radio_button_var.get()
        WritetoFile(lights)
        self.after(1000, self.call_to_write)