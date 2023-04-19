import customtkinter as ctk
import threading
import time
import os
import sys

#Initialization
ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('blue')

root = ctk.CTk()
root.title('Test')
root.geometry('1280x720')
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure((0,5), weight=1)

font = 'Cascadia Code'

#Functions
def startTimer():
    progressbar.set(0)
    progressbar.start()
    
def TempReading():
    run = True
    while run:
        f = open(os.path.join(sys.path[0], 'temp.txt'), 'r')
        Temp = f.read()
        text_label.configure(text=f"Temp : {Temp}")
        f.close()
        time.sleep(2)


#Widgets
frame = ctk.CTkFrame(master=root)
frame.grid(row=0, column=0, columnspan=10, rowspan=10, padx=20, pady=20, sticky='nsew')

text_label = ctk.CTkLabel(master=frame, text='Temp : ')
text_label.grid(row=3,column=2)
temp_button = ctk.CTkButton(master=frame, text='Start Reading', command=(threading.Thread(target=TempReading).start))
temp_button.grid()

progress_frame = ctk.CTkFrame(master=frame)
progress_frame.grid(row=0, column=0)

progressbar = ctk.CTkProgressBar(
    master=progress_frame, 
    width=250, 
    height=30,
    corner_radius=10,
    determinate_speed=(1/300))
progressbar.grid(pady=20, padx=20)

button = ctk.CTkButton(
    master=progress_frame, 
    text='Timer Start', 
    command=startTimer,
    font=(font,14))
button.grid(pady=10, padx=10)

graph_frame = ctk.CTkFrame(master=root)
graph_frame.grid(row=0,column=1)

def Tester():
    for x in range(0,200):
        print('Testing ', x)
        time.sleep(2)

if __name__ == '__main__':
    root.mainloop()