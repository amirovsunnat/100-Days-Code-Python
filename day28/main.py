import math
import tkinter as tk


# set up constants
RED = "#E21818"
BLUE = "#00235B"
YELLOW = "#FFF7D4"
LIGHT_BLUE = "#98DFD6"
FONT_STYLE = "Courier"
WORKING_MINUTES = 30
BREAK_MINUTES = 5
LONG_BREAK_MINUTES = 20


# define a function for keeping track of time
def time_count_down(count):
    """Takes a number and updates time_track"""
    if count > 0:
        minutes = math.floor(count / 60)
        seconds = count % 60
        if seconds == 0:
            seconds = "00"
        canvas.itemconfig(time_track, text=f"{minutes}:{seconds}")
        tkinter_.after(1000, time_count_down, count-1)


# define a start timer function 00
def start_timer():
    """Starts the time_count_down function"""
    # call time_count_down function
    time_count_down(300)


# define a function for resetting a time
def reset_time():
    time_count_down(0)


# set up a window
tkinter_ = tk.Tk()
tkinter_.title("Pomidor")
tkinter_.config(padx=120, pady=60, bg=YELLOW)


# create a canvas
canvas = tk.Canvas(height=224, width=200, bg=YELLOW, highlightthickness=0)
image_ = tk.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=image_)
time_track = canvas.create_text(100, 130, text="00:00", font=(FONT_STYLE, 30, "bold"), fill="white")
canvas.grid(column=1, row=1)

# set up a Timer label and check label
timer_label = tk.Label(text="Timer", fg=LIGHT_BLUE, font=(FONT_STYLE, 50, "bold"), bg=YELLOW)
timer_label.grid(column=1, row=0)

# check label
check_label = tk.Label(text="✔", fg=LIGHT_BLUE, font=(FONT_STYLE, 20, "bold"), bg=YELLOW)
check_label.grid(column=1, row=3)
check_label.config(pady=20)

# start and reset buttons
start = tk.Button(text="Start", font=20, bg="white", command=start_timer)
start.grid(column=0, row=2)

# reset
reset = tk.Button(text="Reset", font=20, bg="white", command=reset_time)
reset.grid(column=2, row=2)


tkinter_.mainloop()
