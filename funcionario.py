#Classes: Funcionário, Gerente, Diretor
#Funcionário: nome, cpf, salário,
#método para calcular bônus (5% do salário)
#Gerente: departamento, método para calcular bônus (10% do salário + 500)
#Diretor: método para calcular bônus (15% do salário + 1000)

class Funcionario:
    def __init__(self):
        self.nome = ''
        self.cpf = 0
        self.salario = 0

    def setNome(self, nome):
        self.nome = nome
    def getNome(self):
        return self.nome
    def setCpf(self, cpf):
        self.cpf = cpf
    def getCpf(self):
        return self.cpf
    def setSalario(self, salario):
        self.salario = salario
    def getSalario(self):
        return self.salario

    def calculaBonus(self):
        self.salario += (5/100) * self.salario

class Gerente(Funcionario):
    def __init__(self):
        super().__init__()
        self.departamento = ''

    def setDepartamento(self, departamento):
        self.departamento = departamento

    def getDepartamento(self):
        return self.departamento

    def bonusGerente(self):
        self.salario += (10/100) * self.salario + 500

class Diretor(Funcionario):
    def __init__(self):
        super().__init__()

    def bonusDiretor(self):
        self.salario += (15/100) * self.salario + 1000


