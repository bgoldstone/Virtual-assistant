#Description: Making A GUI for the voice assistant

#importing modules
import tkinter as tk
from vassistant import get_inaudio

#setting variables
size = "720x500"
path = "resources\img.png"
button_height = 500
button_width = 500



#setting up the window
root = tk.Tk()
root.title("Virtual Assistant")
root.minsize(720,480)
root.geometry(size)
#setting up the talk button
img = tk.PhotoImage(file = path)
talk_b = tk.Button(root , command = get_inaudio())
talk_b.config( image = img, 
               width=button_width, 
               height=button_height )
talk_b.pack()


#displaying the window
root.mainloop()
