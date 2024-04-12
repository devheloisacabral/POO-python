# Classes: Produto, Livro, Eletrônico
# Produto: nome, preço, método para aplicar desconto
# Livro: autor, método para aplicar desconto (5% adicional)
# Eletrônico: garantia, método para aplicar desconto (10% adicional)


class Produto:
    def __init__(self):
        self.nome = ''
        self.preco = 0

    def setNome(self, nome):
        self.nome = nome
    def setPreco(self, preco):
        self.preco = preco
    def getNome(self):
        return self.nome
    def getPreco(self):
        return self.preco

    def aplica_desconto(self, desconto):
        self.preco -= (desconto/100) * self.preco

class Livro(Produto):
    def __init__(self):
        super().__init__()
        self.autor = ''

    def setAutor(self, autor):
        self.autor = autor
    def getAutor(self):
        return self.autor

    def descontoAdicional(self, desconto):
        self.preco -= (5 / 100) * self.preco
        super().aplica_desconto(desconto)

class Eletronico(Produto):
    def __init__(self):
        super().__init__()
        self.garantia = ''

    def setGarantia(self,garantia):
        self.garantia = garantia
    def getGarantia(self):
        return self.garantia

    def descontoGarantia(self, desconto):
        super().aplica_desconto(desconto)
        self.preco -= (10/100) * self.preco

