import customtkinter 
import threading
import time
import os
import sys

customtkinter.set_default_color_theme("blue")
customtkinter.set_appearance_mode("light")

def TempReading(label):
    run=True
    while run:
        path=os.path.join(sys.path[0], 'temp.txt')
        f=open(path,'r')
        Temp = f.read()
        label.configure(text=f"Temp : {Temp}")
        f.close()
        time.sleep(5)


class temp(customtkinter.CTkFrame):
    def __init__(self, *args, master, header_name="Tempratuur", **kwargs):
        super().__init__(master,*args, **kwargs)
        self.header_name= header_name

        self.label = customtkinter.CTkLabel(self, width=120, height=25, corner_radius=8,anchor="center", text=f"Temp: ")
        self.label.grid(row=3,column=2)

        self.button = customtkinter.CTkButton(self, text='Start Reading', command=lambda: TempReading(self.label))
        self.button.grid()


class MyFrame2(customtkinter.CTkFrame):
    def __init__(self, *args, master,header_name="Status machine", **kwargs):
        super().__init__(master, *args, **kwargs)
        # add widgets onto the frame...
        self.header_name = header_name

        self.label = customtkinter.CTkLabel(self, width=120, height=25, fg_color=("orange", "gray75"), corner_radius=8,anchor="center", text="Status Machine")
        self.label.grid(row=0, column=0, padx=10, pady=30)
        self.label = customtkinter.CTkLabel(self, width=120, height=25, fg_color=("red", "gray75"), corner_radius=8,anchor="center", text="Status Aggregraat")
        self.label.grid(row=1, column=0, padx=0, pady=10)
        self.label = customtkinter.CTkLabel(self, width=120, height=25, fg_color=("green", "gray75"), corner_radius=8,anchor="center", text="Status Compressor")
        self.label.grid(row=2, column=0, padx=0, pady=10)
        self.label = customtkinter.CTkLabel(self, width=120, height=25, fg_color=("green", "gray75"), corner_radius=8,anchor="center", text="Status Verlichting")
        self.label.grid(row=3, column=0, padx=0, pady=10)
        self.label = customtkinter.CTkLabel(self, width=120, height=25, fg_color=("green", "gray75"), corner_radius=8,anchor="center", text="Status Voorschuif")
        self.label.grid(row=4, column=0, padx=0, pady=10)
        self.label = customtkinter.CTkLabel(self, width=120, height=25, fg_color=("green", "gray75"), corner_radius=8,anchor="center", text="Status Achterschuif")
        self.label.grid(row=5, column=0, padx=0, pady=10)








class MyFrame(customtkinter.CTkFrame):
    def __init__(self, *args, master,header_name="Warmlopen starten:", **kwargs):
        super().__init__(master, *args, **kwargs)
        # add widgets onto the frame...
        

        
        self.header_name = header_name

        self.header = customtkinter.CTkLabel(self, text=self.header_name)
        self.header.place(relx=0.27, rely=0.05 )

        

        self.progressbar = customtkinter.CTkProgressBar(self, height=20)
        self.progressbar.grid(row=0, column=0, padx=20, pady=80)
        self.progressbar.set(0)
        self.progressbar._border_width=(1)
        self.progressbar._fg_color=("red")
        self.progressbar._progress_color=("green")
        self.progressbar._border_color=("black")
        self.progressbar._mode=("determinate")
        self.progressbar._determinate_speed=(1/300)

        def start_progress_bar():
            self.progressbar.start()
        
        self.button_1 =customtkinter.CTkButton(self, text="Start", border_width=0,corner_radius=8,width=120,height=32,command=start_progress_bar)
        self.button_1.grid(row=1, column=0, padx=0, pady=10)


class RadioButtonFrame(customtkinter.CTkFrame):
    def __init__(self, *args, header_name="RadioButtonFrame", **kwargs):
        super().__init__(*args, **kwargs)
        
        self.header_name = header_name

        self.header = customtkinter.CTkLabel(self, text=self.header_name)
        self.header.grid(row=0, column=0, padx=10, pady=10)

        self.radio_button_var = customtkinter.StringVar(value="")

        self.radio_button_1 = customtkinter.CTkRadioButton(self, text="Handmatig", value="Handmatig", variable=self.radio_button_var)
        self.radio_button_1.grid(row=1, column=0, padx=10, pady=10)
        self.radio_button_2 = customtkinter.CTkRadioButton(self, text="Automatisch", value="Automatisch", variable=self.radio_button_var)
        self.radio_button_2.grid(row=2, column=0, padx=10, pady=10)

        def get_value():
            """ returns selected value as a string, returns an empty string if nothing selected """
            return self.radio_button_var.get()
        self.frame_1_button = customtkinter.CTkButton(self, text="Selecteer", command=get_value)
        self.frame_1_button.grid(row=3, column=0, padx=20, pady=30)

  

    def set_value(self, selection):
        """ selects the corresponding radio button, selects nothing if no corresponding radio button """
        self.radio_button_var.set(selection)

       




class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()


        self.geometry('1280x720')
        self.title("placeholder dashboard")

        self.my_frame = MyFrame(master=self, header_name="Warmlopen starten:")
        self.my_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew") 
        
        self.radio_button_frame_1 = RadioButtonFrame(self, header_name="Besturingsmodus")
        self.radio_button_frame_1.grid(row=0, column=3, padx=20, pady=20)
        
        self.my_frame2 = MyFrame2(master=self, header_name="Status machine")
        self.my_frame2.grid(row=0, column=4, padx=20, pady=20)
        
        self.temp = temp(master=self,header_name="temp")
        self.temp.grid(row=0, column=5, padx=20,pady=20)

        
        

    def print_value_frame_1(self):
        print(f"Frame 1 value: {self.radio_button_frame_1.get_value()}")





if __name__ == "__main__":
    app=App()
    app.mainloop()