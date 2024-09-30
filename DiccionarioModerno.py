import time

meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso.",
            "LOL": "Una respuesta común a algo gracioso.",
            "ROFL": "Una respuesta a una broma.",
            "SHEESH": "Ligera desaprobación.",
            "CREEPY": "Aterrador, siniestro.",
            "AGGRO": "Ponerse agresivo/enojado.",
            }
while True:
    word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")
    if word in meme_dict.keys():
        print(word, meme_dict[word])
    else:
        print("Esta palabra no se encuentra en el diccionario")
    time.sleep(1)
