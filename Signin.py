from tkinter import *
from tkinter import messagebox, filedialog

def submit():
    # Function to handle the sign-in action
    username = entry_uname.get()
    password = entry_password.get()
    # Add your validation or submission logic here
    messagebox.showinfo("Login Info", f"Username: {username}\nPassword: {password}")

root = Tk()  # This class will create layout

root.geometry("500x300")
root.title("Myapp")

# Change app icon
photo = PhotoImage(file=r"c:\Users\Disha\Downloads\insta.png")
root.iconphoto(False, photo)

# App background
root.config(bg="#EBEEF2")

# Frame for image
image_frame = Frame(root, bg="#EBEEF2")
image_frame.grid(row=0, column=0, padx=20, pady=20)

# Image on Canvas
photo1 = PhotoImage(file=r"c:\Users\Disha\Downloads\insta.png")
canvas = Canvas(image_frame, width=200, height=200)  # Set desired dimensions
canvas.pack()
canvas.create_image(0, 0, anchor=NW, image=photo1)
canvas.image = photo1  # Keep a reference to avoid garbage collection

# Frame for login details
login_frame = Frame(root, bg="#EBEEF2")
login_frame.grid(row=0, column=1, padx=20, pady=20, sticky=N)

# Sign-in label
sign_in = Label(login_frame, text="Sign in", bg="#EBEEF2", fg="#355580", font=("", 15, "bold"))
sign_in.grid(row=0, column=0, columnspan=2, padx=10, pady=5)

# User Name label and entry
user_name = Label(login_frame, text="User Name", bg="#EBEEF2", fg="#355580", font=("", 12))
user_name.grid(row=1, column=0, padx=10, pady=5, sticky=E)
entry_uname = Entry(login_frame, width=20, font=("", 12))
entry_uname.grid(row=1, column=1, padx=10, pady=5)

# Password label and entry
password = Label(login_frame, text="Password", bg="#EBEEF2", fg="#355580", font=("", 12))
password.grid(row=2, column=0, padx=10, pady=5, sticky=E)
entry_password = Entry(login_frame, width=20, font=("", 12), show='*')
entry_password.grid(row=2, column=1, padx=10, pady=5)

# Signin button
b1 = Button(login_frame, text="Sign in", command=submit, bg='#378620', fg='white', font=("", 14, 'bold'))
b1.grid(row=3, column=0, columnspan=2, padx=10, pady=20)

root.mainloop()
