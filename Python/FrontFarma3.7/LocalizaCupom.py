# -*- coding: utf-8 -*-
import Variaveis
import log

#Conexao DB
from DAO.ConexaoMySql import conexaoMySql


def LocalizaCupom(Num):
    log.EscreverLog('Conectando ao Central')
    ComDBMaster = conexaoMySql('172.20.90.14', 'root', 'emluwe', 'myouro', '3306')
    log.EscreverLog('Conectando ao Slave')
    ComDBSlave = conexaoMySql('172.20.90.8', 'root', 'emluwe', 'myouro', '3306')

    '''
    Resultado = ComDBMaster.Select(str(Variaveis.CSelect))
    
    if Resultado.__len__() > 0:
        for linha in Resultado:
            Variaveis.cupom = linha[0]
            log.EscreverLog(str(Variaveis.cupom))
    
        log.EscreverLog(str(Resultado[0][0]))
        Variaveis.cupom = str(Resultado[0][0])
    
        log.EscreverLog(str(Variaveis.cupom))
    
        Result = Resultado[0]
        Variaveis.cupom = str(Result[0])
        log.EscreverLog(str(Variaveis.cupom))
    '''

    Variaveis.LocCupom = str(Variaveis.LocCupom) + str(Num)
    Resultado = ComDBMaster.Select(str(Variaveis.LocCupom))
    if Resultado.__len__() > 0:
        Result = Resultado[Num]
        Variaveis.NCupom = str(Result[0])
        #log.EscreverLog(str(Variaveis.cupom))
