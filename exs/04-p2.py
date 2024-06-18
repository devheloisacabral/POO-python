#Qual a escolaridade do chefe de um departamento?

class Escolaridade:
    def __init__(self):
        self.nivel = None

    def set_nivel_escolaridade(self, nivel):
        self.nivel = nivel

    def get_nivel_escolaridade(self):
        return self.nivel
    

class Departamento:
    def __init__(self):
        self.chefia = None

    def set_chefia_do_departamento(self, chefia):
        self.chefia = chefia

    def get_chefia_do_departamento(self):
        return self.chefia

class Funcionario:
    def __init__(self):
        self.chefia = None
        self.escolaridade = None      
        
    def get_escolaridade(self):
        if self.escolaridade == None or self.escolaridade == '':
            return 'Sem escolaridade'
        else:
            return self.escolaridade.get_nivel_escolaridade()

    def set_escolaridade(self, escolaridade):
        self.escolaridade = escolaridade

    def set_funcionario_chefe(self, chefia):
        self.chefia = chefia

    def get_funcionario_chefe(self):
        return self.chefia.get_chefia_do_departamento()
    
#Qual a escolaridade do chefe de um departamento?

funcionario = Funcionario()
departamento = Departamento()
escolaridade = Escolaridade()

departamento.set_chefia_do_departamento('fulano')
funcionario.set_funcionario_chefe(departamento)

escolaridade.set_nivel_escolaridade('Doutorado')
funcionario.set_escolaridade(escolaridade)

print(funcionario.get_funcionario_chefe(), funcionario.get_escolaridade())
