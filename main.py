import tkinter as tk
import pandas
import random

# -------------------- CONSTANTS --------------------
BACKGROUND_COLOR = "#B1DDC6"

# -------------------- DATA --------------------
data = pandas.read_csv("data/french_words.csv")
to_learn = data.to_dict(orient="records")

current_card = {}

# -------------------- FUNCTIONS --------------------

def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)


def next_card():
    global current_card, flip_timer

    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)

    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)

    flip_timer = window.after(3000, flip_card)

# -------------------- UI SETUP --------------------
window = tk.Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card)

# Canvas
canvas = tk.Canvas(
    width=800,
    height=526,
    bg=BACKGROUND_COLOR,
    highlightthickness=0
)

card_front_img = tk.PhotoImage(file="images/card_front.png")
card_back_img = tk.PhotoImage(file="images/card_back.png")

card_background = canvas.create_image(400, 263, image=card_front_img)

card_title = canvas.create_text(
    400, 150,
    text="",
    fill="black",
    font=("Arial", 40, "italic")
)

card_word = canvas.create_text(
    400, 263,
    text="",
    fill="black",
    font=("Arial", 60, "bold")
)

canvas.grid(row=0, column=0, columnspan=2)

# Buttons
cross_image = tk.PhotoImage(file="images/wrong.png")
unknown_button = tk.Button(
    image=cross_image,
    highlightthickness=0,
    command=next_card
)
unknown_button.grid(row=1, column=0)

check_image = tk.PhotoImage(file="images/right.png")
known_button = tk.Button(
    image=check_image,
    highlightthickness=0,
    command=next_card
)
known_button.grid(row=1, column=1)

# -------------------- START --------------------
next_card()
window.mainloop()
