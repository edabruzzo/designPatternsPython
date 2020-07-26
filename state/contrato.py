
from state.estado_contrato import Em_Aprovacao

class Contrato(object):

   def __init__(self, valor, Estado):
       self.__valor = valor
       self.__estado_atual = Estado


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