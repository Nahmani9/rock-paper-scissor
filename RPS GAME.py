import tkinter as tk
import random

PLAYER_SCORE = 0
PLAYER_CHOICE = 0
COMPUTER_SCORE = 0
COMPUTER_CHOICE = 0


def random_comp():
    return random.choice(['rock', 'paper', 'scissor'])


def battle(player_choice, comp_choice):
    global PLAYER_SCORE
    global COMPUTER_SCORE
    p = to_number(player_choice)
    c = to_number(comp_choice)
    if p == c:
        print("Tie!")
    elif (p - c) % 3 == 1:
        print("Player Win!")
        PLAYER_SCORE += 1
    else:
        print("Computer Wins!")
        COMPUTER_SCORE += 1
    answer = "Player choice: {a} \nComputer choice: {b} \nPlayer score: {c} \nComputer score: {d}".format(
        a=PLAYER_CHOICE, b=COMPUTER_CHOICE, c=PLAYER_SCORE, d=COMPUTER_SCORE)
    text.delete(1.0, tk.END)
    text.insert(tk.END, answer)


def rock():
    global PLAYER_CHOICE
    global COMPUTER_CHOICE
    PLAYER_CHOICE = "rock"
    COMPUTER_CHOICE = random_comp()
    battle(PLAYER_CHOICE, COMPUTER_CHOICE)


def paper():
    global PLAYER_CHOICE
    global COMPUTER_CHOICE
    PLAYER_CHOICE = "paper"
    COMPUTER_CHOICE = random_comp()
    battle(PLAYER_CHOICE, COMPUTER_CHOICE)


def scissor():
    global PLAYER_CHOICE
    global COMPUTER_CHOICE
    PLAYER_CHOICE = "scissor"
    COMPUTER_CHOICE = random_comp()
    battle(PLAYER_CHOICE, COMPUTER_CHOICE)


def to_number(choice):
    option = {'rock': 0, 'paper': 1, 'scissor': 2}
    return option[choice]


def exit_func():
    window.destroy()
    window.quit()


window = tk.Tk()
window.geometry("245x340")
window.title("RPS GAME")
window.resizable(width=0, height=0)


head_label = tk.Label(window, text="Choose one of the following:")
head_label.grid(column=0, row=1)

rock_button = tk.Button(text="Rock", bg="yellow", command=rock)
rock_button.grid(column=0, row=2)

Paper_button = tk.Button(text="Paper", bg="yellow", command=paper)
Paper_button.grid(column=0, row=3)

Scissor_button = tk.Button(text="Scissor", bg="yellow", command=scissor)
Scissor_button.grid(column=0, row=4)

score_label = tk.Label(window, text="Score")
score_label.grid(column=0, row=5)

text = tk.Text(master=window, height=12, width=30, bg="#FFFF99")
text.grid(column=0, row=6)

exit_button = tk.Button(text="Exit", command=exit_func)
exit_button.grid(column=0, row=7)
window.mainloop()
