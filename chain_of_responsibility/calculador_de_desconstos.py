from chain_of_responsibility.orcamento import Orcamento, Item


class CalculadorDescontos(object):

    def calculaDesconto(self, orcamento):

        if orcamento.quantidade_itens() > 5:
            desconto = orcamento.valor * 0.10;

        elif orcamento.valor > 500.00:
            desconto = orcamento.valor * 0.07;

        print('Valor do desconto: '+desconto)


if __name__ == 'main':

    item = Item(nome='X', valor=501)
    orcamento = Orcamento()
    orcamento.adicionaItem(item)

    CalculadorDescontos().calculaDesconto(orcamento)    
