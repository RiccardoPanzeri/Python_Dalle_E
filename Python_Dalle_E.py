

import openai
restart = True
risposta = '/'

while restart:
    #il prompt contiene la stringa che rappresenta la richiesta fatta a DALL-E sull'immagine da generare;
    promptUtente = input("inserisci qualcosa che vorresti vedere realizzato come immagine\n")
    #Chiave API OpenAI personale
    openai.api_key = "Inserisci qui la tua chiave API OpenAI"

    response = openai.Image.create(#genero l'immagine;
        prompt=promptUtente,
        n=1,#setto il numero di immagini da creare a 1;
        size="1024x1024",#dimensioni immagine;
    )

    print(response["data"][0]["url"])#genero il link URL che, se aperto tramite browser, mostrerà l'immagine generata;
    #permetto all'utente di generare altre immagini
    risposta = input("Vuoi generare un'altra immagine? (y- si, qualunque altro tasto per uscire)")
    if risposta == 'y':
        restart = True
    else:
        restart = False