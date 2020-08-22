class carro():
    def __init__(self, velocidade=0):
        self.velocidade = velocidade

    def acelerar(self):
        self.acelerar += 1

    def frear(self):
        self.acelerar = 0 if self.velocidade <= 1 else self.velocidade -2

class direcao():
    def __init__(self):
        self.valor='Norte'
    def girar_a_direcao(self):
        direcao = 'Norte'
        if self.valor == 'Oeste':
            self.valor == direcao[0]
        else:
            self.valor = direcao[direcao.index(self.valor) + 1]
    def girar_a_esquerda(self):
        direcao = ('Norte', 'Leste', 'Sul', 'Oeste')
        if self.valor == 'Norte':
            self.valor == direcao[3]
        else:
            self.valor = direcao[direcao.index(self.valor) - 1]
class Carro():
        def __init__(self, direcao, motor):
            self.motor = motor
            self.direcao = direcao

        def calcular_velocidade(self):
            return self.motor.velocidade

        def acelerar(self):
            self.motor.acelerar()

        def frear(self):
            self.motor.frear()

        def calcular_direcao(self):
            return self.direcao.valor

        def girar_a_direita(self):
            self.direcao.girar_a_direita()

        def girar_a_esquerda(self):
            self.direcao.girar_a_esquerda()