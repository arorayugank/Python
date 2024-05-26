## GUI- Graphical user interface

## Types of interface
        # CLI - command line interface
        # GUI - Graphical user interface
        
            ## All Application we use is called GUI
                # Desktop application
                # Mobile application
                # Web application

# .exe
# .apk


#-------------------------------------------------------

# Package in python for 
    # desktop application - tkinter
    # android mobile application - kivy
    # web application - flask, django

# Desktop application

# we generate GUI controls also know as wigates


# GUI controls/Widgets
# label
        # Text
        # image
# Message
# Button
# Entry box
# Text box
# Radio Button
# Check Button
# Option menu
# Scale
# Scrollbar
# Frame
# messagebox
# filedialog
# Menu

## function to place widgets

# pack(side=) # top, bottom, right and left # if not passed any side then top is the default value
# grid(row=,column=)
# place(x=,y=) # x and y are coordinate

# Grid and pack cannot be used in same program


# variable classes

# IntVar()==0
# DoubleVar()==0.0
# booleanVar()== False
# = stringVar() ==""

from tkinter import *
from tkinter import messagebox,filedialog

root=Tk() # this class will create layout

root.geometry("400x400")
root.title ("Myapp")

# change app icon

photo=PhotoImage(file=r"c:\Users\Disha\Downloads\img.png")

root.iconphoto(False,photo)

# app background

root.config (bg="#EBEEF2")  # "#6495ED"

# lable

# font=("type",size,"bold")

# l1=Label(root,text="python", bg="#6495ED", fg="red", font=("times",20,"bold"))

# another way
l1=Label(root)

# l1.config(text="python", bg="#6495ED", fg="red", font=("times",20,"bold"))



# l2=Label(root, text="Java",bg="#6495ED", fg="green", font=("times",20,"bold"))

# l1.pack()
# l2.pack()

# place widgets

# l1.pack(side="bottom")
# l1.pack(side="top")

# l1.grid(row=0,column=0)
# l2.grid(row=0,column=1)
# l2.place(x=180,y=200)

#---------------------------------------------------------------------
# image lable

# lable with images is called image lable        


# l1=Label(root,image=photo)
# l1.pack()

#------------------------------------------------------------------------

# Button

# Set oparation on button'

# def submit():
#     l1=Label(root,image=photo)
#     l1.pack()


# b1=Button(root, text="Enter", command=submit, bg="green", fg="white", font=("",14,"bold"))
# b1.pack()

#--------------------------------------------------------------------------

# Entry box

# e1=Entry(root,width=20,font=("",18))
# e1.pack()


# def submit():
#     # print(e1.get())
#     l1.config(text=e1.get())

# b1=Button(root, text="Enter",command=submit)
# b1.pack()

# l1=Label(root)
# l1.pack()

#---------------------------------------------------------------------------

# Text

# t1=Text(root,height=5,width=10)
# t1.pack()

# def submit():
#     # print(e1.get())
#     l1.config(text=t1.get("0.0",END))

# b1=Button(root, text="Enter",command=submit)
# b1.pack()

# l1=Label(root)
# l1.pack()

#----------------------------------------------------------------------------

# Radio button

# var=IntVar()  # initial value is 0



# r1=Radiobutton(root,text="Male",variable=var,value=1)
# r2=Radiobutton(root,text="Female",variable=var,value=2)
# r1.pack()
# r2.pack()

# def submit():
#     if var.get()==1:
#         print("Male")
#     else:
#         print("Female")
            

# b1=Button(root, text="Enter",command=submit)
# b1.pack()

#--------------------------------------------------------------------------

# Check button

# var1=IntVar()
# var2=IntVar()

# c1=Checkbutton(root,text="Python",variable=var1)
# c2=Checkbutton(root,text="Data Science",variable=var2)
# c1.pack()
# c2.pack()

# def submit():
#     if var1.get()==1 and var2.get()==1:
#         print("Both option selected")
#     elif var1.get()==1 and var2.get()==0:
#         print("Python selected")
#     elif var1.get()==0 and var2.get()==1:
#         print("Data Science selected")
#     else:
#         print("No option selected")
            

# b1=Button(root, text="Enter",command=submit)
# b1.pack()

#-----------------------------------------------------

#option menu (Dropdown menu)

