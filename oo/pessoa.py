class Pessoa:
    def cumprimentar(self):
        return f'olá {id(self)}'
if __name__ == '__main__':
    p = Pessoa()
    print(Pessoa.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar())