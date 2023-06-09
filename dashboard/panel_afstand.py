from imports_n_vars import *

def getdata(dag=0):
    templist=[]
    distlist=[]
    correctedlist=[]
    vdatum=0
    i=0
    with app.app_context():
        for x in Afstand.query.all():
           distlist.append(x.afstand)
        for x in Temperatuur.query.all():
            datum=x.tijd
            if dag==0:
                if (f"{datum.split()[0]} {datum.split()[1]}") != vdatum or vdatum==0: #check of datum niet zelfde is als deze datum
                    templist.append(f"{datum.split()[0]} {datum.split()[1]}")
                    correctedlist.append(distlist[i])
                    vdatum=(f"{datum.split()[0]} {datum.split()[1]}")
                    i+=1
                else:
                    i+=1
            elif dag in f"{datum.split(' ')[0]} {datum.split(' ')[1]}":
              templist.append(datum)  
    return templist,correctedlist



class afst(customtkinter.CTkFrame):
    def __init__(self, *args, master ,header_name="Afstand", **kwargs):
        super().__init__(master,*args, **kwargs)
        self.header_name = header_name
        
        self.fontbold = customtkinter.CTkFont(**fontbold)
        self.fontmedium = customtkinter.CTkFont(**fontmedium)
        
        '''Grafiek'''
        self.fig = Figure(figsize=(5,4), dpi=100)
        xas=getdata()[0]
        yas=getdata()[1]
        print(getdata())
        self.fig.add_subplot(111).plot(
            xas, 
            yas, 
            'go-', label='line 1', linewidth=2)
        

        '''Maak Ruimte voor grafiek'''
        self.canvas = FigureCanvasTkAgg(self.fig, master=self)
        self.canvas.draw()

        # '''Label'''
        # self.label = customtkinter.CTkLabel(self, 
        #                                     width=200, 
        #                                     height=45, 
        #                                     fg_color=("light blue", color),
        #                                     anchor="center", 
        #                                     text="Diepte",
        #                                     corner_radius=8,
        #                                     font=self.fontbold)
        
        # self.label.pack(padx=220,pady=10)
        
        self.disable = customtkinter.CTkButton(self,
                                               text="Switch",
                                               font=self.fontbold,
                                               command=self.Swap)
        
        self.disable.pack(padx=20, pady=20)
        
        '''Afstand zelf'''
        self.label = customtkinter.CTkLabel(self, 
                                            width=120, 
                                            height=25, 
                                            corner_radius=8,
                                            anchor="center", 
                                            text="Afstand: nog niet gemeten",
                                            font=self.fontbold)
        
        self.label.pack(padx=110,pady=200)

    def Swap(self):
        swapped = 1
        if swapped == 1:
            self.canvas.get_tk_widget().pack(padx=70, pady=25)
            self.label.destroy()
        else:
            self.canvas.get_tk_widget().destroy()
            self.label.pack(padx=110, pady=200)
        swapped *= -1
        
        # '''Sticker'''
        # if os.getcwd().split("\\")[-1]=='Picoboot':
        #     self.icon=customtkinter.CTkImage(Image.open("dashboard/images/DepthSymbol.png"), size=(110,110))
        # else:
        #     self.icon=customtkinter.CTkImage(Image.open("images/DepthSymbol.png"), size=(40,40))
        # self.iconwindow=customtkinter.CTkLabel(master=self,image=self.icon, text="")
        # self.iconwindow.place(x=100,y=220)
    
    
    def distanceRead(self):
        self.label.configure(text=f"Diepte : {Reader('Diepte')}, Schuif {Reader('InstructionSchuif')}")

        # schedule the next update after 5 seconds
        self.after(5000, self.distanceRead)
    