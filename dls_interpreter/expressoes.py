class Soma(object):

    def __init__(self, expressao_esquerda, expressao_direita):
        self.__expressao_esquerda = expressao_esquerda
        self.__expressao_direita = expressao_direita

    def avalia(self):
        return (self.__expressao_esquerda.avalia() + self.__expressao_direita.avalia())


class Subtracao(object):

    def __init__(self, expressao_esquerda, expressao_direita):
        self.__expressao_esquerda = expressao_esquerda
        self.__expressao_direita = expressao_direita

    def avalia(self):
        return (self.__expressao_esquerda.avalia() - self.__expressao_direita.avalia())


class Numero(object):

    def __init__(self, numero):
        self.__numero = numero

    def avalia(self):
        return self.__numero


if __name__ == '__main__':

    expressao_esquerda = Soma(Numero(10), Numero(5))
    expressao_direita = Subtracao(Numero(2), Numero(1))


    #  ((10+5)+(2-1)) = 16
    resultado = Soma(expressao_esquerda, expressao_direita).avalia()
    print(resultado)

