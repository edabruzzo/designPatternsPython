


class Controla_Contratos(object):

    def aplicar_desconto(self, contrato):
        contrato.estadoAtual.aplicar_desconto(contrato)

    def aprovar(self, contrato):
        contrato.estadoAtual.aprovar(contrato)

    def reprovar(self, contrato):
        contrato.estadoAtual.reprovar(contrato)

    def finalizar(self, contrato):
        contrato.estadoAtual.finalizar(contrato)


from state.estado_contrato import Em_Aprovacao
from state.contrato import Contrato

if __name__ == '__main__':

    contrato = Contrato(100000, Em_Aprovacao())
    controlador = Controla_Contratos()

    controlador.aplicar_desconto(contrato)
    print('Valor do contrato após aplicação de desconto: '+str(contrato.valor))
    #controlador.aprovar(contrato)
    #controlador.reprovar(contrato)
    controlador.finalizar(contrato)

    #Tentando uma operação ilegal de mudança de estado
    #Peço para aprovar um contrato já finalizado (deve lançar erro)
    controlador.aprovar(contrato)

