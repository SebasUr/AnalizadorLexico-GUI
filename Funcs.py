import re
import os
def buscarEnDic(palabra):
    if len(palabra) != 0:
        carpetaDic = '.\dics'
        dirFiles = os.listdir(carpetaDic)
        palabra = palabra.lower()

        for archivo in dirFiles:
            if archivo.lower().startswith(palabra[0].lower()):
                with open(os.path.join(carpetaDic, archivo), 'r') as archivo_txt:
                    lineas = archivo_txt.readlines()
                    for linea in lineas:
                        if palabra in linea.strip().split():
                            return True
    else:
        return False


def convertirAEmoji(textoA):
    dicEmojis = {":\)":"🙂", ":\(":"🙁", ":D":"😀",
                 ":o":"😲", ":p":"😛", ":3":"🐶",
                 ":'\(":"😢", ";\)":"😉", "xD":"😁", 
                 "<3": "❤️","\(y\)":"👍","\:O":"😲"}
    numEmojis = 0 
    numPalabras = 0

    for palabra in textoA.split(" "):
        for keys,values in dicEmojis.items():
            palabra = re.sub(keys, " ", palabra)
        if len(palabra.split(" ")):
            for palabra in palabra.split(" "):
                if (buscarEnDic(palabra) and len(palabra)>1) or (len(palabra)>1 and (")" not in palabra or ":" not in palabra)):
                    numPalabras = numPalabras + 1
        else:
            if (buscarEnDic(palabra) and len(palabra)>1) or (len(palabra)>1 and (")" not in palabra or ":" not in palabra)):
                numPalabras = numPalabras + 1

    for keys,values in dicEmojis.items():
        textoA = re.sub(keys, values, textoA)
        numEmojis = numEmojis + len(re.findall(values,textoA))
    
    
    return textoA, numEmojis, numPalabras

# texto = "HolacomoEstas:)"
# patron = ":)"
# busqueda = re.search(patron,texto)
# print(busqueda)

# texto = "Si necesi:)tas ayudall:)am:)a al (658)-598-9977"
# patron = ":\)"

# busqueda = re.findall(patron,texto)
# print(busqueda) 

# hola = re.finditer(patron,texto)
# print(f" - {hola}")

# print(re.sub(patron, "🙂", texto, count=0, flags=0))

# for hallazgo in re.finditer(patron,texto):
#     print(hallazgo.span())
    