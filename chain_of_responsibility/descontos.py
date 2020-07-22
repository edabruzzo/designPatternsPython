class Desconto_por_cinco_itens(object):

    def __init__(self, proximo_desconto):
        self.__proximo_desconto = proximo_desconto

    def calcula(self, orcamento):

        if orcamento.quantidade_itens() > 5:
            print('Aplicando desconto por mais de 5 itens')
            return orcamento.valor * 0.1
        else:
            return self.__proximo_desconto.calcula(orcamento)


class Desconto_por_valor(object):

    def __init__(self, proximo_desconto):
        self.__proximo_desconto = proximo_desconto

    def calcula(self, orcamento):

        if orcamento.valor > 500:
            print('Aplicando desconto por valor superior a 500')
            return orcamento.valor * 0.07
        else:
            return self.__proximo_desconto.calcula(orcamento)


class Sem_desconto_Fim_Cadeia(object):

  def calcula(self, orcamento):
    return 0
