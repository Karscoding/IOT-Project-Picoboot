import customtkinter as ctk

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
    progressbar.start()


#Widgets
frame = ctk.CTkFrame(master=root)
frame.grid(row=0, column=0, columnspan=10, rowspan=10, padx=20, pady=20, sticky='nsew')

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

graph_label = ctk.CTkLabel(master=graph_frame, text='Graph')
graph_label.grid()

#Run
root.mainloop()