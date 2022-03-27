from cProfile import label
from operator import length_hint
from tkinter import *
from turtle import color
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 1
timer = None
# # ---------------------------- TIMER RESET ------------------------------- # 
def resetTimer():
  window.after_cancel(timer)
  canvas.itemconfig(canvasText, text="00:00")
  marks = ""
  howManyPomodoros["text"] = marks
  timerLabel["text"] = "Timer"
  global reps
  reps = 0

# # ---------------------------- TIMER MECHANISM ------------------------------- # 
def startTimer():
  global reps
  if reps % 8 == 0:
    countDown(LONG_BREAK_MIN * 60)
    timerLabel["text"] = "Long Break"
    timerLabel["fg"] = RED

  elif reps % 2 == 0:
    countDown(SHORT_BREAK_MIN * 60)
    timerLabel["text"] = "Break"
    timerLabel["fg"] = PINK

  else:
    countDown(WORK_MIN * 60)
    timerLabel["text"] = "Work"
    timerLabel["fg"] = GREEN
    
  reps += 1

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countDown(count):

  minutes = math.floor(count / 60)
  seconds = (count % 60)

  if seconds < 10:
    seconds = f"0{seconds}"

  canvas.itemconfig(canvasText, text=f"{minutes}:{seconds}")
  if(count > 0):
    global timer
    timer = window.after(1000, countDown, count - 1)
  else:
    startTimer()
    if reps % 2 == 0:
      marks = ""
      workSessions = math.floor(reps/2)
      for _ in range(workSessions):
        marks += "✔"
      howManyPomodoros["text"] = marks


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomadoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
imageTomato = PhotoImage(file="tomato.png")

timerLabel = Label(text="Timer", font=(FONT_NAME, 35, "bold"), fg=GREEN, bg=YELLOW)
timerLabel.pack()

canvas.create_image(100, 112, image = imageTomato)
canvasText = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 25, "bold"))
canvas.pack()

howManyPomodoros = Label(text="✔", font=(FONT_NAME, 10, "bold"), fg=GREEN, bg=YELLOW)
howManyPomodoros.pack()

startButton = Button(text="Start", width=10, command = startTimer)
startButton.place(x=-0, y=320)

resetButton = Button(text="Reset", width=10, command = resetTimer)
resetButton.place(x=110, y=320)

window.mainloop()
