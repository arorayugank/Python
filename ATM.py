from tkinter import *
from tkinter import messagebox

balance = 10000
pin = "1234"

# Hide all frames to show only the current frame
def hide_all_frames():
    for widget in root.winfo_children():
        widget.grid_forget()

# Display the balance inquiry frame
def balenq():
    hide_all_frames()
    balance_label = Label(root, text=f"Your balance is: {balance}", font=("", 14, "bold"))
    balance_label.grid(row=7, column=5, columnspan=2, padx=10, pady=20)
    back_button = Button(root, text="Back", command=show_main_menu, bg='#378620', fg='white', font=("", 10, 'bold'))
    back_button.grid(row=10, column=5, columnspan=2, padx=10, pady=20)

# Display the withdrawal frame
def withdraw():
    hide_all_frames()
    withdraw_label = Label(root, text="Enter the amount: ", font=("", 14, "bold"))
    withdraw_label.grid(row=7, column=5, padx=10, pady=20)
    with_text = Entry(root, font=("", 14))
    with_text.grid(row=7, column=7, padx=10, pady=20)

    # Process the withdrawal
    def cash():
        global balance
        try:
            cashw = float(with_text.get())
            if cashw > balance:
                messagebox.showwarning("Insufficient Funds", "You do not have enough balance.")
            else:
                balance -= cashw
                messagebox.showinfo("Withdraw", f"{cashw} has been debited")
                show_main_menu()
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number.")
    
    cw = Button(root, text="Withdraw", command=cash, bg='#378620', fg='white', font=("", 10, 'bold'))
    cw.grid(row=10, column=7, padx=10, pady=20)
    back_button = Button(root, text="Back", command=show_main_menu, bg='#378620', fg='white', font=("", 10, 'bold'))
    back_button.grid(row=10, column=5, padx=10, pady=20)

# Display the mini statement frame (currently a placeholder)
def mini_statement():
    hide_all_frames()
    ms_label = Label(root, text="Mini Statement", font=("", 14, "bold"))
    ms_label.grid(row=7, column=5, columnspan=2, padx=10, pady=20)
    back_button = Button(root, text="Back", command=show_main_menu, bg='#378620', fg='white', font=("", 10, 'bold'))
    back_button.grid(row=10, column=5, columnspan=2, padx=10, pady=20)

# Display the change PIN frame
def change_pin():
    hide_all_frames()
    current_pin_label = Label(root, text="Enter current PIN:", font=("", 14, "bold"))
    current_pin_label.grid(row=7, column=5, padx=10, pady=20)
    current_pin_entry = Entry(root, font=("", 14), show="*")
    current_pin_entry.grid(row=7, column=7, padx=10, pady=20)

    new_pin_label = Label(root, text="Enter new PIN:", font=("", 14, "bold"))
    new_pin_label.grid(row=8, column=5, padx=10, pady=20)
    new_pin_entry = Entry(root, font=("", 14), show="*")
    new_pin_entry.grid(row=8, column=7, padx=10, pady=20)

    confirm_pin_label = Label(root, text="Confirm new PIN:", font=("", 14, "bold"))
    confirm_pin_label.grid(row=9, column=5, padx=10, pady=20)
    confirm_pin_entry = Entry(root, font=("", 14), show="*")
    confirm_pin_entry.grid(row=9, column=7, padx=10, pady=20)

    # Process the PIN change
    def update_pin():
        global pin
        if current_pin_entry.get() == pin:
            if new_pin_entry.get() == confirm_pin_entry.get():
                pin = new_pin_entry.get()
                messagebox.showinfo("PIN Change", "PIN successfully changed")
                show_main_menu()
            else:
                messagebox.showerror("Error", "New PIN and Confirm PIN do not match")
        else:
            messagebox.showerror("Error", "Current PIN is incorrect")

    change_button = Button(root, text="Change PIN", command=update_pin, bg='#378620', fg='white', font=("", 10, 'bold'))
    change_button.grid(row=10, column=7, padx=10, pady=20)
    back_button = Button(root, text="Back", command=show_main_menu, bg='#378620', fg='white', font=("", 10, 'bold'))
    back_button.grid(row=10, column=5, padx=10, pady=20)

# Display the main menu
def show_main_menu():
    hide_all_frames()
    be = Button(root, text="Balance Enquiry", command=balenq, bg='#378620', fg='white', font=("", 14, 'bold'))
    be.grid(row=3, column=0, padx=10, pady=20)

    cw = Button(root, text="Cash Withdrawal", command=withdraw, bg='#378620', fg='white', font=("", 14, 'bold'))
    cw.grid(row=3, column=1, padx=10, pady=20)

    ms = Button(root, text="Mini Statement", command=mini_statement, bg='#378620', fg='white', font=("", 14, 'bold'))
    ms.grid(row=4, column=0, padx=10, pady=20)

    cp = Button(root, text="Change PIN", command=change_pin, bg='#378620', fg='white', font=("", 14, 'bold'))
    cp.grid(row=4, column=1, padx=10, pady=20)

# Initialize the main application window
root = Tk()
root.geometry("600x600")
root.title("ATM")

# Show the main menu
show_main_menu()

# Start the main event loop
root.mainloop()
