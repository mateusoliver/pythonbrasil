tamanho = int(input('Tamanho em metros quadrados: '))
litros = tamanho / 6

if tamanho % 108 == 0:
	latas = tamanho / 108
	preco = latas * 80
	preco2 = (latas * 25)*5
	print(f"Você vai pintar {tamanho} metros. Então vai precisar de {latas} latas de 18L . E vai custar R$ {preco} ")
	print(f"Você vai pintar {tamanho} metros. Então vai precisar de {latas*5} latas de 3,6L. E vai custar R$ {preco2} ")
else:
	latas = int(tamanho / 108) + 1
	preco = latas * 80
	preco2 = (latas * 25)*5
	print(f"Vou vai pintar {tamanho} metros. Então vai precisar de {latas} latas de 18L. E vai custar R$ {preco} ")
	print(f"Vou vai pintar {tamanho} metros. Então vai precisar de {latas*5} latas de 3,6L. E vai custar R$ {preco2} ")
