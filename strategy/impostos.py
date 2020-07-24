
from abc import ABCMeta, abstractmethod


class Imposto(object):
    __metaclass__ = ABCMeta

    def __init__(self, outro_imposto = None):
        self.__outro_imposto = outro_imposto

    @abstractmethod
    def calcular(self, orcamento):
        pass

# Ué, uma classe abstrata que herda de outra classe abstrata ?
class Template_de_imposto_condicional(Imposto):

    __metaclass__ = ABCMeta

    def calcular(self, orcamento):
        if self.deve_usar_maxima_taxacao(orcamento):
            return self.maxima_taxacao(orcamento)
        else:
            return self.minima_taxacao(orcamento)

    @abstractmethod
    def deve_usar_maxima_taxacao(self, orcamento): pass

    @abstractmethod
    def maxima_taxacao(self, orcamento): pass

    @abstractmethod
    def minima_taxacao(self, orcamento): pass



class ISS(Imposto):

    #https://stackoverflow.com/questions/23944657/typeerror-method-takes-1-positional-argument-but-2-were-given
    def calcular(self, orcamento):
        return orcamento.valor * 0.1


class ICMS(Imposto):

    #https://stackoverflow.com/questions/23944657/typeerror-method-takes-1-positional-argument-but-2-were-given
    def calcular(self, orcamento):
        return orcamento.valor * 0.06



class ICPP(Template_de_imposto_condicional):

    def deve_usar_maxima_taxacao(self, orcamento):
        if orcamento.valor > 500 :
            return True

    def maxima_taxacao(self, orcamento):
        return orcamento.valor * 0.1

    def minima_taxacao(self, orcamento):
        return orcamento.valor * 0.06




class IKCV(Template_de_imposto_condicional):

    def deve_usar_maxima_taxacao(self, orcamento):
        if orcamento.valor > 500 and self.__tem_item_maior_que_100_reais(orcamento):
            return True

    def maxima_taxacao(self, orcamento):
        return orcamento.valor * 0.07

    def minima_taxacao(self, orcamento):
        return orcamento.valor * 0.05


    def __tem_item_maior_que_100_reais(self, orcamento):
        for item in orcamento.obter_itens():
            return item.valor > 100
        return False