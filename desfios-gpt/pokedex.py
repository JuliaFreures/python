from turtle import title
import pypokedex
import PIL.Image, PIL.ImageTk
import tkinter as tk
import urllib3
from io import BytesIO

window = tk.Tk()
window.geometry("600x500")
window.title("Pokedéx - Python")
window.config(padx=10, pady=10, bg="#f44336")

title_label = tk.Label(window, text="Pokedéx")
title_label.config(font=("Arial", 32, "bold"), bg="#f44336", fg= "white")
title_label.pack(padx=10, pady=10)

pokemon_image = tk.Label(window, bg="#f44336")
pokemon_image.pack(padx=10, pady=10)

pokemon_information = tk.Label(window)
pokemon_information.config(font=("Arial", 20, "bold"), bg="#f44336", fg="white")
pokemon_information.pack(padx=10, pady=10)

pokemon_types = tk.Label(window)
pokemon_types.config(font=("Arial", 20), bg="#f44336", fg="white")
pokemon_types.pack(padx=10, pady=10)



#function
def load_pokemon():
    try:
        name_or_id = text_id_name.get().strip().lower()
        if not name_or_id:
            pokemon_information.config(text="Digite um nome ou ID!", fg="yellow")
            return
    
        
        pokemon = pypokedex.get(name=text_id_name.get())

        http = urllib3.PoolManager()
        response = http.request('GET', pokemon.sprites.front['default'])
        image = PIL.Image.open(BytesIO(response.data))

        img = PIL.ImageTk.PhotoImage(image)
        pokemon_image.config(image = img)
        pokemon_image.image = img

        pokemon_information.config(text=f"{pokemon.dex} - {pokemon.name.title()}")
        pokemon_types.config(text="Tipos:"+ " - ".join([t.title() for t in pokemon.types]))
        
    except Exception:
        pokemon_information.config(text="Pokémon não encontrado!", fg="yellow")
        pokemon_image.config(image="")
       
        

label_id_name = tk.Label(window,text="ID or Name:")
label_id_name.config(font=("Arial", 20), bg="#f44336", fg="white")
label_id_name.pack(padx=10, pady=10)

text_id_name = tk.Entry(window,  font=("Arial", 20), justify="center")
text_id_name.pack(padx=10, pady=10)

bnt_load= tk.Button(window,text="Carregar Pokemon", command=load_pokemon)
bnt_load.config(font=("Arial", 20, "bold"), bg="#ffcc00")
bnt_load.config(command=load_pokemon)
bnt_load.pack(padx=10, pady=10)





window.mainloop()
