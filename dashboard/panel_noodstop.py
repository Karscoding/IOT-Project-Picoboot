from imports_n_vars import * 


class NoodStop(customtkinter.CTkFrame):
    def __init__(self, *args, master ,header_name="Noodstop", **kwargs):
        super().__init__(master,*args, **kwargs)
        self.header_name = header_name

        self.fontbold = customtkinter.CTkFont(**fontbold)
        self.fontmedium = customtkinter.CTkFont(**fontmedium)

        def ramp():
            return messagebox.showinfo('Noodstop','Noodstop ingedrukt, herstart het systeem!\nAls er verdere assistentie nodig is bel dan "number"')
        
        
        self.label = customtkinter.CTkLabel(self, 
                                            width=200, 
                                            height=45, 
                                            fg_color=("light blue", color),
                                            anchor="center", 
                                            text="Noodstop",
                                            corner_radius=8,
                                            font=self.fontbold)
        

        self.noodstopbutton = customtkinter.CTkButton(self, 
                                            width=200, 
                                            height=100, 
                                            anchor="center", 
                                            text="Stop",
                                            fg_color=("red"),
                                            bg_color=("black"),
                                            hover_color=("dark red"),
                                            corner_radius=20,
                                            command=ramp,
                                            font=self.fontbold)
        
        self.label.pack(padx=220, pady=10)
        self.noodstopbutton.pack(padx=0,pady=35)

        
        