from tkinter import *
import math
from tkinter import messagebox
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
Check_green="#06D001"
tomatored="#EE4E4E"
FONT_NAME = "Courier"
WORK_MIN = 1#25
SHORT_BREAK_MIN =1# 5
LONG_BREAK_MIN = 1#20
reps=0
time_counter=None

# ---------------------------- TIMER RESET ------------------------------- #
def reset():
    window.after_cancel(time_counter)
    timerlabel.config(text="Timer")
    checkmark.config(text="")
    canvas.itemconfig(timer_txt,text="00.00")
    global reps
    reps=0



# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_time():
    global reps
    reps+=1
    work_sec = WORK_MIN*60
    s_break_sec = SHORT_BREAK_MIN*60
    l_break_sec = LONG_BREAK_MIN*60

    if reps % 8 == 0:
        timerlabel.config(text="Break",fg=RED)
        count_down(l_break_sec)
        messagebox.showinfo(title="Break",message="Take a long break!")
    elif reps % 2==0:
        timerlabel.config(text="Break",fg=PINK)
        count_down(s_break_sec)
        messagebox.showinfo(title="Break",message="Take a short break!")
    else:
        timerlabel.config(text="Work")
        count_down(work_sec)






# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    min=math.floor(count/60)    ##To get in minutes
    sec=count % 60     ##To get in seconds
    if sec < 10:
        sec=f"0{sec}"
    canvas.itemconfig(timer_txt,text=f"{min}:{sec}")
    if count>0:
        global time_counter
        time_counter=window.after(1000, count_down, count-1)
    else:
        start_time()
        a=""
        work_session=math.floor(reps/2)
        for i in range(work_session):
            a += "✔"
        checkmark.config(text=a)

# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=GREEN)
canvas=Canvas(width=200,height=224,bg=GREEN,highlightthickness=0)
img=PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=img)
timer_txt=canvas.create_text(100,130,text="00.00",fill="white", font=(FONT_NAME,35,"bold"))
canvas.grid(column=1,row=1)


##Timer label
timerlabel=Label(text="Timer", fg=tomatored,bg=GREEN,font=(FONT_NAME,45,"bold"))
timerlabel.grid(column=1,row=0)


##checkmark label
checkmark=Label(bg=GREEN, fg=Check_green)
checkmark.grid(column=1,row=3)


##Button
start_button=Button(text="Start",command=start_time)
start_button.grid(column=0,row=2)
reset_button=Button(text="Reset",command=reset)
reset_button.grid(column=2,row=2)


window.mainloop()