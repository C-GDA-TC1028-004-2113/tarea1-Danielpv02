def main():
    #escribe tu código abajo de esta línea
    men = int(input("Dame el número de mensajes: "))
    meg = float(input("Dame el número de megas: "))
    min = int(input("Dame el número de minutos: "))
    print("El costo mensual es: " + str(men*0.80 + meg*0.80 + min*0.80))




if __name__ == '__main__':
    main()
