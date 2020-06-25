# -*- coding: utf-8 -*-
# import Principal

import Variaveis
import log

# Conexao DB
from DAO.ConexaoMySql import conexaoMySql


def LocalizaPrevenda(Num):
    log.EscreverLog('Conectando ao Central')
    ComDBMaster = conexaoMySql('172.20.90.14', 'root', 'emluwe', 'myouro', '3306')
    log.EscreverLog('Conectando ao Slave')
    ComDBSlave = conexaoMySql('172.20.90.8', 'root', 'emluwe', 'myfront', '3306')

    log.EscreverLog(str(Variaveis.LocPrevenda))
    Resultado = ComDBSlave.Select(str(Variaveis.LocPrevenda))

    if Resultado.__len__() > 0:
        Result = Resultado[Num]
        Variaveis.NroPrevenda = str(Result[1])
        Variaveis.Recebe    = str(Result[2])

