#qual a escolaridade de um presidente de um grupo

class Escolaridade:
    def __init__(self):
        self.nivel = ''

    def set_escolaridade(self, nivel):
        self.nivel = nivel

    def get_escolaridade(self):
        return self.nivel

class Funcionario:
    def __init__(self): 
        self.escolaridade = None      
        
    def get_escolaridade(self):
        if self.escolaridade == None or self.escolaridade == '':
            return 'Sem escolaridade'
        else:
            return self.escolaridade

    def set_escolaridade(self, escolaridade):
        self.escolaridade = escolaridade

class Grupo:
    def __init__(self):
        self.presidente = ''   

    def get_presidente(self):
        return self._presidente

    def set_presidente(self, presidente):
        self._presidente = presidente   


escolaridade = Escolaridade()
escolaridade.set_escolaridade('')

presidente = Funcionario()
escolaridade_do_presidente = presidente.set_escolaridade(escolaridade.get_escolaridade())

grupo = Grupo()
grupo.set_presidente(presidente.get_escolaridade())

print(grupo.get_presidente())


