from customtkinter import CTkOptionMenu

from Image_Editor import *
from tkinter import *
from customtkinter import *

root = CTk()  # create the Tk window like you normally do
root.geometry("400x240")
root.title("CustomTkinter Test")
set_default_color_theme("green")
set_appearance_mode("dark")
#set_widget_scaling()

def button_function(res):
    print(res)
    for widget in root.winfo_children():
        widget.destroy()


options = ["Edit Image", "Compress Image", "Resize Image", "Crop Image", "Rotate Image", "Blur Image", "Sharpen Image", "Edge Enhance Image", "Meta Data"]

button = CTkButton(master=root, corner_radius=10, command=button_function)
button.place(relx=0.5, rely=0.5, anchor=CENTER)

# clicked = StringVar(root_tk)
# clicked.set(options[0])

# drop = OptionMenu( root_tk, clicked , *options )
# drop.pack()

drop = CTkOptionMenu(root,  values=options, command=button_function)
drop.place(relx=0.5, rely=0.5, anchor=CENTER)
print(root.winfo_children())

root.mainloop()