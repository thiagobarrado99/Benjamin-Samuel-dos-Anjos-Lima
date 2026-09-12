#!/usr/bin/evn python3

import os
import sys

        

def main():
    
    variavel1 = -1
    
    while variavel1 is not 0:
    
        print("")
        print("menu de opções")
        print("1: somar dois numeros")
        print("2: subtrair dois numeros")
        print("3: multiplicar dois numeros")
        print("4: dividir dois numeros")
        print("0: sair")
            
        variavel1 = input("escolha uma opção: ")
        print("")
        match variavel1:
            case "1":
                funcao1()
                
            case "2":
                funcao2()
                
            case "3":
                funcao3()
                
            case "4":
                funcao4()
                
            case "0":
                return
            case _:
                print("opção invalida")
                
            
def funcao1():
    numero1 = input("Digite o primeiro numero: ")
    numero2 = input("Digite o segundo numero: ")
    
    if numero1.isnumeric() and numero2.isnumeric():
        final = int(numero1) + int(numero2)
        print(f"A soma é: {final}")
    else:
        print("numero invalido")
    
def funcao2():
    numero1 = input("Digite o primeiro numero: ")
    numero2 = input("Digite o segundo numero: ")
    
    if numero1.isnumeric() and numero2.isnumeric():
        final = int(numero1) - int(numero2)
        print(f"A subtração é: {final}")
    else:
        print("numero invalido")
    
def funcao3():
    numero1 = input("Digite o primeiro numero: ")
    numero2 = input("Digite o segundo numero: ")
    
    if numero1.isnumeric() and numero2.isnumeric():
        final = int(numero1) * int(numero2)
        print(f"A multiplicação é: {final}")
    else:
        print("numero invalido")

def funcao4():
    numero1 = input("Digite o primeiro numero: ")
    numero2 = input("Digite o segundo numero: ")
    
    if numero1.isnumeric() and numero2.isnumeric():
        final = int(numero1) / int(numero2)
        print(f"A divisão é: {final}")
    else:
        print("numero invalido")

     
if __name__ == "__main__":
    main()