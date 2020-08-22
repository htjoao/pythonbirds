class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=28) -> object:
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)
    def cumprimentar(self):
        return f'olá {id(self)}'
    @staticmethod
    def metodo_statico():
        return 42
    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos{cls.olhos}'
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
    luciano.sobrenome = 'ramalho'
    luciano.olhos = 1
    del luciano.olhos
    Pessoa.olhos = 3
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