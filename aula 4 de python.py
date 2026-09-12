print("dicionario e funçoes")

alunos = [
    ("ana", 8.5),
    ("bruno", 4.0),
    ("carla", 9.20)
]

for nome, nota in alunos:
    print(f"{nome} tirou {nota}")

notas = {"ana": 8.5, "bruno": 4.0, "carla": 9.2}

print("funçao keys()")

print( notas.keys())

print("funçao values()")
print(notas.values())

print("funçao items()")
print(notas.items())

reprovados =[
    nome
    for nome, nota in notas.items()
    if nota < 6
]

print("alunos reprovados:")
print(reprovados)

print("maior nota da turma:")
print(max(notas.values()))

print("menor nota da turma:")
print(min(notas.values()))

aluno = {
    "nome": "ben",
    "idade": "12",
    "status": True,
    "notas": {
        "matematica": 8.0,
        "portugues": 8.0,
        "historia": 9.0
    }
}

print(f"nome do aluno: {aluno['nome']}")
print(f"nota em matematica: {aluno['notas']['matematica']}")
