from imports_n_vars import *
from panel_lights import LightsMaster, MainLights, PLights

class LightsPage():
    def __init__(self, *args, master, header_name="Lampen Besturing", **kwargs):
        # super().__init__(master, *args, **kwargs)
        self.light_master = LightsMaster(master=self, header_name="Lampen Besturing")
        self.plight = PLights(master=self.light_master)
        self.lights_control = MainLights(master=self.light_master)
        
    def Init(self):
        self.light_master = LightsMaster(master=self, header_name="Lampen Besturing")
        self.plight = PLights(master=self.light_master)
        self.lights_control = MainLights(master=self.light_master)
        
    def Show(self):
        self.light_master.place(x=20, y=100)
        self.plight.pack(padx=20, pady=20, side=customtkinter.LEFT)
        self.lights_control.pack(padx=20, pady=20, side=customtkinter.RIGHT)
        
    def Hide(self):
        self.light_master.destroy()
        self.plight.destroy()
        self.lights_control.destroy()
        self.Init()