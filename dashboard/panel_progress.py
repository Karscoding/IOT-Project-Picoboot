from imports_n_vars import *

class ProgressFrame(customtkinter.CTkFrame):
    def __init__(self, *args, master,header_name="Warmlopen starten:", **kwargs):
        super().__init__(master, *args, **kwargs)
        # add widgets onto the frame...
        self.header_name = header_name
        
        self.count = 300
        
        self.fontbold = customtkinter.CTkFont(**fontbold)
        self.fontbig = customtkinter.CTkFont(**fontbig)
        
        self.label = customtkinter.CTkLabel(self, 
                                            width=120, 
                                            height=25,
                                            corner_radius=8,
                                            fg_color=color,
                                            anchor="center", 
                                            text="Timer (5 minuten)", 
                                            font=self.fontbold)
        
        self.label.pack(padx=77, pady=10)
        

        self.progressbar = customtkinter.CTkProgressBar(self, height=25,
                                                        border_width=0,
                                                        progress_color="green",
                                                        border_color="black",
                                                        fg_color="grey",
                                                        mode="determinate",
                                                        determinate_speed=1/300)
        
        self.progressbar.pack(padx=50, pady=63)
        self.progressbar.set(0)
        
        
        self.counter = customtkinter.CTkLabel(self,
                                              text="",
                                              font=self.fontbig)
        
        self.counter.pack()
        
        
        def Counting():
            self.count -= 1
            self.counter.configure(text=self.count)
            self.after(1000, Counting)
        
        
        
        def Starter():
            self.progressbar.start()
            Counting()
            
        self.button_1 =customtkinter.CTkButton(self, 
                                               text="Start", 
                                               border_width=0,
                                               corner_radius=8,
                                               width=120,
                                               command=Starter, 
                                               font=self.fontbig)
        
        self.button_1.pack(padx=100, pady=20)