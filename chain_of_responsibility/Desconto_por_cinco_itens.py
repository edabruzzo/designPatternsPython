class Desconto_por_cinco_itens(object):

    def calcula(self, orcamento):

        if orcamento.quantidade_itens() > 5:
            return orcamento.valor * 0.1
        else:
            return 0


class Desconto_por_valor(object):

    def calcula(self, orcamento):

        if orcamento.valor > 500:
            return orcamento.valor * 0.07
        else:
            return 0