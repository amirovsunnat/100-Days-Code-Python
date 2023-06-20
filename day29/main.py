import tkinter as tk


# set up window
tkinter_ = tk.Tk()
tkinter_.title("Password manager")
tkinter_.minsize(width=650, height=450)
tkinter_.config(pady=50, padx=50)
FONT = ("Arial", 16, "normal")

# # function for validating user input
# def validate_entry():
#     """Check entries are empty or not"""
#     if

# set up canvas
canvas = tk.Canvas(height=200, width=200)
image_ = tk.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image_)
canvas.grid(row=0, column=1)

# website label and entry
website_label = tk.Label(text="Website:", font=FONT, padx=30, pady=10)
website_label.grid(row=1, column=0, sticky='w')
website_entry = tk.Entry(width=35, font=FONT, highlightthickness=2, highlightcolor="blue")  # highlight color
website_entry.focus()  # focus mode
website_entry.grid(row=1, column=1, columnspan=2)
# email label and entry
email_label = tk.Label(text="Email/Username:", font=FONT)
email_label.grid(row=2, column=0, sticky='w')
email_entry = tk.Entry(width=35, font=FONT, highlightthickness=2, highlightcolor="blue")
email_entry.insert(string="amirovsunnat@gmail.com", index=0)  # setting up default email
email_entry.grid(row=2, column=1, columnspan=2)
# password label and entry
password_label = tk.Label(text="Password:", font=FONT, pady=10)
password_label.grid(row=3, column=0)
password_entry = tk.Entry(width=22, font=FONT, highlightthickness=2, highlightcolor="blue")
password_entry.grid(row=3, column=1, sticky='w')

# generate password button
generate_pas = tk.Button(text="Generate Password", font=("Arial", 10, "bold"), width=17, bg="white")
generate_pas.grid(row=3, column=2, sticky='e')
generate_pas.config(pady=2)

# add button
add = tk.Button(text="Add", font=("Arial", 10, "bold"), width=35, bg="white")
add.grid(row=4, column=1, columnspan=2, sticky='we')

tkinter_.mainloop()

