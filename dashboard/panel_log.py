from imports_n_vars import *

class HistoryLog(customtkinter.CTkFrame):    
    def __init__(self, *args, master, header_name="Log", **kwargs):
        super().__init__(master, *args, **kwargs)
        self.header_name=header_name
        
        self.fontbold = customtkinter.CTkFont(**fontbold)
        self.fontmedium = customtkinter.CTkFont(**fontsmall)
        
        
        self.label = customtkinter.CTkLabel(self, 
                                            fg_color=("light blue", color), 
                                            corner_radius=8,
                                            anchor="center", 
                                            text="Log", 
                                            font=self.fontbold)

        self.label.pack(padx=108, pady=20)
        
        
        self.logbox = customtkinter.CTkLabel(self,
                                             font=self.fontmedium,)
        
        self.logbox.pack(padx=20, pady=0)

    def change(self,log):
        output=''
        for x in range(1,13):
            output+=log[-x][0]+','+log[-x][1]+"\n\n"
        self.logbox.configure(text=output)
        # self.logbox.configure(text=f"{log[0]}")
        # 
        # for x in range(0, len(incoming)):
        #     output = (log[x][0] + ',' + log[x][1])
        # self.logbox.configure(text=f"{output}")