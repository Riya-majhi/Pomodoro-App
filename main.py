from tkinter import *
import math
from playsound import playsound
#---------------------------------------CONSTANTS---------------------------

PINK= "#e2979c"
RED= "#e7385b"
BLUE= "#205375"
YELLOW= "#f7f5dd"
GREEN="#008000"
PURPLE="#ba55d3"
FONT_NAME= "Courier"
WORK_MIN= 25
SHORT_BREAK_MIN= 5
LONG_BREAK_MIN= 30
reps=0 #repetation
marks = 0 #count no of promodaro
timer = None
#---------------------------------------TIMER RESET-------------------------------

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text,text="00:00")
    title_label.config(text="Timer")
    promodaro_count.config(text="Pomodaros:0")
    

#---------------------------------------TIMER PAUSE--------------------------------

def pause_timer():
    window.after_cancel(timer)
  
#---------------------------------------TIMER MECHANISM---------------------------

def start_timer():
    global reps
    reps+=1                                             #whenever count_own ends it add one repeatation
    work_sec = WORK_MIN*60                              #calculate 25 min
    short_break_sec = SHORT_BREAK_MIN*60                #calculate 5 min
    long_break_sec = LONG_BREAK_MIN * 60                #calculate 30 min

    if reps % 8 == 0:                                   #when 8 repetatio are completed
        count_down(long_break_sec)                      #calls count_down
        title_label.config(text="30 min Break", fg=RED) #change of label
        
    elif reps % 2 == 0:                                 #when repetation is even short break will work
        count_down(short_break_sec)
        title_label.config(text="5min Break", fg=PURPLE) #change of label
        playsound('alarm1.mp3')
        
    else:                                               #when repetation is odd work timer will work   
        count_down(work_sec)
        title_label.config(text="WORK TIME", fg=GREEN)  #change of label
        print(reps)
        if(reps>1):
            playsound('alarm1.mp3')
        

#---------------------------------------COUNTDOWN MECHANISM---------------------------

def count_down(count):

    count_min = math.floor(count/60)                    #converts the decimal into whole number converted to minute
    count_sec = count % 60                              #converted into second

    if count_sec < 10: 
        count_sec=f"0{count_sec}"                       #when timer is less than 10 it converts into 09,08,..

    
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}") #format to display the timer
    if (count>0):                                       #timer should not move to negative
        global timer
        timer = window.after(1000, count_down, count-1)         #1000 means 1 sec, count_down for recursion, count-1 to reduce the time
    else:
        start_timer()                                   #starting point of timer
        #if reps % 2 == 0:
         #   global pro_counts
          #  pro_count+=1
           # promodaro_count.config(text=f"{pro_count}")
        global marks 
        work_sessions = math.floor(reps%2)
        for _  in range(work_sessions):
            marks+=1
        promodaro_count.config(text=f"Pomodaros:{marks}")   

#---------------------------------------UI SETUP----------------------------------

window=Tk()
window.title("Pomodaro")
window.config(padx=50,pady=50, bg=YELLOW)


title_label = Label(text="Timer", fg=BLUE, bg=YELLOW, font=(FONT_NAME,30,"bold")) 
title_label.grid(column=1,row=0)                        #the page is divided into grid column and row


canvas = Canvas(width = 200,height = 200, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato2.png")
canvas.create_image(100,100, image=tomato_img)          #placing the image in grid
timer_text = canvas.create_text(105,105,text="00:00",fill="white",font=(FONT_NAME,20,"bold"))
canvas.grid(column=1,row=1)


start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

#pause_button = Button(text="Pause", command=pause_timer)
#pause_button.grid(column=1, row=2)

reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(column=2,row=2)

promodaro_count = Label(text="Pomodaros:0", fg=BLUE, bg=YELLOW, font=(FONT_NAME,15,"bold"))
promodaro_count.grid(column=1,row=3)

window.mainloop()





















