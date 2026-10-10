import csv
import json

print("aula de arquivo e erros")

arquivo = open("teste.txt", "r", encoding="utf-8")
conteudo = arquivo.read()
arquivo.close()

print(conteudo)

arquivo = open("escrito.txt", "w", encoding="utf-8")
conteudo = arquivo.write("ola mundo")
arquivo.close()

with open("teste.txt", "r", encoding="utf-8") as arquivo:
    conteudo = arquivo.read()
    arquivo.close()


alunos = [
    {"nome": "benjamin", "nota": 10},
    {"nome": "maria", "nota": 4},
    {"nome": "laura", "nota": 8.5},
    {"nome": "henrrique", "nota": 9}
]

with open("alunos.csv", "w", encoding="utf-8", newline="") as arquivo:
    escritor = csv.DictWriter(arquivo, fieldnames=["nome", "nota"])
    escritor.writeheader()
    escritor.writerows(alunos)


with open("alunos.csvs", "r", encoding="utf-8", newline="") as arquivo:
    leitor = csv.DictReader(arquivo)
    arquvo_alunos = list(leitor)
    print(arquvo_alunos)

with open("alunos.json", "w", encoding="utf-8", newline="") as arquivo:
    json.dump(alunos, arquivo, indent=2, ensure_ascii=False)

with open("alunos.json", "r", encoding="utf-8", newline="") as arquivo:
    alunos__json = json.load(arquivo)
    print(alunos__json)

try:
    print("print normal")
    with open("grupo.json", "r", encoding="utf-8", newline="") as arquivo:
        alunos__json = json.load(arquivo)
        print(alunos__json)

except Exception:
    print("deu erro")
else:
    print("erro nao encontrado try/except")


finally:
    print("final do bloco try/except")


