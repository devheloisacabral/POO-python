class Livro:
    def __init__(self):
        self.titulo =''
        self.autor_principal=''
        self.ano = 0
        self.editora = ''
        self.isbn=0
        self.estado=True
        self.quantidade_emprestimos=0

    def setTitulo(self, titulo):
        self.titulo=titulo
    def getTitulo(self):
        return self.titulo
    def setAutorPrincipal(self, autor_principal):
        self.autor_principal=autor_principal
    def getAutorPrincipal(self):
        return self.autor_principal
    def setEditora(self, editora):
        self.editora=editora
    def getEditora(self):
        return self.editora
    def setIsbn(self, isbn):
        self.isbn=isbn
    def getIsbn(self):
        return self.isbn
    def setEstado(self, estado):
        self.estado=estado
    def getEstado(self):
        return self.estado
    def setQuantidadeEmprestimos(self, quantidade_emprestimos):
        self.quantidade_emprestimos=quantidade_emprestimos
    def getQuantidadeEmprestimos(self):
        return self.quantidade_emprestimos
    def setAno(self, ano):
        self.ano=ano
    def getAno(self):
        return self.ano
    def emprestar(self):
        if self.estado == True:
            self.quantidade_emprestimos += 1
            self.estado=False
            print('O livro foi emprestado')
        else:
            print('Esse livro está indisponível para empréstimo')

    def devolver(self):
        if self.estado == False:
            self.estado=True
            print('Livro foi devolvido do empréstimo')
        else:
            print('Esse livro não pode ser devolvido porque já está disponível')

    def exibir(self):
        print('Título: ' + self.getTitulo() + '\nAutor: ' + self.getAutorPrincipal() + '\nEditora: ' + self.getEditora(), '\nEstado: ', self.getEstado() )
        print('Ano: ', self.getAno(), '\nISBN: ', self.getIsbn(), '\nQuantidade de empréstimos: ', self.getQuantidadeEmprestimos())
print('-------LIVRO-------\n\n')
livro= Livro()
livro.setTitulo('Harry Potter e a Camara Secreta')
livro.setAutorPrincipal('JK')
livro.setAno(2006)
livro.setIsbn(2222)
livro.setEditora('Rocco')
livro.setEstado(True)
livro.emprestar()
livro.devolver()
livro.exibir()
class Revista:
    def __init__(self):
        self.titulo=''
        self.ano=0
        self. editora=''
        self.issn=0

    def setTitulo(self, titulo):
        self.titulo = titulo
    def getTitulo(self):
        return self.titulo
    def setAno(self, ano):
        self.ano=ano
    def getAno(self):
        return self.ano
    def setEditora(self, editora):
        self.editora=editora
    def getEditora(self):
        return self.editora
    def setIssn(self, issn):
        self.issn=issn
    def getIss(self):
        return self.issn

    def exibirRevista(self):
        ano = 2024 - self.ano
        if ano <= 5:
            print('Título: '+ self.getTitulo()+'\nEditora: '+self.getEditora() +'\nAno: ' , self.getAno(),'\nIssn: ', self.getIss())
        else:
            print('Os dados dessa revista não podem ser exibidos')
print('\n\n-------REVISTA-------\n\n')
revista = Revista()
revista.setTitulo('Titulo exemplo da revista')
revista.setAno(2018)
revista.setEditora('Vogue')
revista.setIssn(22222)
revista.exibirRevista()
class Pessoa:
    def __init__(self):
        self.nome=''
        self.telefone=0
        self.email=''


    def setNome(self, nome):
        self.nome=nome
    def getNome(self):
        return self.nome
    def setTelefone(self, telefone):
        self.telefone=telefone
    def getTelefone(self):
        return self.telefone
    def setEmail(self, email):
        self.email=email
    def getEmail(self):
        return self.email

    def exibirDados(self):
        print('Nome: ' + self.getNome(), '\nTelefone: ', self.getTelefone(), '\nEmail: ', self.getEmail())
print('\n\n-------PESSOA-------\n\n')
pessoa = Pessoa()
pessoa.setNome('Heloisa Cabral')
pessoa.setTelefone(992886775)
pessoa.setEmail('heloisacabralco@gmail.com')
pessoa.exibirDados()
print('\n\n-------BIBLIOTECARIO-------\n\n')
class Bibliotecario(Pessoa):
    def __init__(self):
        super().__init__()
        self.matricula=0
        self.tempo_de_servico=0
        self.salario=0

    def setMatricula(self, matricula):
        self.matricula=matricula
    def getMatricula(self):
        return self.matricula
    def setTempoServico(self, tempo_de_servico):
        self.tempo_de_servico=tempo_de_servico
    def getTempoServico(self):
        return self.tempo_de_servico
    def setSalario(self, salario):
        self.salario=salario
    def getSalario(self):
        return self.salario

    def calcularSalario(self):
        calculo_salario = 2000 + (200 * self.tempo_de_servico)
        self.salario = calculo_salario
        print(self.salario)
    def exibirDadosBibliotecario(self):
        self.exibirDados()
        print('Matricula: ', self.getMatricula() , '\nTempo de serviço: ', self.getTempoServico(), '\nSalário Calculado: ' , self.salario)
biblitecario = Bibliotecario()
biblitecario.setNome('Heloisa Cabral')
biblitecario.setEmail('heloisacabralco@gmail.com')
biblitecario.setMatricula(202311029)
biblitecario.setTempoServico(2)
biblitecario.setTelefone(992886775)
biblitecario.calcularSalario()
biblitecario.exibirDadosBibliotecario()
class Leitor(Pessoa):
    def __init__(self):
        super().__init__()
        self.endereco= ''
        self.idade = 0

    def setEndereco(self):
        logradouro = input('Logradouro: ')
        numero = int(input('Número: '))
        complemento = input('Complemento: ')
        bairro = input('Bairro: ')
        cidade = input('Cidade: ')
        estado = input('Estado: ')
        cep = int(input('CEP: '))
        endereco = logradouro, numero, complemento, bairro, cidade, estado, cep
        self.endereco = endereco
    def getEndereco(self):
        return self.endereco

    def setIdade(self, idade):
        self.idade = idade
    def getIdade(self):
        return self.idade

    def validaIdade(self):
        if self.idade < 18:
            print('Voce não é maior de idade, voce nao pode fazer empréstimo de livros')
        else:
            print('Os empréstimos estão liberados')

    def diminuirIdade(self):
        if self.idade <= 0:
            print('Voce nao pode diminuir 1 ano da idade zero')
        else:
            self.idade -= 1
    def aumentarIdade(self):
            self.idade += 1

    def exibirDadosLeitor(self):
        self.exibirDados()
        print('Endereço: ', self.endereco ,'\nIdade: ', self.idade )
print('\n\n-------LEITOR-------\n')
leitor = Leitor()
leitor.setNome('Heloisa Cabral')
leitor.setIdade(18)
leitor.setEmail('heloisacabralco@gmail.com')
leitor.setEndereco()
leitor.setTelefone(24002886775)
leitor.aumentarIdade()
leitor.diminuirIdade()
leitor.validaIdade()
leitor.exibirDadosLeitor()








