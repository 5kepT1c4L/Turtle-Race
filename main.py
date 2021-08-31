import turtle
from tkinter import *
import random

Bank_account = 0


class turtle_s:

    def __init__(self, color):
        self.color = color
        self.turt = turtle.Pen()
        self.turt.shape('turtle')
        self.turt.color(color)


red_turtle = turtle_s('red')
blue_turtle = turtle_s('blue')
yellow_turtle = turtle_s('yellow')

turtle_list = [red_turtle, blue_turtle, yellow_turtle]


## Turtle Game Setup
def turtle_stuff():

    turtle.screensize(canvwidth=500, canvheight=500)
    turtle.bgcolor('black')

    for color_turtle in turtle_list:

        if turtle_list.index(color_turtle) % 3 == 0:

            color_turtle.turt.penup()
            color_turtle.turt.setpos(-300, -250)
            color_turtle.turt.left(90)

        elif turtle_list.index(color_turtle) % 3 == 1:

            color_turtle.turt.penup()
            color_turtle.turt.setpos(300, -250)
            color_turtle.turt.left(90)

        else:

            color_turtle.turt.penup()
            color_turtle.turt.setpos(0, -250)
            color_turtle.turt.left(90)







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








