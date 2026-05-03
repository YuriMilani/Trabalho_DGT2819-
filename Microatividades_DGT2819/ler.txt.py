# Leitura de arquivos

ler_text = open("Microatividades_DGT2819/loremipsum.txt", "r")

print("Arquivo aberto com sucesso!")

# Ler todo o conteúdo do arquivo

conteudo = ler_text.read()

print(repr(conteudo))


# Imprime apenas a primeira linha

print(ler_text.readline())

# Volta ao início do arquivo para ler os caracteres corretamente

ler_text.seek(0)

# Imprime apenas os 3 primeiros caracteres

print(ler_text.read(3))

ler_text.close()




with open("Microatividades_DGT2819/loremipsum.txt", "r") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)

    
# Fechar o arquivo

ler_text.close()