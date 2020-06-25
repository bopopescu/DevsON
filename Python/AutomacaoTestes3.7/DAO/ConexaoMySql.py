#!/usr/bin/python
# -*- coding: UTF-8 -*-

import datetime
import os
import sys
import getopt

try:
    import mysql.connector
    from mysql.connector import Error
except ImportError:
    urlMySql = 'http://dev.mysql.com/downloads/connector/python/'
    print("Nao foi possivel encontrar o drive de conexao do MySql baixo o mesmo em: %s") % (urlMySql)
    sys.exit(1)


class MysqlPython(object):
    __instance = None
    __host = None
    __user = None
    __password = None
    __database = None
    __session = None
    __connection = None
    __port = None
    __config = None

    def __init__(self, host='localhost', user='root', password='', database='', port=3306):
        self.__host = host
        self.__user = user
        self.__password = password
        self.__database = database
        self.__port = port

    ## End def __init__

    def __open(self):
        try:
            cnx = mysql.connector.connect(host=self.__host, database=self.__database, user=self.__user,
                                          password=self.__password, buffered=True, connect_timeout=20)
            self.__connection = cnx
            self.__session = cnx.cursor()
        except Error as e:
            print("Error %d: %s" % (e.args[0], e.args[1]))

    ## End def __open

    def __close(self):
        self.__session.close()
        self.__connection.close()

    ## End def __close

    def Select(self, sql):
        result = None
        query = sql
        self.__open()
        self.__session.execute(query)
        result = self.__session.fetchall()
        self.__close()
        return result

    ## End def select

    def FetchAllAssoc(self, sql):
        try:
            result = []
            query = sql
            self.__open()
            self.__session.execute(query)
            cols = tuple([field[0] for field in self.__session.description])
            for row in self.__session.fetchall():
                result.append(dict(zip(cols, row)))
        except Exception as e:
            result = {"error": str(e)}
        return result

    def Execute(self, sql):
        query = sql
        self.__open()
        # self.__session.be
        self.__session.execute(query)
        self.__connection.commit()
        self.__close()
        ## End def execute


# Finalidade.: Realizar a conexão com o banco
def conexaoMySql(host, usuario, senha, banco, porta):
    '''
    Descrição: Função responsavel pela conexão com o banco de dados mysql

    Utilização:
    funcao(param1, param2, param3, param4, param5)

    Parâmetros:
    param1 : Host de conexao
    param2 : Usuario
    param3 : senha do banco
    param4 : DB
    param5 : POrta
    '''

    conn = MysqlPython(host, usuario, senha, banco, int(porta))
    return conn


"""
Exemplo de utilização
def main():
    try:
        conexao = conexaoMySql('172.20.90.14','root', 'emluwe', 3306, 'myouro')

        resultado = conexao.FetchAllAssoc('select v.idvenda from venda v order by v.idvenda desc limit 10')

        if resultado.__len__() > 0:
            for linha in resultado:
                idvenda = (linha['idvenda'])
                sSql = 'select * from vendaprodutos where idvenda = %i' % (idvenda)
                resultado2 = conexao.FetchAllAssoc(sSql)
                print (resultado2)



    except:
        print('Erro de conexao')


if __name__ == '__main__':
    main()

"""



