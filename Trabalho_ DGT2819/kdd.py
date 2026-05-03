import time

# uso with

palavras_totais = list()


with open("Microatividades_DGT2819/my_text.txt", "r") as arquivo:
    conteudo = arquivo.read().split()

# metodos de ordenação

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


def selection_sort(lista):
    n = len(lista)
    
    for i in range(n):
        # Assume que o primeiro item não ordenado é o menor
        indice_minimo = i
        
        # Procura o verdadeiro menor no restante da lista
        for j in range(i + 1, n):
            if lista[j] < lista[indice_minimo]:
                indice_minimo = j
        
        # Troca o menor encontrado com o elemento da posição i
        lista[i], lista[indice_minimo] = lista[indice_minimo], lista[i]
        
    return lista


# timer

# Bubble Sort
inicio = time.time()
res_bubble = bubble_sort(palavras_totais)
fim = time.time()
print(f"Bubble Sort    | Tempo: {fim - inicio:.10f}s")

# Selection Sort
inicio = time.time()
res_selection = selection_sort(palavras_totais)
fim = time.time()
print(f"Selection Sort | Tempo: {fim - inicio:.10f}s")

# Nativo Sort
lista_nativa = palavras_totais.copy()
inicio = time.time()
lista_nativa.sort()
fim = time.time()
print(f"Nativo Sort    | Tempo: {fim - inicio:.10f}s")

# criar o arquivo

arquivo = open("texto.txt", "w", encoding="utf-8")

for palavra in conteudo:
    arquivo.write(palavra + "\n")


arquivo.close()
