from imports import *

class ProgressFrame(customtkinter.CTkFrame):
    def __init__(self, *args, master,header_name="Warmlopen starten:", **kwargs):
        super().__init__(master, *args, **kwargs)
        # add widgets onto the frame...
        self.header_name = header_name
        
        self.label = customtkinter.CTkLabel(self, 
                                            width=120, 
                                            height=25, 
                                            fg_color=("light blue", "blue"), 
                                            corner_radius=8,
                                            anchor="center", 
                                            text="Timer (5 minuten)", 
                                            font=('Arial', 18))
        
        self.label.pack(padx=20, pady=10)
        

        self.progressbar = customtkinter.CTkProgressBar(self, height=20)
        
        self.progressbar.pack(padx=20, pady=80)
        self.progressbar.set(0)
        self.progressbar._border_width=(1)
        self.progressbar._progress_color=("green")
        self.progressbar._border_color=("black")
        self.progressbar._fg_color=("blue")
        self.progressbar._mode=("determinate")
        self.progressbar._determinate_speed=(1/300)
        

        def start_progress_bar():
            self.progressbar.start()
        
        
        self.button_1 =customtkinter.CTkButton(self, 
                                               text="Start", 
                                               border_width=0,
                                               corner_radius=8,
                                               width=120,
                                               command=start_progress_bar, 
                                               font=('Arial', 18))
        
        self.button_1.pack(padx=100, pady=20)