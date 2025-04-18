from turtle import title
import pypokedex
import PIL.Image, PIL.ImageTk
import tkinter as tk
import urllib3
from io import BytesIO

window = tk.Tk()
window.geometry("600x500")
window.title("NeuralNine Pokedex Tutorial")
window.config(padx=10, pady=10)

title_label = tk.Label(window, text="NeuralNine Pokedex")
title_label.config(font=("Arial", 32))
title_label.pack(padx=10, pady=10)

pokemon_image = tk.Label(window)
pokemon_image.pack(padx=10, pady=10)

pokemon_information = tk.Label(window)
pokemon_information.config(font=("Arial", 20))
pokemon_information.pack(padx=10, pady=10)

pokemon_types = tk.Label(window)
pokemon_types.config(font=("Arial", 20))
pokemon_types.pack(padx=10, pady=10)

#function
def load_pokemon():
    pokemon = pypokedex.get(name=text_id_name.get(1.0, "end-1c"))

    http = urllib3.PoolManager()
    response = http.request('GET', pokemon.sprites.front.get('default'))
    image = PIL.Image.open(BytesIO(response.data))

    img = PIL.ImageTk.PhotoImage(image)
    pokemon_image.config(image = img)
    pokemon_image.image = img

    pokemon_information.config(text=f"{pokemon.dex} - {pokemon.name}")
    pokemon_types.config(text=" - ".join([t.title() for t in pokemon.types]))

label_id_name = tk.Label(window,text="ID or Name:")
label_id_name.config(font=("Arial", 20))
label_id_name.pack(padx=10, pady=10)

text_id_name = tk.Text(window, height=1)
text_id_name.config(font=("Arial", 20))
text_id_name.pack(padx=10, pady=10)

bnt_load= tk.Button(window,text="Load Pokemon", command=load_pokemon)
bnt_load.config(font=("Arial", 20))
bnt_load.config(command=load_pokemon)
bnt_load.pack(padx=10, pady=10)





window.mainloop()
