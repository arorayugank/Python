from tkinter import *
from tkinter import messagebox, filedialog

# Function to handle form submission
def submit():
    # Get the values from the entry fields and option menus
    fname = entry_fname.get()
    lname = entry_lname.get()
    email = entry_email.get()
    pwd = entry_password.get()
    gender = var.get()
    birth_date = dvar.get()
    birth_month = mvar.get()
    birth_year = yvar.get()

    # Validate that all fields are filled
    if not fname or not lname or not email or not pwd or gender == "Select your gender" or birth_date == "Date" or birth_month == "Month" or birth_year == "Year":
        # Show error message if any field is empty
        messagebox.showerror("Error", "Please fill all fields")
    else:
        # Show success message if all fields are filled
        messagebox.showinfo("Success", "Signup successful")

# Create the main application window
root = Tk()
root.geometry("500x500")  # Set window size
root.title("Insta")  # Set window title

# Change application icon
photo = PhotoImage(file=r"C:\Users\Disha\Downloads\insta.png")
root.iconphoto(False, photo)

# Set application background color
root.config(bg="#EBEEF2")

# Create and place the "Sign up" label
sign_up = Label(root, text="Sign up", bg="#EBEEF2", fg="#355580", font=("", 15, "bold"))
sign_up.grid(row=0, column=1, columnspan=2, padx=10, pady=5)

# Create and place the "First Name" label and entry field
first_name = Label(root, text="First Name", bg="#EBEEF2", fg="#355580", font=("", 12))
first_name.grid(row=1, column=0, padx=10, pady=5)

entry_fname = Entry(root, width=20, font=("", 12))
entry_fname.grid(row=1, column=1, padx=10, pady=5)

# Create and place the "Last Name" label and entry field
last_name = Label(root, text="Last Name", bg="#EBEEF2", fg="#355580", font=("", 12))
last_name.grid(row=2, column=0, padx=10, pady=5)

entry_lname = Entry(root, width=20, font=("", 12))
entry_lname.grid(row=2, column=1, padx=10, pady=5)

# Create and place the "Your mail ID" label and entry field
Email_ID = Label(root, text="Your mail ID", bg="#EBEEF2", fg="#355580", font=("", 12))
Email_ID.grid(row=3, column=0, padx=10, pady=5)

entry_email = Entry(root, width=20, font=("", 12))
entry_email.grid(row=3, column=1, padx=10, pady=5)

# Create and place the "Password" label and entry field
password = Label(root, text="Password", bg="#EBEEF2", fg="#355580", font=("", 12))
password.grid(row=4, column=0, padx=10, pady=5)

entry_password = Entry(root, width=20, font=("", 12), show='*')
entry_password.grid(row=4, column=1, padx=10, pady=5)

# Create and place the "Gender" label and option menu
gender = Label(root, text="Gender", bg="#EBEEF2", fg="#355580", font=("", 12))
gender.grid(row=5, column=0, padx=10, pady=5)

options = ['Male', 'Female']
var = StringVar()
var.set("Select your gender")
op = OptionMenu(root, var, *options)
op.grid(row=5, column=1, padx=10, pady=5)

# Create and place the "Birthday" label and option menus for date, month, and year
dob = Label(root, text="Birthday", bg="#EBEEF2", fg="#355580", font=("", 12))
dob.grid(row=6, column=0, padx=10, pady=5)

# Date option menu
date = list(range(1, 32))
dvar = StringVar()
dvar.set("Date")
op1 = OptionMenu(root, dvar, *date)
op1.grid(row=6, column=1, padx=10, pady=5)

# Month option menu
month = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
mvar = StringVar()
mvar.set("Month")
op2 = OptionMenu(root, mvar, *month)
op2.grid(row=6, column=2, padx=10, pady=5)

# Year option menu
year = list(range(1900, 2025))
yvar = StringVar()
yvar.set("Year")
op3 = OptionMenu(root, yvar, *year)
op3.grid(row=6, column=3, padx=10, pady=5)

# Create and place the "Signup" button
b1 = Button(root, text="Signup", command=submit, bg='#378620', fg='white', font=("", 14, 'bold'))
b1.grid(row=7, column=1, padx=10, pady=5)

# Run the main application loop
root.mainloop()
