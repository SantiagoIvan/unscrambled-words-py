palabras_desordenadas = open("palabras_target.txt","r")
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

for palabra_desordenada in palabras_desordenadas:
    print("Analizando ",palabra_desordenada)
    wordlist = open("wordlist.txt","r")
    for word in wordlist:
        if(es_palabra_desordenada(palabra_desordenada.rstrip("\n"), word.rstrip("\n"))):
            print("Palabra encontrada ", palabra_desordenada.rstrip("\n"), " vs ", word.rstrip("\n"))
            respuesta.append(word.rstrip("\n"))
            break
    wordlist.close()

print(str(respuesta).replace(" ","").lstrip("[").rstrip("]").replace("'",""))
palabras_desordenadas.close()
