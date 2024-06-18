#qual o estado da filial que um funcionario coordena?

#classes: filial, estado, funcionario

class Funcionario:
    def __init__(self):
        self.coordenacao = None
        self.alocacao_funcionario = ''

    def set_alocacao_funcionario(self, alocacao):
        self.alocacao_funcionario = alocacao

    def get_alocacao_funcionario(self):
        return self.alocacao_funcionario.get_nome_do_estado()

    def set_funcionario_coordenador(self, coordenacao): 
        self.coordenacao = coordenacao

    def get_funcionario_coordenador(self):
        return self.coordenacao
       
class Estado:
    def __init__(self):
        self.nome_do_estado = ''

    def set_nome_do_estado(self, nome_do_estado):
        self.nome_do_estado = nome_do_estado

    def get_nome_do_estado(self):
        return self.nome_do_estado

class Filial:
    def __init__(self):
        self.estado = None

    def set_estado_da_filial(self, estado):
        self.estado = estado

    def get_estado_da_filial(self):
        return self.estado
    
#qual o estado da filial que um funcionario coordena?

funcionario = Funcionario()
estado = Estado()
filial = Filial()


estado.set_nome_do_estado('Rio de Janeiro')
funcionario.set_alocacao_funcionario(estado)
print(funcionario.get_alocacao_funcionario())








