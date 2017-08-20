from tkinter import *
from Algorithm import *
import calendar

root = Tk()

Home = Frame(root)

class Edit:
    def __init__(self, parent):
        top = self.top = Toplevel(parent)

        Label(top,text="Edit").pack()

        Label(top, text='What do you want to edit?')

        cate = Button(top,fg='white',bg='blue' , text="Category", command=lambda: raise_frame(EditCategory))
        cate.pack(pady=5, padx=5, side=LEFT)

        activity = Button(top,fg='white',bg='blue' , text="Activity", command=lambda: raise_frame(EditActivity))
        activity.pack(pady=5, padx=5, side=LEFT)


def edit():
    ed = Edit(Home)
    Home.wait_window(ed.top)
