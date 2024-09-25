""" Escreva um programa que verifique, em uma string, a existência da letra 'a', seja maiúscula ou minúscula, além de informar a quantidade de vezes em que ela ocorre. """

def verificar(texto):
    contador = 0
    encontrada = False

    for letra in texto:
        if letra.lower() == 'a':
            contador += 1
            encontrada = True

    return encontrada, contador

texto = input("Digite um texto: ")
resultado, quantidade = verificar(texto)

if resultado:
    print(f"A letra 'a' foi encontrada {quantidade} vezes no texto.")
else:
    print("A letra 'a' não foi encontrada no texto.")