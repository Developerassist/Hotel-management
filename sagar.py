from tkinter import *
from PIL import ImageTk, Image

root = Tk()

# Open the image file
img = Image.open("hotel1.jpg")

# Create a PhotoImage object from the image
photo = ImageTk.PhotoImage(img)

# Create a Label widget and set its image property to the PhotoImage
label = Label(root, image=photo)
label.pack()

root.mainloop()
