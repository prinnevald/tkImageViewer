from tkinter import *
from PIL import ImageTk, Image
import os

# memory class

class Memory():
    def __init__(self):
        self.cursor = 0
        self.images = []
        for i in os.listdir("images"):
            self.images.append(ImageTk.PhotoImage(Image.open("images/" + i)))

# main function

def main():
        
    # creating window
    
    root = Tk()
    root.title("tkimgViewer")

    # setting icon for the app

    root.iconbitmap("py.ico")

    # read images and create cursor in class

    mem = Memory()

    # widget to show image

    my_label = Label(image=mem.images[mem.cursor])
    my_label.grid(column=0, row=0, columnspan=3)

    # change the image function

    def change(mem, act):
        mem.cursor = mem.cursor + act

        if mem.cursor == -1:
            mem.cursor = mem.cursor - act
        elif mem.cursor == len(os.listdir("images")):
            mem.cursor = mem.cursor - act

        my_label.configure(image=mem.images[mem.cursor])

    # buttons for changing images

    prev = Button(root, text="Previous", command=lambda:change(mem, -1))
    nexti = Button(root, text="Next", command=lambda:change(mem, 1))
    
    prev.grid(column=0, row=1)
    nexti.grid(column=2, row=1)

    # creating a quit button

    button_quit = Button(root, text="Exit Program", command=root.quit)
    button_quit.grid(column=1, row=1)

    root.mainloop()
    
if __name__ == "__main__":
    main()