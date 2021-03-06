from abc import ABCMeta, abstractmethod

class Estado_Contrato(object):

    __metaclass__ = ABCMeta

    @abstractmethod
    def aprovar(self, contrato):
        pass

    @abstractmethod
    def reprovar(self, contrato):
        pass

    @abstractmethod
    def finalizar(self, contrato):
        pass

    @abstractmethod
    def aplicar_desconto(self, contrato):
        pass


class Em_Aprovacao(Estado_Contrato):

    def aprovar(self, contrato):
        contrato.estadoAtual = Aprovado()

    def reprovar(self, contrato):
        contrato.estadoAtual = Reprovado()

    def finalizar(self, contrato):
        contrato.estadoAtual = Finalizado()

    def aplicar_desconto(self, contrato):
        novo_valor = contrato.valor - contrato.valor * 0.07
        contrato.valor = novo_valor
        contrato.descontoAplicado = True


class Aprovado(Estado_Contrato):

    def aprovar(self, contrato):
        raise RuntimeError('O contrato já está aprovado')

    def reprovar(self, contrato):
        raise RuntimeError('O contrato já está aprovado')

    def finalizar(self, contrato):
        contrato.estadoAtual = Finalizado()

    def aplicar_desconto(self, contrato):
        novo_valor = contrato.valor - contrato.valor * 0.05
        contrato.valor = novo_valor
        contrato.descontoAplicado = True

class Reprovado(Estado_Contrato):

    def aprovar(self, contrato):
        raise RuntimeError('O contrato já está reprovado')

    def reprovar(self, contrato):
        raise RuntimeError('O contrato já está reprovado')

    def finalizar(self, contrato):
        contrato.estadoAtual = Finalizado()

    def aplicar_desconto(self, contrato):
        print('Nenhum desconto será aplicado, pois o contrato está reprovado')


class Finalizado(Estado_Contrato):

    def aprovar(self, contrato):
        raise RuntimeError('O contrato já está finalizado')

    def reprovar(self, contrato):
        raise RuntimeError('O contrato já está finalizado')

    def finalizar(self, contrato):
        raise RuntimeError('O contrato já está finalizado')

    def aplicar_desconto(self, contrato):
        raise RuntimeError('O contrato já está finalizado')