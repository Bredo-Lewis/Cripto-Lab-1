import sys

def cifrado_cesar(texto, desplazamiento):
    alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    resultado = ""

    for char in texto.upper():  # pasamos todo a mayúsculas
        if char in alfabeto:
            idx = alfabeto.index(char)
            nueva_idx = (idx + desplazamiento) % len(alfabeto)
            resultado += alfabeto[nueva_idx]
        else:
            resultado += char
    return resultado

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Por favor. Ingrese a una terminal y compile usando: py 'Nombre Archivo.py' 'Palabra' 'numero desplazamientos'")
        sys.exit(1)

    palabra = sys.argv[1]
    try:
        n = int(sys.argv[2])
    except ValueError:
        print("El número de desplazamientos debe ser un entero.")
        sys.exit(1)

    cifrado = cifrado_cesar(palabra, n)
    print("Texto cifrado:", cifrado)
