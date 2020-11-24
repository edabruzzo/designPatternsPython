# -*- coding: utf-8 -*-
import MySQLdb

'''
No Builder, ainda estamos no controle da criação do objeto, porém com o auxílio 
do Builder e podemos construir um objetos de diferentes maneiras. 
Já o Factory, não participamos do processo de criação do objeto, isto é, 
já recebemos o objeto pronto!

'''



class Connection_factory(object):

    def get_connection(self):
        # tratamento de erro omitido
        return MySQLdb.connect(host="localhost",
            user='root',
            passwd='',
            db='alura')