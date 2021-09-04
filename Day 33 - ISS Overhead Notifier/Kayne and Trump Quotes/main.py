from tkinter import *
import requests


def trump():
    get_quote("trump")


def get_quote(person=""):

    if person == "trump":
        url = "https://api.whatdoestrumpthink.com/api/v1/quotes/random/"
        a = "t"
    else:
        url = "https://api.kanye.rest/"
        a = "k"
    response = requests.get(url=url)
    response.raise_for_status()
    data = response.json()
    sizes = [(0, 30), (60, 26), (70, 22), (80, 19)]

    for size in sizes:
        if len(data["message"] if a == "t" else data["quote"]) > size[0]:
            canvas.itemconfig(
                quote_text,
                text=data["message"] if a == "t" else data["quote"],
                font=("Arial", size[1], "bold"))
        else:
            break
    print(data["message"])


window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(
    file="Day 33 - ISS Overhead Notifier\Kayne and Trump Quotes\\background.png"
)
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150,
                                207,
                                text="Kanye Quote Goes HERE",
                                width=250,
                                font=("Arial", 30, "bold"),
                                fill="white")
canvas.grid(row=0, column=0, columnspan=2)

kanye_img = PhotoImage(
    file="Day 33 - ISS Overhead Notifier\Kayne and Trump Quotes\kanye.png")
trump_img = PhotoImage(
    file="Day 33 - ISS Overhead Notifier\Kayne and Trump Quotes\\trump.png", width=100, height=130)
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
trump_button = Button(image=trump_img, highlightthickness=0, command=trump)
kanye_button.grid(row=1, column=0)
trump_button.grid(row=1, column=1)

window.mainloop()