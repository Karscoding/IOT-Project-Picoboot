from imports import *

class LightsControl(customtkinter.CTkFrame):    
    def __init__(self, *args, master, header_name="Lampen Besturing", **kwargs):
        super().__init__(master, *args, **kwargs)
        # add widgets onto the frame...
        self.header_name = header_name

        self.label = customtkinter.CTkLabel(self, 
                                            width=120, 
                                            height=25, 
                                            fg_color=("light blue", "blue"), 
                                            corner_radius=8,
                                            anchor="center", 
                                            text="Passeerlicht", 
                                            font=('Arial', 18))

        self.label.pack(padx=20, pady=20)
        

        self.radio_button_var = customtkinter.StringVar(value="")

        self.radio_button_1 = customtkinter.CTkRadioButton(self, 
                                                           text="P bakboord  ", 
                                                           value="L",
                                                           width=20, 
                                                           variable=self.radio_button_var, 
                                                           command=self.call_to_write)
        
        self.radio_button_1.pack(padx=10, pady=20)
        
        
        self.radio_button_2 = customtkinter.CTkRadioButton(self, 
                                                           text="P stuurboord", 
                                                           value="R",
                                                           width=20, 
                                                           variable=self.radio_button_var,
                                                           command=self.call_to_write)
        
        self.radio_button_2.pack(padx=10, pady=20)
        
        
        self.radio_button_2 = customtkinter.CTkRadioButton(self, 
                                                           text="     P uit       ", 
                                                           value="P",
                                                           width=20, 
                                                           variable=self.radio_button_var,
                                                           command=self.call_to_write)
        
        self.radio_button_2.pack(padx=10, pady=20)
        
        
        self.radio_button_3 = customtkinter.CTkRadioButton(self, 
                                                           text="alle verlichting    ", 
                                                           value="X",
                                                           width=20, 
                                                           variable=self.radio_button_var,
                                                           command=self.call_to_write)
        
        self.radio_button_3.pack(padx=10, pady=20)
        
        
        self.radio_button_3 = customtkinter.CTkRadioButton(self, 
                                                           text="alle verlichting uit", 
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