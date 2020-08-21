class Pessoa:
    def __init__(self, *filhos, nome=None, idade=28) -> object:
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)
    def cumprimentar(self):
        return f'olá {id(self)}'
if __name__ == '__main__':
    joão = Pessoa(nome='joão')
    luciano = Pessoa(joão, nome='luciano')
    print(Pessoa.cumprimentar(luciano))
    print(id(luciano))
    print(luciano.cumprimentar())
    print(luciano.nome)
    print(luciano.idade)
    for filho in luciano.filhos:
        print(filho.nome)