import turtle
from tkinter import *
import random

Bank_account = 0


## Turtle Game Setup
def turtle_stuff():

    turtle.screensize(canvwidth=500, canvheight=500)

    class turtle_details():

        def __init__(self, color):
            self.color = color
            self.turt = turtle.Pen()
            self.turt.color(color)
            self.turt.shape('turtle')
















def enter_input():
    global turtle_bet
    global bet_amount

    turtle_bet = user_turtle_bet.get()
    bet_amount = user_bet_amount.get()
    turtle_stuff() # trigger the turtle code
    return turtle_bet, bet_amount


## Tkinter Entry Setup
tk = Tk()

user_turtle_bet = StringVar()
user_bet_amount = StringVar()

user_turtle_label = Label(tk, text="Turtle Bet", font=('Times', 13, 'bold'))
user_turtle_entry = Entry(tk, textvariable=user_turtle_bet, font=('Times', 13, 'normal'))

user_amount_label = Label(tk, text="Bet Amount", font=('Times', 13, 'bold'))
user_amount_entry = Entry(tk, textvariable=user_bet_amount, font=('Times', 13, 'normal'))

enter_button = Button(tk, text="ENTER", command=enter_input)

user_turtle_label.grid(row=0, column=0)
user_turtle_entry.grid(row=0, column=1)
user_amount_label.grid(row=1, column=0)
user_amount_entry.grid(row=1, column=1)
enter_button.grid(row=2, column=1)

tk.mainloop()








