#IMPORTS
from tkinter.ttk import *
from tkinter import *
import pandas as pd
import random

#CONSTANTS AND VARIABLES
BACKGROUND_COLOR = "#B1DDC6"
#TIME IN SECONDS TO FLIP THE CARD
TIME_SECONDS = 3
#FONT OF THE LANGUAGE
TITLE_FONT = ("SF Compact Display", 35, "italic")
#FONT OF THE WORD
WORD_FONT = ("SF Pro Display", 60, "bold")
#LANGUAGES SYMBOLS FOR TEXT-TO-SPEACH FEATURE
LANGUAGE1_SYMBOL = "fr"
LANGUAGE2_SYMBOL = "pt-BR"
#PATH TO YOUR LANGUAGE DICT (DELETE words_to_learn.csv)
DICT_PATH = "Day 31 - Flashy\\data\\french_words.csv"
current = None


#READ DATA
data = pd.read_csv(DICT_PATH)
data_index = pd.read_csv(DICT_PATH)

#CHECK IF words_to_learn DATA ALREADY EXISTS,
#IF NOT CREATE ONE WITH ALL WORDS OF YOUR MAIN DATA
try:
    data = pd.read_csv("Day 31 - Flashy\data\\words_to_learn.csv")

except:
    data.to_csv("Day 31 - Flashy\data\\words_to_learn.csv", index=False)
    data = pd.read_csv("Day 31 - Flashy\data\\words_to_learn.csv")

#CREATE A DICT WITH THE DATA
data = data.to_dict(orient="records")


#IS CALLED WHEN CLICK IN WRONG BUTTON,
# AND CALL RANDOM WORD METHOD WITHOUT DELETING DATA FROM words_to_learn
def no_remove_data():
    random_word(False)

#FLIP THE CARD (CHANGE THE CANVAS IMAGE),
# AND DISPLAY THE SECOND LANGUAGE AND WORD IN THE SCREEN
def flip_card(current, button):
    #GET THE NAME OF THE SECOND LANGUAGE
    language_name2 = data_index.columns[1]
    #GET THE WORD FOR THE SECOND LANGUAGE
    language_word2 = current[language_name2]
    #CHANGE CANVAS IMAGE AND TEXT
    canvas.itemconfig(flip_image, image=card_back)
    canvas.itemconfig(title_text, text=language_name2, fill="white")
    canvas.itemconfig(word_text, text=language_word2, fill="white")
    #ENABLE BUTTONS AGAIN
    right_button.config(state="normal")
    wrong_button.config(state="normal")


#GENERATE RANDOM NUMBER FOR CHOOSE AN WORD,
# DISPLAY THE FIRST LANGUAGE NAME AND THE WORD IN THE SCREEN
def random_word(button=True):
    global current
    #CHECK IF IS TO REMOVE THE WORD FROM words_to_learn
    try:
        if button == True:
            data.remove(current)
            pd.DataFrame(data).to_csv(
                "Day 31 - Flashy\data\\words_to_learn.csv", index=False)
    except:
        pass
    #GENERATE RANDOM CHOICE
    current = random.choice(data)
    #GET THE NAME OF THE FIRST LANGUAGE
    language_name1 = data_index.columns[0]
    #GET THE RANDOM WORD
    language_word1 = current[language_name1]
    #CHANGE CANVAS IMAGE AND TEXT
    canvas.itemconfig(flip_image, image=card_front)
    canvas.itemconfig(title_text, text=language_name1, fill="black")
    canvas.itemconfig(word_text, text=language_word1, fill="black")
    #DISABLE BUTTONS
    right_button.config(state="disabled")
    wrong_button.config(state="disabled")
    #IN (TIME_SECONDS) SECONDS FLIP THE CARD
    window.after(TIME_SECONDS * 1000, flip_card, current, button)


#WINDOW SETUP
window = Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=30)

#IMAGE VARIABLES
card_front = PhotoImage(file="Day 31 - Flashy\\images\\card_front.png")
card_back = PhotoImage(file="Day 31 - Flashy\\images\\card_back.png")
right_photo = PhotoImage(file="Day 31 - Flashy\\images\\right.png")
wrong_photo = PhotoImage(file="Day 31 - Flashy\\images\\wrong.png")

#CREATE CANVAS
canvas = Canvas(width=810,
                height=550,
                bg=BACKGROUND_COLOR,
                highlightthickness=0)

#CREATE CANVAS ITENS
flip_image = canvas.create_image(412, 263, image=card_front)
title_text = canvas.create_text(412, 150, text="Flashy", font=TITLE_FONT)
word_text = canvas.create_text(412,
                               263,
                               text="Click on green\nbutton to start",
                               font=WORD_FONT)

#BUTTONS
right_button = Button(image=right_photo,
                      bg=BACKGROUND_COLOR,
                      borderwidth=0,
                      relief="flat",
                      command=random_word)

wrong_button = Button(image=wrong_photo,
                      bg=BACKGROUND_COLOR,
                      borderwidth=0,
                      relief="flat",
                      command=no_remove_data,
                      state="disabled")

#GRID
canvas.grid(row=0, column=0, columnspan=2)
right_button.grid(row=1, column=1)
wrong_button.grid(row=1, column=0)

#MAIN LOOP
window.mainloop()
