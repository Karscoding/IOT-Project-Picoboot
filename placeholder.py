import customtkinter 

customtkinter.set_default_color_theme("blue")
customtkinter.set_appearance_mode("light")




class MyFrame(customtkinter.CTkFrame):
    def __init__(self, *args, master, **kwargs):
        super().__init__(master, *args, **kwargs)
        

        # add widgets onto the frame...

        self.progressbar = customtkinter.CTkProgressBar(self)
        self.progressbar.pack(padx=20, pady=10)
        self.progressbar.set(0)
        self.progressbar._border_width=(1)
        self.progressbar._fg_color=("red")
        self.progressbar._progress_color=("green")
        self.progressbar._border_color=("black")
        self.progressbar._mode=("determinate")
        self.progressbar._determinate_speed=(1/300)
        self.progressbar.start()




class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()


        self.geometry('1280x720')
        self.title("placeholder dashboard")

        
        self.my_frame = MyFrame(master=self)
        self.my_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        


        


        





if __name__ == "__main__":
    app = App()
    app.mainloop()