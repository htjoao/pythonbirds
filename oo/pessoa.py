class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=28) -> object:
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)
    def cumprimentar(self):
        return f'olá meu nome e {self.nome}'
    @staticmethod
    def metodo_statico():
        return 42
    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos{cls.olhos}'

class Homem(Pessoa):
    def cumprimentar(self):
        cumprimentar_da_classe = super().cumprimentar()
        return f'{cumprimentar_da_classe}.apertar a mão'


class Mutante(Pessoa):
    olhos = 3


if __name__ == '__main__':
    joão = Mutante(nome='joão')
    luciano = Homem(joão, nome='luciano')
    print(Pessoa.cumprimentar(luciano))
    print(id(luciano))
    print(luciano.cumprimentar())
    print(luciano.nome)
    print(luciano.idade)
    for filho in luciano.filhos:
        print(filho.nome)
    luciano.sobrenome = 'ramalho'
    luciano.olhos = 1
    del luciano.olhos
    del luciano.filhos
    print(luciano.sobrenome)
    print(luciano.__dict__)
    print(joão.__dict__)
    print(Pessoa.olhos)
    print(luciano.olhos)
    print(joão.olhos)
    print(id (Pessoa.olhos),id(luciano.olhos), id(joão.olhos))
    print(Pessoa.metodo_statico(), luciano.metodo_statico(), joão.metodo_statico())
    print(Pessoa.nome_e_atributos_de_classe(),joão.nome_e_atributos_de_classe(), luciano.nome_e_atributos_de_classe())
    pessoa = Pessoa('Anonimo')
    print(isinstance(pessoa, Pessoa))
    print(isinstance(Homem, Pessoa))
    print(isinstance(joão, Pessoa))
    print(isinstance(joão, Homem))
    print(joão.olhos)
    print(luciano.cumprimentar())
    print(joão.cumprimentar())