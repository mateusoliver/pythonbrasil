import time
peso = float(input("Entre com o valor do peixe: "))
multa=((peso-50)*4)
passou=(peso-50)
if peso<50:
	print("Voce não excedeu peso do seu peixe. Bom churasco. Me chame.")
if peso>50:
	print("vamos calcular sua multa:...")
	time.sleep(2)
	print(f"Você passou {passou} kilos e vai precisar pagar: R$ {multa}")
