import tkinter as tk
import requests

URL = "https://api.kanye.rest/"

window = tk.Tk()
window.title("Kanye Says...")

window.config(pady=50, padx=50)
bg_image = tk.PhotoImage(file="images/background.png")
bg_canvas = tk.Canvas(width=300, height=414)
bg_canvas.create_image(150, 207, image=bg_image)

quote = bg_canvas.create_text(150, 207, width=250, font=("Arial", 20, "bold"), text="text ...", fill="#fff")
bg_canvas.grid(row=0, column=0)


def generate_quote():
    resp = requests.get(url=URL)
    resp.raise_for_status()
    quote_text = resp.json()["quote"]
    bg_canvas.itemconfig(quote, text=quote_text)


btn_quote = tk.Button()
btn_image = tk.PhotoImage(file="images/kanye.png")
btn_quote.config(image=btn_image, width=100, height=131, command=generate_quote)
btn_quote.grid(row=1, column=0)

window.mainloop()
