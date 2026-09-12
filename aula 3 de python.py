print("aula de loops e tipagem")

listanumeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("lista simples :")
print(listanumeros)

print("")

dobros = [n * 2 for n in listanumeros]

print("lista dobrada :")
print(dobros)

print("")

listacortada = listanumeros[1:3]
print("lista cortada com operador [:] :")
print(listacortada)

print("")

dobro_dos_pares = [item * 2      
                   for item in listanumeros 
                   if item % 2 == 0]

print("dobro dos numeros pares: ")
print(dobro_dos_pares) 

metade_dos_pares = [item / 2      
                   for item in listanumeros 
                   if item % 2 == 0]

print("metade dos numeros pares: ")
print(metade_dos_pares)

print("")

dicionario = [
    {"nome":"benjamin", "nota": 10},
    {"nome":"thiago", "nota": 10},
    {"nome":"lucca", "nota": 8},
    {"nome":"pedro", "nota": 9.5}
]


nomesdodicionario = [item["nome"] for item in dicionario]
print("nomes exrtraidos: ")
print(nomesdodicionario)

notasdodicionario = [item["nota"] for item in dicionario]
print("notas exrtraidos: ")
print(notasdodicionario)

totaisdodicionario = [f" {item["nome"]} tirou {item["nota"]}"
                                                 for item in dicionario]
print("notas dos alunos: ")
print(totaisdodicionario)


def dobrar (x: int) -> int:
    return x * 2

print("testando erro de tipagem")
print( dobrar(2) )
print( dobrar(8.2) )
print( dobrar([1, 2]) )
print( dobrar("oi") )