from tkinter import *
from Algorithm import *
import calendar

create_table()


def raise_frame(parent):
    parent.tkraise()

root = Tk()

Home = Frame(root)
AddActivity = Frame(root)
AddCategory = Frame(root)
EditActivity = Frame(root)
EditCategory = Frame(root)
Calendar = Frame(root)
Todo = Frame(root)
Today = Frame(root)
Now = Frame(root)


for frame in (Home, AddActivity, AddCategory, EditActivity, EditCategory, Calendar, Todo, Today, Now):
    frame.grid(row=0, column=0, sticky='news')
########################################################################################################################
# Home Frame






TopFrame = Frame(Home)
MiddleFrame = Frame(Home, padx=200)
BottomFrame = Frame(Home)
LastFrame_Home = Frame(Home)

TopFrame.pack(side='top', fill=X)
MiddleFrame.pack(side='top', ipady=5, fill=X)
BottomFrame.pack(side='top', ipady=5, fill=X)
LastFrame_Home.pack(side='top', ipady=5, fill=X)

HomeLabel = Label(TopFrame, text='Home')
HomeLabel.pack(side=LEFT)

AddButton = Button(TopFrame, text='Add', command=add)
AddButton.pack(side=RIGHT)

CalendarButton = Button(MiddleFrame, text='Calendar', command=lambda: raise_frame(Calendar))
CalendarButton.pack(padx=5, pady=10, side=LEFT)

TodoButton = Button(MiddleFrame, text='Todo', command=lambda: raise_frame(Todo))
TodoButton.pack(padx=5, pady=10, side=LEFT)

TodayButton = Button(MiddleFrame, text='Today', command=lambda: raise_frame(Today))
TodayButton.pack(padx=5, pady=10, side=LEFT)

NowButton = Button(MiddleFrame, text='Now', command=lambda: raise_frame(Now))
NowButton.pack(padx=5, pady=10, side=LEFT)


category_name = strainer('name', 'sort', 'category')
number = 0
# if category_name[number][0]
for i in range(0, len(category_name)):
    if number == 10:
        break
    CategoryButton = Button(BottomFrame, text='{}'.format(category_name[number][0]), width=5, anchor="w")
    CategoryButton.pack(padx=5, pady=5, fill=X)
    number += 1

EditButton = Button(LastFrame_Home, text='Edit', command=edit)
EditButton.pack()

########################################################################################################################
# AddActivity Frame
# The layout is devided in many frames


def on_entry_click(event):
    """
    when any entry widget is clicked, this code comes to action.
    This deletes what was written in the entry widget and makes the font-colour black
    """
    global FirstClick
    entry = event.widget
    if FirstClick:
        FirstClick = False
        entry.config(fg='black')
        entry.delete(0, "end")
    FirstClick = True
    return


def back():
    """
    is called when the BackButton is clicked.
    It gets the user back to home
    """
    raise_frame(Home)


def insert():
    """
    This saves the data of the user and brings him back to home
    """
    list_of_days = [Mon.get(), Tue.get(), Wed.get(), Thu.get(), Fri.get(), Sat.get(), Sun.get()]
    number_of_day = 0
    list_of_calendar_day_names = calendar.day_name
    frequency = []
    for day in list_of_days:
        if day == 1:
            frequency.append(list_of_calendar_day_names[number_of_day])
            number_of_day += 1
    date_of_activity = "{}/{}/{}".format(Day.get(), Month.get(), Year.get())
    if Category.get() == 'todo':
        insert_todo(NameOfActivity.get(), Category.get(), HoursFrom.get(), MinTo.get(), date_of_activity,
                    Importance.get(), frequency)
    else:
        insert_event(NameOfActivity.get(), Category.get(), HoursFrom.get(), MinTo.get(), date, Importance.get(),
                     frequency)
    raise_frame(Home)


# The first frame contains the name of the event the user will write
NameFrame = Frame(AddActivity)
NameFrame.pack(side='top', fill=X, ipady=5)

NameLabel = Label(NameFrame, text='Name: ')
NameLabel.pack(side=LEFT)
FirstClick = True

