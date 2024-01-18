
imagem = int(input("Entre com o tamanho da imagem em MB: "))
link = int(input("Entre com a velocidade do link de internet com Mbps: "))
tempo = (imagem/(link/8))
print(f"Voce vai gastar {tempo} segundos.")
