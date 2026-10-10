print("classes e objetos")
class Aluno:
    nome = ""
    turma = ""
    nota = 0
    idade = 0
    status = False

    def __init__(self, nome, turma, nota, idade, status):
        self.nome = nome
        self.turma = turma
        self.nota = nota
        self.idade = idade
        self.status = status

    def __str__(self):
        return f"nome: {self.nome}, turma: {self.turma}, nota: {self.nota}, idade: {self.idade}, status: {self.status}"

class Turma:
    nome = ""
    alunos: list[Aluno] = []

    def adicionar(self, aluno):
        self.alunos.append(aluno)

    def __len__(self):
        return len(self.alunos)

    def __init__(self, nome):
        self.nome = nome

    def __str__(self):
        return f"nome: {self.nome}, Alunos: {len(self.alunos)}"
        


print("")
print("")

turmas: list[Turma] = []

opcao = 0

while opcao != 4:
    print("")
    print("")
    print("escolha uma opçao:")
    print("1 listar turmas")
    print("2 cadastrar turma")
    print("3 cadastrar aluno")
    print("4 sair")
    opcao = int(input("digite sua escolha:"))

    if opcao == 1:
        print("turmas cadastradas")
        for turma in turmas:
            print(turma)
            for aluno in turma.alunos:
                print(f"-> {aluno}")
    elif opcao == 2:
        nome = input("digite o nome da turma")
        turma = Turma(nome)
        turmas.append(turma)
        print("turma cadastrada com sucesso")
    elif opcao == 3:
        numero = 0
        for turma in turmas:
            print(f"{numero}: {turma}")
            numero += 1

        numero_turma = int(input("digite o numero da turma:"))
        nome_turma = turmas[numero_turma].nome
        nome = input("digite o nome do aluno:")
        nota = float(input("digite a nota do aluno:"))
        idade = int(input("digite a idade do aluno:"))
        status = True

        aluno = Aluno(nome, nome_turma, nota, idade, status)
        turmas[numero_turma].adicionar(aluno)
        print("aluno cadastrado com sucesso!")
    