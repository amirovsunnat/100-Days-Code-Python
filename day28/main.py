import math
import tkinter as tk


# set up constants
RED = "#CD1818"
PINK = "#DB005B"
YELLOW = "#FFF7D4"
LIGHT_BLUE = "#98DFD6"
FONT_STYLE = "Courier"
WORKING_MINUTES = 30
BREAK_MINUTES = 5
LONG_BREAK_MINUTES = 20
reps = 0  # variable for changing timestamp
timer = None


# define a function for keeping track of time
def time_count_down(count):
    """Takes a number and updates time_track"""
    minutes = math.floor(count / 60)
    seconds = count % 60
    if seconds < 10:
        seconds = f"0{seconds}"
    canvas.itemconfig(time_track, text=f"{minutes}:{seconds}")
    if count > 0:
        global timer
        timer = tkinter_.after(1000, time_count_down, count-1)
    elif count == 0:
        start_timer()
        check_labels = ""  # keeping track of checks
        for i in range(int(reps/2)):
            check_labels += "✔"
        check_label.config(text=check_labels)


# define a start timer function 00
def start_timer():
    """Starts the time_count_down function"""
    # call time_count_down function
    global reps
    reps += 1
    working_seconds = WORKING_MINUTES * 60
    break_seconds = BREAK_MINUTES * 60
    long_break_seconds = LONG_BREAK_MINUTES * 60

    if reps % 2 == 0:
        time_count_down(break_seconds)
        timer_label.config(text="BREAK", fg=PINK)
    elif reps % 8 == 0:
        time_count_down(long_break_seconds)
        timer_label.config(text="BREAK", fg=RED)
    else:
        time_count_down(working_seconds)
        timer_label.config(text="WORK")


# define a function for resetting a time
def reset_time():
    tkinter_.after_cancel(timer)
    canvas.itemconfig(time_track, text=f"00:00")
    timer_label.config(text="TIMER", fg=LIGHT_BLUE)
    check_label.config(text="")
    # reset reps in order to behave properly
    global reps
    reps = 0


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
check_label = tk.Label(text="", fg=LIGHT_BLUE, font=(FONT_STYLE, 20, "bold"), bg=YELLOW)
check_label.grid(column=1, row=3)
check_label.config(pady=20)

# start and reset buttons
start = tk.Button(text="Start", font=20, bg="white", command=start_timer)
start.grid(column=0, row=2)

# reset
reset = tk.Button(text="Reset", font=20, bg="white", command=reset_time)
reset.grid(column=2, row=2)


tkinter_.mainloop()
