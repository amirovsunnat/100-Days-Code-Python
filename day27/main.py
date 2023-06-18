import tkinter as tk

tkinter_ = tk.Tk()
tkinter_.title("Miles to kilometer converter")
tkinter_.minsize(width=300, height=200)
tkinter_.config(padx=15, pady=15)
FONT = ("Arial", 20, "bold")


# define a function to calculate miles to km
def cal_mil_km():
    miles = text_entry.get()
    kilometers = round(float(miles) * 1.609344, ndigits=2)
    label2.config(text=str(kilometers))


label1 = tk.Label(text="is equal to", font=FONT)
label1.grid(column=0, row=1)
label1.config(padx=20)

label2 = tk.Label(text="0", font=FONT)
label2.grid(column=1, row=1)
label2.config(pady=20)

label3 = tk.Label(text="Km", font=FONT)
label3.grid(column=2, row=1)

text_entry = tk.Entry(font=FONT)
text_entry.grid(column=1, row=0)
text_entry.config(width=10)

label4 = tk.Label(text="Miles", font=FONT)
label4.grid(column=2, row=0)
label4.config(padx=30)

calculate_button = tk.Button(text="Calculate", font=FONT, command=cal_mil_km)
calculate_button.grid(column=1, row=2)

tkinter_.mainloop()
