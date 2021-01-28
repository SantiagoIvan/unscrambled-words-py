lista_palabras_desordenadas = list()
palabras_desordenadas = open("palabras_target.txt","r")
for palabra in palabras_desordenadas:
    lista_palabras_desordenadas.append(palabra.rstrip("\n"))
palabras_desordenadas.close()
registro_de_letras1 = {}
registro_de_letras2 = {}
respuesta = list()

def apariciones_de_letras(palabra, dict):
    for letra in palabra:
            if(letra in dict):
                dict[letra] += 1
            else:
                dict[letra] = 1

def es_palabra_desordenada(desordenada, ordenada):
    if(len(desordenada)==len(ordenada)):
        registro_de_letras1.clear()
        registro_de_letras2.clear()
        apariciones_de_letras(desordenada, registro_de_letras1)
        apariciones_de_letras(ordenada, registro_de_letras2)
        return registro_de_letras1==registro_de_letras2

wordlist = open("wordlist.txt","r")
for word in wordlist:
    new_word = word.rstrip("\n")
    for i in range(len(lista_palabras_desordenadas)):
        if(es_palabra_desordenada(lista_palabras_desordenadas[i], new_word)):
            lista_palabras_desordenadas[i] = new_word
            break
wordlist.close()

print(str(lista_palabras_desordenadas).lstrip("[").rstrip("]").replace("'","").replace(" ",""))