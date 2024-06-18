#qual o país de alocacao de um funcionario?

class Funcionario:
    def __init__(self):
        self.alocacao_funcionario = None

    def set_alocacao_funcionario(self, alocacao):
        self.alocacao_funcionario = alocacao

    def get_alocacao_funcionario(self):
        return self.alocacao_funcionario    

class Pais:
    def __init__(self):
        self.sede = None

    def set_sede(self, sede):
        self.sede = sede

    def get_sede(self):
        return self.sede

funcionario = Funcionario()
pais = Pais()

pais.set_sede('Brasil')
funcionario.set_alocacao_funcionario(pais.get_sede())

print(funcionario.get_alocacao_funcionario())