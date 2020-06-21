from tkinter import *
from PIL import ImageTk, Image
import os

# memory class

class Memory():
    def __init__(self):
        self.cursor = 0
        self.images = []
        for i in os.listdir("images"):
            self.images.append(ImageTk.PhotoImage(Image.open("images/"+i)))

# change the image functions

def prevImg(label, mem):
    mem.cursor = mem.cursor - 1
    if mem.cursor == -1:
        mem.cursor = mem.cursor + 1
    label.configure(image=mem.images[mem.cursor])

def nextImg(label, mem):
    mem.cursor = mem.cursor + 1
    if mem.cursor == len(os.listdir("images")):
        mem.cursor = mem.cursor - 1
    label.configure(image=mem.images[mem.cursor])

### MAIN ###

def main():
        
    # creating window
    
    root = Tk()
    root.title("tkimgViewer")

    # setting icon for the app

    root.iconbitmap("py.ico")

    # read images and create cursor in class

    mem = Memory()

    # widget to show image

    label = Label(image=mem.images[mem.cursor])
    label.grid(column=0, row=0, columnspan=3)

    # buttons for changing images and quitting

    b_prev = Button(root, text="Previous", command=lambda:prevImg(label, mem))
    b_next = Button(root, text="Next", command=lambda:nextImg(label, mem))
    b_quit = Button(root, text="Exit Program", command=root.quit)
    
    b_prev.grid(column=0, row=1)
    b_next.grid(column=2, row=1)
    b_quit.grid(column=1, row=1)

    root.mainloop()
    
if __name__ == "__main__":
    main()