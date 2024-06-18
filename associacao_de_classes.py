class Funcionario:
    def __init__(self):
        self.nome = None
        self.escolaridade = None
        self.alocacao = None

    def set_alocacao_do_funcionario(self, alocacao):
        self.alocacao = alocacao

    def get_alocaco_do_funcionario(self):
        return self.alocacao.get_sede_do_pais()        

    def set_nome_do_funcionario(self, nome):
        self.nome = nome

    def get_nome_do_funcionario(self):
        return self.nome        

    def set_escolaridade_do_funcionario(self, escolaridade):
        self.escolaridade = escolaridade

    def get_escolaridade_do_funcionario(self):
        return self.escolaridade.get_nivel_de_escolaridade()
    
    def get_escolaridade(self):
        return self.escolaridade

class Grupo:
    def __init__(self):
        self.presidente = None

    def set_presidente_do_grupo(self, presidente):
        self.presidente = presidente

    def get_presidente_do_grupo(self):
        return self.presidente.get_nome_do_funcionario()

class Escolaridade:
    def __init__(self):
        self.nivel_de_escolaridade = None

    def set_nivel_de_escolaridade(self, escolaridade):
        self.nivel_de_escolaridade = escolaridade

    def get_nivel_de_escolaridade(self):
        return self.nivel_de_escolaridade
    
class Pais:
    def __init__(self):
        self.sede = None

    def set_sede_do_pais(self, sede):
        self.sede = sede

    def get_sede_do_pais(self):
        return self.sede

class Empresa:
    def __init__(self):
        self.estado = None
        self.diretor = None
    
    def set_diretor_da_empresa(self, diretor):
        self.diretor  = diretor

    def get_diretor_da_empresa(self):
        return self.diretor.get_nome_do_funcionario()
        
    def set_estado_da_empresa(self, estado):
        self.estado = estado

    def get_estado_da_empresa(self):
        return self.estado.get_nome_do_estado()

class Filial(Empresa):
    def __init__(self):
        Empresa.__init__(self)
        self.coordenacao = None

    def set_coordenacao_da_filial(self, coordenacao):
        self.coordenacao = coordenacao

    def get_coordenacao_da_filial(self):
        return self.coordenacao.get_nome_do_funcionario()        

class Estado:
    def __init__(self):
        self.estado = None

    def set_nome_do_estado(self, estado):
        self.estado = estado

    def get_nome_do_estado(self):
        return self.estado

class Departamento:
    def __init__(self):
        self.chefia = None

    def set_chefia_do_departamento(self, chefia):
        self.chefia = chefia 

    def get_chefia_do_departamento(self):
        return self.chefia.get_escolaridade()                    

###################################################################################################

#1
presidente = Funcionario()
escolaridade = Escolaridade()
grupo = Grupo()

presidente.set_nome_do_funcionario('Presidente Fulano')
grupo.set_presidente_do_grupo(presidente)

escolaridade.set_nivel_de_escolaridade('Ensino Médio')
presidente.set_escolaridade_do_funcionario(escolaridade)

print(presidente.get_escolaridade_do_funcionario(), presidente.get_nome_do_funcionario())

##################################################################################################

#2
pais = Pais()
funcionario = Funcionario()

pais.set_sede_do_pais('Brasil')
funcionario.set_alocacao_do_funcionario(pais)

print(funcionario.get_alocaco_do_funcionario())

##################################################################################################

#3

estado = Estado()
filial = Filial()
funcionario = Funcionario()

estado.set_nome_do_estado('Rio de Janeiro')
filial.set_estado_da_empresa(estado)

funcionario.set_nome_do_funcionario('Funcionario coordenador da empresa')
filial.set_coordenacao_da_filial(funcionario)

print(filial.get_coordenacao_da_filial(), filial.get_estado_da_empresa())

###################################################################################################

#4
funcionario = Funcionario()
departamento = Departamento()
escolaridade = Escolaridade()

funcionario.set_escolaridade_do_funcionario('Doutorado')
departamento.set_chefia_do_departamento(funcionario)

print(departamento.get_chefia_do_departamento())

####################################################################################################

#5
diretor = Funcionario()
filial = Filial()

diretor.set_nome_do_funcionario('Fulano diretor da filial')
filial.set_diretor_da_empresa(diretor)

print(filial.get_diretor_da_empresa())



