from tkinter import *
from tkinter import messagebox
from Password_Generator import *
import pyperclip

'''
This program uses Tkinter to create a GUI to manage information about login.
messagebox is not a class so have to be imported by itself.
Data will be written to a text file. 
Password can be manually entered or automatically generated. 
If generated, password is automatically copied to clipboard.
Example email/username is automatically entered but if wanted it to be empty, delete line-76.
'''


def create_password():
    password = PasswordGenerator()
    # Get a password from PasswordGenerator class.
    new_password = password.password_generator()
    # Copy the generated password to the clipboard.
    pyperclip.copy(new_password)
    password_entry.insert(0, new_password)


def record_data():
    # Get website's name.
    web_name = web_entry.get().capitalize()
    # Get email or username.
    get_username = username_entry.get()
    # Get password.
    get_password = password_entry.get()
    # If any boxes is empty, pop up warning message box.
    if len(web_name) == 0 or len(get_password) < 0:
        messagebox.showerror(title="Warning!", message="Please fill all empty boxes.")
    else:
        # Get confirmation from user whether to save data entered.
        is_ok = messagebox.askokcancel(title=web_name, message=f"THESE ARE THE DETAILS ENTERED."
                                                               f"\nEmail: {get_username}\nPassword: {get_password}\n"
                                                               f"Is it alright to continue to save?")
        if is_ok:
            # Write data to a text file with append mode so subsequent data will be added to existing one.
            with open("data.txt", mode="a") as data:
                data.write(f"{web_name} | {get_username} | {get_password}\n")
            # Empty boxes for new data to be entered.
            web_entry.delete(0, END)
            password_entry.delete(0, END)
            # Send cursor to the first box.
            web_entry.focus()


# Create a GUI window.
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Add the pic using Canvas class.
canvas = Canvas(width=200, height=200)
photo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=photo)
canvas.grid(column=1, row=0)

# Create labels at desired locations.
web_label = Label(text="Website:", font=("Courier", 18))
web_label.grid(column=0, row=1)
username_label = Label(text="Email/Username:", font=("Courier", 18))
username_label.grid(column=0, row=2)
password_label = Label(text="Password:", font=("Courier", 18))
password_label.grid(column=0, row=3)

# Create boxes accordingly.
web_entry = Entry(width=35)
web_entry.grid(column=1, row=1, columnspan=2)
web_entry.focus()
username_entry = Entry(width=35)
username_entry.grid(column=1, row=2, columnspan=2)
username_entry.insert(0, "johndoe@gmail.com")
password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

# Create buttons at appropriate locations. When clicked, call the respective function.
generate_pass_button = Button(text="Generate Password", command=create_password)
generate_pass_button.grid(column=2, row=3)
add_button = Button(text="Add", width=36, command=record_data)
add_button.grid(column=1, row=4, columnspan=2)

# To keep the window stay on.
window.mainloop()