NameOfActivity = Entry(NameFrame, fg='grey')
NameOfActivity.insert(0, "Enter the name of your event ...", )
NameOfActivity.bind('<FocusIn>', on_entry_click)
NameOfActivity.pack(ipadx=25, side=LEFT)

# This frame includes a DropDownMenu which gets all of the categories in the database
CategoryFrame = Frame(AddActivity)
CategoryFrame.pack(side='top', ipady=5, fill=X)

category_names = []

category_name = strainer('name', 'sort', 'category')
number = 0

for loop in range(0, len(category_name)):
    category_names.append(category_name[number][0])
    number += 1

Category = StringVar(CategoryFrame)
Category.set('None')

option = OptionMenu(CategoryFrame, Category, *category_names)
option.pack(fill=X, pady=5)


event = StringVar(CategoryFrame)
event.set('Todo')
category = OptionMenu(CategoryFrame, event, "Todo", 'Event')
category.pack(fill=X, pady=5)

# This Frame contains two entry widgets, where the user will write the from and to time, aka hours and min
EstimatedFrame = Frame(AddActivity)
EstimatedFrame.pack(side='top', ipady=5, fill=X)


HoursFrom = Entry(EstimatedFrame, fg='grey')
HoursFrom.insert(0, "Hours: 2 / From: 7:30", )
HoursFrom.bind('<FocusIn>', on_entry_click)
HoursFrom.pack(ipadx=25, side=LEFT, padx=5)

MinTo = Entry(EstimatedFrame, fg='grey')
MinTo.insert(0, "Min: 15 / To: 9:30")
MinTo.bind('<FocusIn>', on_entry_click)
MinTo.pack(ipadx=25, side=RIGHT, padx=5)

# Here the user will type the date of the event
DateFrame = Frame(AddActivity)
DateFrame.pack(side='top', ipady=5, fill=X, padx=10)

Day = Entry(DateFrame, fg='grey')
Day.insert(0, "DD")
Day.bind('<FocusIn>', on_entry_click)
Day.pack(ipadx=25, side=LEFT, padx=5)

Month = Entry(DateFrame, fg='grey')
Month.insert(0, "MM")
Month.bind('<FocusIn>', on_entry_click)
Month.pack(ipadx=25, side=LEFT, padx=5)

Year = Entry(DateFrame, fg='grey')
Year.insert(0, "YYYY")
Year.bind('<FocusIn>', on_entry_click)
Year.pack(ipadx=25, side=LEFT, padx=5)

# Here the user will say in wich days the activity should be done
FrequencyFrame = Frame(AddActivity)
FrequencyFrame.pack(side='top', ipady=5, fill=X)

Sun = IntVar()
Mon = IntVar()
Tue = IntVar()
Wed = IntVar()
Thu = IntVar()
Fri = IntVar()
Sat = IntVar()

Checkbutton(FrequencyFrame, text='Sunday', variable=Sun).pack(side=LEFT, padx=5)
Checkbutton(FrequencyFrame, text='Monday', variable=Mon).pack(side=LEFT, padx=5)
Checkbutton(FrequencyFrame, text='Tuesday', variable=Tue).pack(side=LEFT, padx=5)
Checkbutton(FrequencyFrame, text='Wednesday', variable=Wed).pack(side=LEFT, padx=5)
Checkbutton(FrequencyFrame, text='Thursday', variable=Thu).pack(side=LEFT, padx=5)
Checkbutton(FrequencyFrame, text='Friday', variable=Fri).pack(side=LEFT, padx=5)
Checkbutton(FrequencyFrame, text='Saturday', variable=Sat).pack(side=LEFT, padx=5)

# Here the user will determine how important is the activity for him
PriorityFrame = Frame(AddActivity)
PriorityFrame.pack(side='top', ipady=5, fill=X, padx=200)

Importance = IntVar()
Radiobutton(PriorityFrame, text='1', variable=Importance, value=1).pack(side=LEFT, padx=5)
Radiobutton(PriorityFrame, text='2', variable=Importance, value=2).pack(side=LEFT, padx=5)
Radiobutton(PriorityFrame, text='3', variable=Importance, value=3).pack(side=LEFT, padx=5)
Radiobutton(PriorityFrame, text='4', variable=Importance, value=4).pack(side=LEFT, padx=5)

