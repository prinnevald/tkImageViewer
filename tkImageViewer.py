from tkinter import *
from PIL import ImageTk, Image

# main function

def main():
        
    # creating window
    
    root = Tk()
    root.title("tkImages")

    # setting icon for the app

    root.iconbitmap("py.ico")

    # create an image

    my_img = ImageTk.PhotoImage(Image.open("image.png"))
    my_label = Label(image=my_img)
    my_label.pack()

    # creating a quit button

    button_quit = Button(root, text="Exit Program", command=root.quit)
    button_quit.pack()

    root.mainloop()
    
if __name__ == "__main__":
    main()