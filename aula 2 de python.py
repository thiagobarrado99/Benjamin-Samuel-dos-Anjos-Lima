nome = input("qual é seu nome")
idade = int(input("quantos anos você tem"))
peso = float(input("qual é seu peso"))
altura = float(input("qual é sua altura"))
imc = round( peso / (altura**2),2)
if imc < 18.5:
    print(f"{nome}, voce tem {idade} anos e imc de {imc}classificado como abaixo do peso")
if imc >= 18.5:
    print(f"{nome}, voce tem {idade} anos e imc de {imc}classificado como peso normal")
if imc >= 25 and imc < 29.9:
    print(f"{nome}, voce tem {idade} anos e imc de {imc}classificado como sobrepeso")
if imc >= 30 and imc < 34.9:
    print(f"{nome}, voce tem {idade} anos e imc de {imc}classificado como obesidade grau I ")
if imc >= 35 and imc < 39.9:
    print(f"{nome}, voce tem {idade} anos e imc de {imc}classificado como obesidade grau II ")
if imc >= 40:
    print(f"{nome}, voce tem {idade} anos e imc de {imc}classificado como obesidade grau III")