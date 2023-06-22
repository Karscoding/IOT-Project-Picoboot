from imports_n_vars import * 
nurl= f'http://localhost:5000/nood'

def Timer():
    sleep(20)
    Writer("NOOD",False)

class NoodStop(customtkinter.CTkFrame):
    def __init__(self, *args, master ,header_name="Noodstop", **kwargs):
        super().__init__(master,*args, **kwargs)
        self.header_name = header_name

        self.fonthuge = customtkinter.CTkFont(**fonthuge)
        self.fontmedium = customtkinter.CTkFont(**fontmedium)

        def ramp():
            Thread(target=NoodLog).start()
            Writer("NOOD", True)
            Thread(target=Timer).start()
            return messagebox.showinfo('Noodstop','Noodstop ingedrukt, herstart het systeem!\nAls er verdere assistentie nodig is bel dan "+31 6 27620981"')
        
        def NoodLog():
            tijd = translate()
            try:
                requests.post(nurl, json=f"{tijd}")
            except:
                ""
        

        self.noodstopbutton = customtkinter.CTkButton(self, 
                                            width=300, 
                                            height=175, 
                                            anchor="center", 
                                            text="NOODSTOP",
                                            fg_color=("red"),
                                            hover_color=("dark red"),
                                            corner_radius=240,
                                            command=ramp,
                                            font=self.fonthuge)
        
        self.noodstopbutton.pack(padx=490,pady=30)
        
        