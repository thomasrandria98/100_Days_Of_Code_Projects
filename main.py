
## -------- Library Imports ------ ##
from tkinter import *
import random
import pandas as pd

## ------- Constants--------- ##
BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = []


##------ Functionality ------- ##



try:
    data = pd.read_csv("Data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("Data/french_words.csv")
    print(original_data)
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")






def draw_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=foreground_img)
    flip_timer = window.after(3000, func=card_flip)



def card_flip():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=background_img)


def is_known():
    to_learn.remove(current_card)
    print(len(to_learn))
    data = pd.DataFrame(to_learn)
    data.to_csv("Data/words_to_learn.csv", index=False)
    draw_card()


## ---------------- UI setup ------------##

window = Tk()
window.title("Flash Card App Capstone")
window.configure(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=card_flip)

# Flash card Canvas
canvas = Canvas(width=800, height=526, bg="white")
background_img = PhotoImage(file="Images/card_back.png")
foreground_img = PhotoImage(file="Images/card_front.png")
card_background = canvas.create_image(400, 263, image=foreground_img)
card_title = canvas.create_text(400, 150, text="", font=("Arial", 40) )
card_word = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold") )
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)


# wrong button
wrong_image = PhotoImage(file="Images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=draw_card)
wrong_button.grid(row=1, column=0)

# right button

right_image = PhotoImage(file="Images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=is_known)
right_button.grid(row=1, column=1)




draw_card()



window.mainloop()