# options=['BA','Bcom','BCA','MCA','BTech','Mtech','PHD']
# var=StringVar()
# var.set("Select any option")
# op=OptionMenu(root,var,*options)
# op.pack()

# def submit():
#     print(var.get())
            

# b1=Button(root, text="Enter",command=submit)
# b1.pack()


#-----------------------------------------------

# Scale

# var=IntVar()

# s=Scale(root,orient="horizontal",variable=var)
# s.pack()

# def submit():
#     print(var.get())
            

# b1=Button(root, text="Enter",command=submit)
# b1.pack()

#-------------------------------------------------

#scroll bar

# s=Scrollbar(root)
# s.pack(side="right",fill=Y)

# t1=Text(root,height=8,width=25)
# t1.pack()

# def submit():
#     # print(e1.get())
#     l1.config(text=t1.get("0.0",END))

# b1=Button(root, text="Enter",command=submit)
# b1.pack()

# l1=Label(root)
# l1.pack()

# s.config(command=t1.yview)

#----------------------------------------------

# Frame

# f=Frame(root)
# f.pack()
# s=Scrollbar(f)
# s.pack(side="right",fill=Y)

# t1=Text(f,height=8,width=25)
# t1.pack()

# def submit():
#     # print(e1.get())
#     l1.config(text=t1.get("0.0",END))

# b1=Button(root, text="Enter",command=submit)
# b1.pack()

# l1=Label(root)
# l1.pack()

# s.config(command=t1.yview)

#----------------------------------------------------

# Message box (popup)

# user="admin"
# password="1234"

# Label(root,text="Username:",bg="#6495ED").grid(row=0,column=0)
# e1=Entry(root)
# e1.grid(row=0,column=1)

# Label(root,text="Password:",bg="#6495ED").grid(row=1,column=0)
# e2=Entry(root,show='*')
# e2.grid(row=1,column=1)

# def submit():
#     if e1.get()==user and e2.get()==password:
#         messagebox.showinfo("Login","Login Sucessful")
#     else:
#         messagebox.showerror("Login","Login failed")    

# Button(root,text="Submit",command=submit).grid(row=2,column=0)

# def submit():
#     if messagebox.askokcancel('Delete','Do you want to delete ?'):
#         print("Deleted")
#     else:
#         print("Cancelled")

# Button(root,text="Delete",command=submit).grid(row=2,column=0)

#-----------------------------------------------------------------------------------------------------------------
# filedialog - open, save the file with file dilog box in GUI - To CHECK

def openfile():
    
    f=filedialog.askopenfile(filetypes=[('python file','*.py'),('Text file','*.txt'),("All files",'*.*')]) # filetype is used to open specifice type of file only
    print(f.read())
    f.write("My python file")

def savefile():
    try:
        f=filedialog.asksaveasfile(filetypes=[('python file','*.py'),('Text file','*.txt'),("All files",'*.*')])
        f.write("My python file")
    except:
        pass    

# Button(root,text="Open File",command=openfile).pack()
# Button(root, text="Save File",command=savefile).pack()


#--------------------------------------------------------------------------------------------------------

# Menu - optioin at header
# We can make menue ans submenu with same calass as menu


menubar=Menu(root) # main menu

def newfile():
    # for parient window
    # window=Tk()
    # window.geometry("300x200")

    # child window
    window=Toplevel(root)
    window.geometry("300x200")
    Button(window,text="Select").pack()

filemenu=Menu(menubar,tearoff=0) # sub menu
menubar.add_cascade(label="File",menu=filemenu)
# file menu commands
filemenu.add_command(label="New File",command=newfile)
filemenu.add_command(label="Open File",command=openfile)
filemenu.add_command(label="Save File",command=savefile)

editmenu=Menu(menubar,tearoff=0) # sub menu
menubar.add_cascade(label="Edit",menu=editmenu)
# edit menu commands
editmenu.add_command(label="Copy")

helpmenu=Menu(menubar,tearoff=0) # sub menu 
menubar.add_cascade(label="Help",menu=helpmenu)
# help menu commands
helpmenu.add_command(label="Help indexes")

root.config(menu=menubar)

root.mainloop()

# Question

# Signup and Signin form with database connectivity

# Notepad Prototype

# ATM prototype with database connectivity