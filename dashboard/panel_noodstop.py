from imports_n_vars import * 

nurl= f'http://localhost:5000/nood'

class NoodStop(customtkinter.CTkFrame):
    def __init__(self, *args, master ,header_name="Noodstop", **kwargs):
        super().__init__(master,*args, **kwargs)
        self.header_name = header_name

        self.fontbold = customtkinter.CTkFont(**fontbold)
        self.fontmedium = customtkinter.CTkFont(**fontmedium)

        def ramp():
            Thread(target=NoodLog).start()
            return messagebox.showinfo('Noodstop','Noodstop ingedrukt, herstart het systeem!\nAls er verdere assistentie nodig is bel dan "number"')
        
        def NoodLog():
            tijd = translate()
            noodstop = requests.post(nurl, json=f"{tijd}")
            responses=noodstop.json
        
        # self.label = customtkinter.CTkLabel(self, 
        #                                     width=200, 
        #                                     height=45, 
        #                                     fg_color=("light blue", color),
        #                                     anchor="center", 
        #                                     text="Noodstop",
        #                                     corner_radius=8,
        #                                     font=self.fontbold)
        

        self.noodstopbutton = customtkinter.CTkButton(self, 
                                            width=150, 
                                            height=150, 
                                            anchor="center", 
                                            text="NOODSTOP",
                                            fg_color=("red"),
                                            hover_color=("dark red"),
                                            corner_radius=240,
                                            command=ramp,
                                            font=self.fontbold)
        
        # self.label.pack(padx=220, pady=10)
        self.noodstopbutton.pack(padx=161,pady=43)

        
        