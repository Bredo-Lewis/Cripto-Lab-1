from scapy.all import IP, ICMP, send
import sys

def enviar_icmp_texto(destino, mensaje):
    for char in mensaje:
        paquete = IP(dst=destino)/ICMP()/char.encode()
        send(paquete, verbose=False)
        print(f"Enviado: {char} -> {destino}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Por favor. Ingrese a una terminal y compile usando: py 'Nombre Archivo.py' 'IP_DESTINO' 'mensaje cifrado'")
        sys.exit(1)

    destino = sys.argv[1]
    mensaje = sys.argv[2]

    enviar_icmp_texto(destino, mensaje)
