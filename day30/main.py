import tkinter as tk
from tkinter import messagebox
# import string library function
import string
# Importing random to generate
import random
import pyperclip  # for copying the password
import json

# set up window
tkinter_ = tk.Tk()
tkinter_.title("Password manager")
tkinter_.minsize(width=650, height=500)
tkinter_.config(pady=50, padx=50)
FONT = ("Arial", 16, "normal")
BORDER_COLOR = "light blue"


# define a save function for saving all the information user provided
def save_info():
    website_name = website_entry.get().title()
    email = email_entry.get()
    password = password_entry.get()
    website_info = {
        website_name: {
            "email": email,
            "password": password
        }
    }

    # password or website entry validation
    if len(website_name) <= 0 or len(password) <= 0:
        messagebox.showwarning(title="Missing fields", message="Please make sure all the fields filled.")
    else:
        try:
            with open("passwords.json", mode="r") as file:
                #  reading old info
                info = json.load(file)
        except FileNotFoundError:
            with open("passwords.json", "w") as file:
                json.dump(website_info, file, indent=4)
        else:
            #  updating info
            info.update(website_info)
            with open("passwords.json", mode="w") as file:
                #  writing new info
                json.dump(info, file, indent=4)
        finally:
            website_entry.delete(0, len(website_name))
            password_entry.delete(0, len(password))


# Storing the value in variable letters
letters = string.ascii_letters

# Storing the value in variable numbers
numbers = string.digits

# Storing the sets of punctuation in variable symbols
symbols = string.punctuation


def rand_password_generate():
    # Takes random choices from
    # letters, numbers, and symbols
    generate_pass = ''.join([random.choice(
        letters + numbers + symbols)
        for n in range(12)])
    password_entry.insert(0, generate_pass)
    pyperclip.copy(generate_pass)  # copy the generated password to clipboard you can paste it right away


# define a function for searching password
def search_password():
    try:
        with open("passwords.json", "r") as data:
            website_info = json.load(data)
        website_name = website_entry.get().title()
    except FileNotFoundError:
        messagebox.showwarning(title="Error", message="File does not exist.")
    else:
        try:
            messagebox.showinfo(title=website_name,
                                message=f"Email: {website_info[website_name]['email']}\n"
                                        f"Password {website_info[website_name]['password']}")
        except KeyError:
            messagebox.showinfo(message=f"{website_name} is not in your password file.")


# set up canvas
canvas = tk.Canvas(height=200, width=200)
image_ = tk.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image_)
canvas.grid(row=0, column=1)

# website label and entry
website_label = tk.Label(text="Website:", font=FONT, padx=30, pady=10)
website_label.grid(row=1, column=0, sticky='w')
website_entry = tk.Entry(width=25, font=FONT, highlightthickness=2, highlightcolor=BORDER_COLOR) # highlight color
website_entry.focus()  # focus mode
website_entry.grid(row=1, column=1)
# email label and entry
email_label = tk.Label(text="Email/Username:", font=FONT)
email_label.grid(row=2, column=0, sticky='w')
email_entry = tk.Entry(width=35, font=FONT, highlightthickness=2, highlightcolor="blue")
email_entry.insert(string="amirovsunnat@gmail.com", index=0)  # setting up default email
email_entry.grid(row=2, column=1, columnspan=2, sticky="we")
# password label and entry
password_label = tk.Label(text="Password:", font=FONT, pady=10)
password_label.grid(row=3, column=0)
password_entry = tk.Entry(width=22, font=FONT, highlightthickness=2, highlightcolor="blue")
password_entry.grid(row=3, column=1, sticky='we')

# generate password button
generate_pas = tk.Button(text="Generate Password", font=("Arial", 10, "bold"), width=17, bg="white",
                         command=rand_password_generate, background="light blue")
generate_pas.grid(row=3, column=2, sticky='we')
generate_pas.config(pady=2)

# add button
add = tk.Button(text="Add", font=("Arial", 10, "bold"), width=35, bg="white", command=save_info,
                background="light blue")
add.grid(row=4, column=1, columnspan=2, sticky='we')

# search button
search = tk.Button(text="Search", font=("Arial", 10, "bold"), width=35, bg="white", background="light blue",
                   command=search_password)
search.grid(row=1, column=2)

tkinter_.mainloop()
