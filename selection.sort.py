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

numeros = [64, 25, 12, 22, 11]
print(selection_sort(numeros))
