# Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo
import time
print("Este programa testa se o número é positivo ou negativo")
num = int(input("Entre com o valor para teste: "))
time.sleep(3)
if num==0:
    print("Você digitou um número nulo.")
if num>0:
    print(f"Você digitou o número {num}, POSITIVO.")
if num<0:
    print(f"Você digitou o número {num}, NEGATIVO.")