# This frame contains two buttons
LastFrame_AddActivity = Frame(AddActivity)
LastFrame_AddActivity.pack(side='top', fill=X)

Back_AddActivity = Button(LastFrame_AddActivity, text='Back', command=back).pack(side=LEFT, ipadx=20)
Insert_AddActivity = Button(LastFrame_AddActivity, text='Insert', command=insert).pack(side=RIGHT, ipadx=20)
########################################################################################################################
# AddCategory Frame
NameFrame = Frame(AddCategory)
PriorityFrame = Frame(AddCategory)
LastFrame_AddCategory = Frame(AddCategory)

NameFrame.pack(side='top', fill=X, ipady=5)
PriorityFrame.pack(side='top', ipady=5, fill=X, padx=200)
LastFrame_AddCategory.pack(side='top', fill=X)

NameLabel = Label(NameFrame, text='Name: ')
NameLabel.pack(side=LEFT)

name = Entry(NameFrame, fg='grey')
name.insert(0, "Enter the name of your event ...", )
name.bind('<FocusIn>', on_entry_click)
name.pack(ipadx=25, side=LEFT)

Importance = IntVar()
Radiobutton(PriorityFrame, text='1', variable=Importance, value=1).pack(side=LEFT, padx=5)
Radiobutton(PriorityFrame, text='2', variable=Importance, value=2).pack(side=LEFT, padx=5)
Radiobutton(PriorityFrame, text='3', variable=Importance, value=3).pack(side=LEFT, padx=5)
Radiobutton(PriorityFrame, text='4', variable=Importance, value=4).pack(side=LEFT, padx=5)


def back():
    raise_frame(Home)


def insert():
    insert_category(name.get(), Importance.get())
    raise_frame(Home)

Insert_AddCategory = Button(LastFrame_AddCategory, text='Back', command=insert).pack(side=LEFT, ipadx=20)
Back_AddCategory = Button(LastFrame_AddCategory, text='Back', command=back).pack(side=LEFT, ipadx=20)
########################################################################################################################
# EditActivity Frame

LastFrame = Frame(EditActivity)
LastFrame.pack(side='top', fill=X)

Back_EditActivity = Button(LastFrame, text='Back', command=back).pack(side=LEFT, ipadx=20)

# Here you should let the user edit his/her activities
# Functions you will use: edit, done, delete, del_done, strainer
########################################################################################################################
# EditCategory Frame

LastFrame = Frame(EditCategory)
LastFrame.pack(side='top', fill=X)

Back_EditCategory = Button(LastFrame, text='Back', command=back).pack(side=LEFT, ipadx=20)

# Here you should let the user edit his/her categories
# Functions you will use: edit, delete, strainer
########################################################################################################################
# Calendar Frame

LastFrame = Frame(Calendar)
LastFrame.pack(side='top', fill=X)

Back_Calendar = Button(LastFrame, text='Back', command=back).pack(side=LEFT, ipadx=20)

# Here the user should see all of his events
# Functions you will use: strainer, done
########################################################################################################################
# Todo Frame

LastFrame_Todo = Frame(Todo)
LastFrame_Todo.pack(side='top', fill=X)

Back_Todo = Button(LastFrame_Todo, text='Back', command=back).pack(side=LEFT, ipadx=20)

# Here the user should see all of his Todo
# Functions you will use: strainer, done
########################################################################################################################
# Today Frame

LastFrame_Today = Frame(Today)
LastFrame_Today.pack(side='top', fill=X)

Back_Today = Button(LastFrame_Today, text='Back', command=back).pack(side=LEFT, ipadx=20)

# Functions you will use: strainer, organize(propabily you will need to make an extra db for this)
########################################################################################################################
# Now Frame

LastFrame_Now = Frame(Now)
LastFrame_Now.pack(side='top', fill=X)

Back_Now = Button(LastFrame_Now, text='Back', command=back).pack(side=LEFT, ipadx=20)

# Functions you will use: strainer(propabily you will need to make an extra db for this)

raise_frame(Home)
root.mainloop()
