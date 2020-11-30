# -*- coding: utf-8 -*-

from datetime import date

class Pedido(object):

    def __init__(self, cliente, valor):
        self.__cliente = cliente
        self.__valor = valor
        self.__status = 'NOVO'
        self.__data_finalizacao = None


    def paga(self):
        self.__status = 'PAGO'

    def finaliza(self):
        self.__data_finalizacao = date.today()
        self.__status = 'ENTREGUE'

    @property
    def cliente(self):
        return self.__cliente

    @property
    def valor(self):
        return self.__valor

    @property
    def status(self):
        return self.__status

    @property
    def data_finalizacao(self):
        return self.__data_finalizacao



class Fila_Trabalho(object):

    def __init__(self):
        self.__comandos = []

    def adiciona(self, comando):
        self.__comandos.append(comando)

    def processa(self):
        for comando in self.__comandos:
            comando.executa()



from abc import ABCMeta, abstractmethod


class Comando(object):

    __metaclass__ = ABCMeta

    @abstractmethod
    def executa(self):
        pass


class Conclui_Pedido(Comando):

     def __init__(self, pedido):
         self.__pedido = pedido


     def executa(self):
         self.__pedido.finaliza()



class Paga_Pedido(Comando):

    def __init__(self, pedido):
        self.__pedido = pedido

    def executa(self):
        self.__pedido.paga()



if __name__ == '__main__':

    pedido1 = Pedido('A', 10)
    pedido2 = Pedido('B', 20)

    fila = Fila_Trabalho()
    fila.adiciona(Paga_Pedido(pedido1))
    fila.adiciona(Paga_Pedido(pedido2))
    fila.adiciona(Conclui_Pedido(pedido2))
    fila.adiciona(Conclui_Pedido(pedido1))

    fila.processa()