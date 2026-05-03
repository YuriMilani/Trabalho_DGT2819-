# a. Abre o arquivo 'texto.txt' para escrita ('w' de write)
# O modo 'w' cria o arquivo caso ele ainda não exista
arquivo = open("texto.txt", "w", encoding="utf-8")

# b. Cria uma lista vazia
texto = list()

# c. Atribui frases à lista usando o método append
texto.append("Esta é a primeira frase do arquivo.\n")
texto.append("O Python facilita muito a manipulação de arquivos.\n")
texto.append("Agora estamos salvando uma lista inteira de uma vez.\n")

# d. Escreve o conteúdo da lista no arquivo aberto
arquivo.writelines(texto)

# É importante fechar o arquivo para salvar as alterações
arquivo.close()