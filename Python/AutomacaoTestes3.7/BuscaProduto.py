# -*- coding: utf-8 -*-
from random import choice
import Variaveis
import log
import Tempo
from DAO import FuncoesBD


def BuscaProduto():
    sSql = "SELECT P.CODPROD  FROM MYOURO.PRODUTOS P " \
           "INNER JOIN MYOURO.STOCK S ON S.CODPROD = P.CODPROD  AND S.CODLOJA =  %s " \
           "WHERE " \
           "P.SITUACAO ='A' " \
           "AND P.TIPOPROD = 'R' " \
           "AND P.PORTARIAPROD ='' " \
           "AND P.PRECOVENDA BETWEEN 50 AND 1000 " \
           "AND S.CONTROLALOTE ='N'  " \
           "AND P.DIAS_POSVENDA = 0  " \
           "AND P.TIPO ='*' AND " \
           "P.NBM NOT IN('30044090','30045099','30039090') " \
           "ORDER BY RAND() LIMIT 0,1 " % (Variaveis.CodLoja)
    Tempo.Sql()
    log.EscreverLog('Executando Sql:' + str(sSql))
    Resultado = FuncoesBD.ComDBSlave.Select(sSql)
    if Resultado.__len__() > 0:
        Result = Resultado[0]
        Variaveis.CodProd = str(Result[0])
    log.EscreverLog('Fim da execução da Sql')

    ApDesc = choice(['0','1','2','3','4','5'])
    Variaveis.AtwDesc = str(ApDesc)




