from imports_n_vars import *

class DBcontrol(customtkinter.CTkFrame):
    def __init__(self, *args, master,header_name="DBcontrol", **kwargs):
        super().__init__(master, *args, **kwargs)
        # add widgets onto the frame...
        self.header_name = header_name
        
        self.fonthuge = customtkinter.CTkFont(**fonthuge)
        self.fontmedium = customtkinter.CTkFont(**fontmedium)
        
        self.DBlabel = {"corner_radius":8,
                            "font":self.fonthuge,
                            "fg_color":("green", "#3e8747")}
        
        def returnies():
            sleep(3)
            self.print.configure(text="Gegevens printen")

        def printde():
            writetotext(getdata())
            self.print.configure(text="gelukt")
            Thread(target=returnies).start()
            
        def ja():
            writetotext(getdata())
            sleep(1)
            delete()
            #self.sure.destroy()
            self.ja.destroy()
            self.nee.destroy()


        def nee():
            #self.sure.destroy()
            self.ja.destroy()
            self.nee.destroy()

        def usure():
            # self.sure = customtkinter.CTkLabel(self,
            #                                 fg_color="red", 
            #                                 corner_radius=8,
            #                                 text="Dit print een bestand uit met alle huidige gegevens. \nHierna word de database geleegd. Weet u het zeker?.",
            #                                 font=self.fontmedium)
            # self.sure.pack(padx=0, pady=0)

            self.ja = customtkinter.CTkButton(self,
                                               text="Ja",
                                               font=self.fontmedium,
                                               command=ja)
        
            self.ja.pack(padx=0, pady=50,)

            self.nee = customtkinter.CTkButton(self,
                                               text="Nee",
                                               font=self.fontmedium,
                                               command=nee)
        
            self.nee.pack(padx=0, pady=50)
            return messagebox.showinfo("Waarschuwing","Dit print een bestand uit met alle huidige gegevens. \nHierna word de database geleegd. Weet u het zeker? Klik dan op Ja.")

        self.titel = customtkinter.CTkLabel(self,
                                            fg_color=(color), 
                                            corner_radius=8,
                                            text="DB controle",
                                            font=self.fonthuge)
        
        self.titel.pack(padx=175, pady=30)
        
        
        self.delete = customtkinter.CTkButton(self,
                                               text="Nieuwe ronde",
                                               font=self.fontmedium,
                                               command=usure)
        
        self.delete.pack(padx=0, pady=50)

        self.print = customtkinter.CTkButton(self,
                                               text="Gegevens printen",
                                               font=self.fontmedium,
                                               command=printde)
        
        self.print.pack(padx=0, pady=50)
        

        