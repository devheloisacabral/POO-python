#qual o nome do diretor da empresa de uma filial?

#classes: empresa, filial, funcionario

class Empresa:
    def __init__(self):
        self.diretor = None

    def set_diretor_da_empresa(self, diretor):
        self.diretor = diretor

    def get_diretor_da_empresa(self):
        return self.diretor.get_nome_do_funcionario()

class Filial(Empresa):
    def __init__(self):
        Empresa.__init__(self)

class Funcionario:
    def __init__(self):
        self.nome = None

    def set_nome_do_funcionario(self, nome):
        self.nome = nome

    def get_nome_do_funcionario(self):
        return self.nome 

#qual o nome do diretor da empresa de uma filial?


diretor = Funcionario()
filial = Filial()

diretor.set_nome_do_funcionario('Fulado Diretor da empresa de uma filial')
filial.set_diretor_da_empresa(diretor)

print(filial.get_diretor_da_empresa())


