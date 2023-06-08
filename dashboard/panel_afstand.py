from imports_n_vars import *

class Afstand(customtkinter.CTkFrame):
    def __init__(self, *args, master ,header_name="Afstand", **kwargs):
        super().__init__(master,*args, **kwargs)
        self.header_name = header_name
        
        self.fontbold = customtkinter.CTkFont(**fontbold)
        self.fontmedium = customtkinter.CTkFont(**fontmedium)
        
        '''Grafiek'''
        self.fig = Figure(figsize=(5,4), dpi=100)

        self.fig.add_subplot(111).plot(
            [1, 2, 5], #X as + dots
            [1, "hallo", 10], #Y as + werkende string
            'go-', label='line 1', linewidth=2)
        

        '''Maak Ruimte voor grafiek'''
        self.canvas = FigureCanvasTkAgg(self.fig, master=self)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(padx=20, pady=10)


        """        '''Label'''
        self.label = customtkinter.CTkLabel(self, 
                                            width=200, 
                                            height=45, 
                                            fg_color=("light blue", color),
                                            anchor="center", 
                                            text="Diepte",
                                            corner_radius=8,
                                            font=self.fontbold)
        
        self.label.pack(padx=220,pady=10)
        
        '''Afstand zelf'''
        self.label = customtkinter.CTkLabel(self, 
                                            width=120, 
                                            height=25, 
                                            corner_radius=8,
                                            anchor="center", 
                                            text="Afstand: nog niet gemeten",
                                            font=self.fontbold)
        
        self.label.pack(padx=0,pady=200)

        '''Sticker'''
        if os.getcwd().split("\\")[-1]=='Picoboot':
            self.icon=customtkinter.CTkImage(Image.open("dashboard/images/DepthSymbol.png"), size=(110,110))
        else:
            self.icon=customtkinter.CTkImage(Image.open("images/DepthSymbol.png"), size=(40,40))
        self.iconwindow=customtkinter.CTkLabel(master=self,image=self.icon, text="")
        self.iconwindow.place(x=100,y=220)"""
    
    
    def distanceRead(self):
        self.label.configure(text=f"Diepte : {Reader('Diepte')}, Schuif {Reader('InstructionSchuif')}")
        
        # schedule the next update after 5 seconds
        self.after(5000, self.distanceRead)