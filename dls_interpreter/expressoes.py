class Soma(object):

    def __init__(self, expressao_esquerda, expressao_direita):
        self.__expressao_esquerda = expressao_esquerda
        self.__expressao_direita = expressao_direita

    @property
    def expressao_esquerda(self):
        return self.__expressao_esquerda

    @property
    def expressao_direita(self):
        return self.__expressao_direita


    def avalia(self):
        return (self.__expressao_esquerda.avalia() + self.__expressao_direita.avalia())

    def aceita(self, visitor):
        visitor.visita_soma(self)


class Subtracao(object):

    def __init__(self, expressao_esquerda, expressao_direita):
        self.__expressao_esquerda = expressao_esquerda
        self.__expressao_direita = expressao_direita

    @property
    def expressao_esquerda(self):
        return self.__expressao_esquerda

    @property
    def expressao_direita(self):
        return self.__expressao_direita

    def avalia(self):
        return (self.__expressao_esquerda.avalia() - self.__expressao_direita.avalia())

    def aceita(self, visitor):
        visitor.visita_subtracao(self)


class Numero(object):

    def __init__(self, numero):
        self.__numero = numero

    @property
    def numero(self):
        return self.__numero

    def avalia(self):
        return self.__numero

    def aceita(self, visitor):
        visitor.visita_numero(self)



class Impressora(object):

    def visita_soma(self, soma):
        print('('+
        str(soma.expressao_esquerda.aceita(self))
        +'+'+
        str(soma.expressao_direita.aceita(self))
        +')')


    def visita_subtracao(self, subtracao):
        print('('+
        str(subtracao.expressao_esquerda.aceita(self))
        +'-'+ str(subtracao.expressao_direita.aceita(self))
        +')')

    def visita_numero(self, numero):
        print(numero.avalia())





class Prefixa_Visitor(object):

    def visita_soma(self, soma):

        print('+')
        print('(')
        print(str(soma.expressao_esquerda.aceita(self)))
        print(str(soma.expressao_direita.aceita(self)))
        print(')')

    def visita_subtracao(self, subtracao):
        print('-')
        print('(')
        print(str(subtracao.expressao_esquerda.aceita(self)))
        print(str(subtracao.expressao_direita.aceita(self)))
        print(')')

    def visita_numero(self, numero):

        print(str(numero.avalia()))









if __name__ == '__main__':

    expressao_esquerda = Soma(Numero(10), Numero(5))
    expressao_direita = Subtracao(Numero(2), Numero(1))


    #  ((10+5)+(2-1)) = 16
    resultado = Soma(expressao_esquerda, expressao_direita)

    visitor = Impressora()
    visitor_preFixa = Prefixa_Visitor()
    resultado.aceita(visitor)
    resultado.aceita(visitor_preFixa)

