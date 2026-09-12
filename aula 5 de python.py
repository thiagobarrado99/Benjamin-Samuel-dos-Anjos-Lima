print("aula de funções.")

def somar(numero1, numero2):
    return numero1 + numero2

def subtrair(numero1, numero2):
    return numero1 - numero2

def somarvarios(*numeros):
    return sum(numeros)

def criar_dicionario(**dados):
    return dados

def criar_aluno(nome, idade, nota, status=True):
    return {"nome": nome, "idade": idade, "nota": nota, "status": status}

#print("digite dois numeros para somar e subtrair")
#numero1 = float(input("numero1:"))
#numero2 = float(input("numero2:"))

#resultado_soma = somar(numero1, numero2)
#resultado_subtração = subtrair(numero1, numero2)

#print(f"resultado da soma: {resultado_soma}")
#print(f"resultado da subteção: {resultado_subtração}")

somatotal = somarvarios(2, 4, 10, 12, 3123, 4312321, 4111424, 1233331, 334)
print(f"soma total: {somatotal}")

aluno1 = criar_aluno("benjamin", 12, "9.5")
aluno2 = criar_aluno("joão", 8, "8", False)

aluno3 = criar_aluno(idade=10, nota=6, nome="joaquim")

print(f"aluno1: {aluno1}")
print(f"aluno2: {aluno2}")
print(f"aluno3: {aluno3}")

dicionario = criar_dicionario(nome="benjamin", 
                              idade="26",
                              status=True)

print(dicionario)
funcao_lambda = lambda *numeros: sum(numeros)
soma_lambda = funcao_lambda(3452, 4565, 545656, 7666)

print(f"resultado da funcao lambda: {soma_lambda}")