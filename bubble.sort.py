def bubble_sort(lista):
    n = len(lista)
    # Loop para percorrer toda a lista n vezes
    for i in range(n):
        # O último elemento já está no lugar, então ignoramos o final
        for j in range(0, n - i - 1):
            # COMPARAÇÃO DE ADJACENTES:
            if lista[j] > lista[j + 1]:
                # TROCA (Swap Pythônico):
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

numeros = [12, 45, 7, 89, 33, 56, 21, 94, 2, 67, 38, 51, 14, 76, 82]
print(bubble_sort(numeros))