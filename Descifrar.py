import sys

def descifrar_cesar(texto):
    alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    resultados = []

    for desplazamiento in range(26):
        resultado = ""
        for char in texto.upper():
            if char in alfabeto:
                idx = alfabeto.index(char)
                nueva_idx = (idx - desplazamiento) % len(alfabeto)
                resultado += alfabeto[nueva_idx]
            else:
                resultado += char  # deja espacios y símbolos igual
        resultados.append((desplazamiento, resultado))
    return resultados


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Por favor. Ingrese a una terminal y compile usando: py 'Nombre Archivo.py' 'mensaje cifrado'")
        sys.exit(1)

    # Une todos los argumentos en un solo string, por si hay espacios
    texto = " ".join(sys.argv[1:])

    resultados = descifrar_cesar(texto)

    for desplazamiento, posible in resultados:
        print(f"Desplazamiento {desplazamiento:2}: {posible}")
