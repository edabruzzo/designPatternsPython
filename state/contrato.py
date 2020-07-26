
from state.estado_contrato import Em_Aprovacao

class Contrato(object):


   def __init__(self, valor, Estado):
       self.__valor = valor
       self.__estado_atual = Estado
       self.__descontoAplicado = False


   @property
   def descontoAplicado(self):
       return self.__descontoAplicado

   @descontoAplicado.setter
   def descontoAplicado(self, descontoAplicado):
       self.__descontoAplicado = descontoAplicado

   @property
   def valor(self):
       return self.__valor


   @valor.setter
   def valor(self, valor):
        self.__valor = valor

   @property
   def estadoAtual(self):
       return self.__estado_atual


   @estadoAtual.setter
   def estadoAtual(self, Estado):
       self.__estado_atual = Estado