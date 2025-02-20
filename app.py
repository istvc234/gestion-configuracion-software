def saludo():
    print("Hola, Mundo")
    with open("mensaje.txt", "w") as f:
        f.write("Este es un mensaje guardado en un archivo.")

def suma(a, b):
    return a + b

saludo()
