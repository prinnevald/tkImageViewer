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

def reconfig(status, label, mem):
    label.configure(image=mem.images[mem.cursor])
    stat = mem.cursor + 1
    status.configure(text="Image "+str(stat)+" of "+str(len(mem.images)))

def prevImg(status, label, mem):
    mem.cursor = mem.cursor - 1
    if mem.cursor == -1:
        mem.cursor = mem.cursor + 1
    reconfig(status, label, mem)


def nextImg(status, label, mem):
    mem.cursor = mem.cursor + 1
    if mem.cursor == len(mem.images):
        mem.cursor = mem.cursor - 1
    reconfig(status, label, mem)

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

    # creating status bar

    status = Label(root, text="Image 1 of "+str(len(mem.images)),
                    bd=1, relief=SUNKEN, anchor=E)

    # buttons for changing images and quitting

    p = "<< Previous Image"
    n = "Next Image >>"
    e = "Exit Viewer"

    b_prev = Button(root, text=p, command=lambda:prevImg(status, label, mem))
    b_next = Button(root, text=n, command=lambda:nextImg(status, label, mem))
    b_quit = Button(root, text=e, command=root.quit)
    
    b_prev.grid(column=0, row=1)
    b_next.grid(column=2, row=1)
    b_quit.grid(column=1, row=1, pady=10)
    status.grid(column=0, row=2, columnspan=3, sticky=W+E)

    root.mainloop()
    
if __name__ == "__main__":
    main()