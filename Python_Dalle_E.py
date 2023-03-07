# create.py

import os

import openai
restart = True
risposta = '/'

while restart:
    #il prompt contiene la stringa che rappresenta la richiesta fatta a DALL-E sull'immagine da generare
    promptUtente = input("inserisci qualcosa che vorresti vedere realizzato come immagine\n")

    openai.api_key = "Inserisci qui la tua API Key"

    response = openai.Image.create(
        prompt=promptUtente,
        n=1,
        size="1024x1024",
    )

    print(response["data"][0]["url"])
    risposta = input("Vuoi generare un'altra immagine? (y- si, qualunque altro tasto per uscire)")
    if risposta == 'y':
        restart = True
    else:
        restart = False