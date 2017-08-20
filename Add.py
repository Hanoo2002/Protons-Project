from tkinter import *

root = Tk()

Home = Frame(root)

class Add:
    def __init__(self, parent):
        top = self.top = Toplevel(parent)

        Label(top, fg='white',bg='blue' ,text="Add").pack()

        Label(top,fg='white',bg='blue' , text='What do you want to add?')

        cat = Button(top,fg='white',bg='blue' , text="Category", command=lambda: raise_frame(AddCategory))
        cat.pack(pady=5, padx=5, side=LEFT)

        act = Button(top,fg='white',bg='blue' , text="Activity", command=lambda: raise_frame(AddActivity))
        act.pack(pady=5, padx=5, side=LEFT)


def add():
    ad = Add(Home)
    Home.wait_window(ad.top)