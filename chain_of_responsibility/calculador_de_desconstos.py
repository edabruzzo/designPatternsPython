from chain_of_responsibility.orcamento import Orcamento, Item


class CalculadorDescontos(object):

    def calculaDesconto(self, orcamento):

        desconto = 0

        if orcamento.quantidade_itens() > 5:
            desconto = orcamento.valor * 0.10

        elif orcamento.valor > 500.00:
            desconto = orcamento.valor * 0.07

        print('Valor do desconto: ' + str(desconto))


if __name__ == '__main__':

    orcamentoA = Orcamento()
    orcamentoA.adicionaItem(Item(nome='X', valor=501))
    orcamentoB = Orcamento()
    orcamentoB.adicionaItem(Item(nome='X', valor=400))
    orcamentoC = Orcamento()
    orcamentoC.adicionaItem(Item('Item A', 100.0))
    orcamentoC.adicionaItem(Item('Item B', 50.0))
    orcamentoC.adicionaItem(Item('Item C', 400.0))
    orcamentoC.adicionaItem(Item('Item D', 100.0))
    orcamentoC.adicionaItem(Item('Item E', 100.0))

    CalculadorDescontos().calculaDesconto(orcamentoA)
    CalculadorDescontos().calculaDesconto(orcamentoB)
    CalculadorDescontos().calculaDesconto(orcamentoC)