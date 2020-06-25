# -*- coding: utf-8 -*-
import Variaveis
import log
from DAO import Config

#Conexao DB
from DAO.ConexaoMySql import conexaoMySql

log.EscreverLog('Passou pela conexão com o Central')

#ComDBMaster = conexaoMySql('172.20.90.14', 'root', 'drogaria', 'myouro', '3306')

ComDBMaster = ''
#Conexão Master Luiz
ComDBMaster1 = conexaoMySql(Config.BDIpMLuiz, Config.BDUserM, Config.BDSenhaMLuiz, Config.BDO, Config.BDPortaM)
#Conexão Master Wagner
ComDBMaster2 = conexaoMySql(Config.BDIpMWG, Config.BDUserM, Config.BDSenhaMWG, Config.BDO, Config.BDPortaM)
#Conexão Master Wellinton
ComDBMaster3 = conexaoMySql(Config.BDIpMWell, Config.BDUserM, Config.BDSenhaMWell, Config.BDO, Config.BDPortaM)
#Conexão Master Sandra
ComDBMaster4 = conexaoMySql(Config.BDIPMSandra, Config.BDUserM, Config.BDSenhaMSandra, Config.BDO, Config.BDPortaMSandra)

#ComDBMaster = conexaoMySql(Config.BDIpM, Config.BDUserM, Config.BDSenhaM, Config.BDO, Config.BDPortaM)

log.EscreverLog('Passou pela conexão com o Slave')
#ComDBSlave = conexaoMySql('172.20.90.8', 'root', 'drogaria', 'myfront', '3306')

ComDBSlave=''
#Conexão Slave Luiz
ComDBSlave1 = conexaoMySql(Config.BDIpSLuiz, Config.BDUserS, Config.BDSenhaSLuiz, Config.BDF, Config.BDPortaS)
#Conexão Slave Wagner
ComDBSlave2 = conexaoMySql(Config.BDIpSWG, Config.BDUserS, Config.BDSenhaSWG, Config.BDF, Config.BDPortaS)
#Conexão Slave Well
ComDBSlave3 = conexaoMySql(Config.BDIpSWell, Config.BDUserS, Config.BDSenhaSWell, Config.BDF, Config.BDPortaS)
#Conexão Slave Sandra
ComDBSlave4 = conexaoMySql(Config.BDIPMSandra, Config.BDUserS, Config.BDSenhaMSandra, Config.BDF, Config.BDPortaSSandra)


ComDBSlaveMyouro=''
#Conexão Slave Luiz
ComDBSlaveMyouro1 = conexaoMySql(Config.BDIpSLuiz, Config.BDUserS, Config.BDSenhaSLuiz, Config.BDO, Config.BDPortaS)
#Conexão Slave Wagner
ComDBSlaveMyouro2 = conexaoMySql(Config.BDIpSWG, Config.BDUserS, Config.BDSenhaSWG, Config.BDO, Config.BDPortaS)
#Conexão Slave Well
ComDBSlaveMyouro3 = conexaoMySql(Config.BDIpSWell, Config.BDUserS, Config.BDSenhaSWell, Config.BDO, Config.BDPortaS)
#Conexão Slave Sandra
ComDBSlaveMyouro4 = conexaoMySql(Config.BDIPMSandra, Config.BDUserS, Config.BDSenhaMSandra, Config.BDO, Config.BDPortaSSandra)

def LocalizaCupom(Num):
    log.EscreverLog('Entra Função Localiza Cupom')
    log.EscreverLog(str(Variaveis.LocCupom) + str(Num))
    Resultado = ComDBSlave.Select(str(Variaveis.LocCupom) + str(Num))

    if Resultado.__len__() > 0:
        Result = Resultado[0]
        Variaveis.NCupom = str(Result[0])
        Variaveis.NCodCli= str(Result[1])
        Variaveis.Retorna = 'S'
    else:
        Variaveis.Retorna='N'
    log.EscreverLog('Sai Função Localiza Cupom')



def LocalizaPrevenda(Num):

    if Num > 0:
        Variaveis.LocPrevenda = str(Variaveis.sLocPrevendaN) + str(Num)
    if Num == 0:
        Variaveis.LocPrevenda = Variaveis.sLocPrevenda


    log.EscreverLog('Entra Função Localiza Prevenda')
    log.EscreverLog(str(Variaveis.LocPrevenda))
    Resultado = ComDBSlave.Select(str(Variaveis.LocPrevenda))

    if Resultado.__len__() > 0:
        Result = Resultado[0]
        Variaveis.NroPrevenda = str(Result[1])
        Variaveis.Recebe    = str(Result[2])
        Variaveis.Retorna = 'S'
    else:
        Variaveis.Retorna='N'
    log.EscreverLog('Sai Função Localiza Prevenda')


def LocalizaEntrega(Num):
    if Num > 0:
        Variaveis.LocEntrega = str(Variaveis.sLocEntregaN) + str(Num)
    if Num == 0:
        Variaveis.LocEntrega = str(Variaveis.sLocEntrega)
    log.EscreverLog('Entra Função Localiza Entrega')
    Resultado = ComDBMaster.Select(str(Variaveis.LocEntrega))

    log.EscreverLog(str(Variaveis.LocEntrega))

    if Resultado.__len__() > 0:
        Result = Resultado[0]
        Variaveis.NroPrevenda = str(Result[2])
        Variaveis.NCupom    = str(Result[5])
        Variaveis.Troco     = str(Result[11])
        Variaveis.Recebe    = str(Result[12])
        Variaveis.Retorna   = 'S'
    else:
        Variaveis.Retorna='N'
    log.EscreverLog('Sai Função Localiza Entrega')


def SqlMaster(sSql):
    ComDBMaster.Execute(sSql)

def SqlSlave(sSql):
    ComDBSlave.Execute(sSql)


def PreparaConfig():
    ComDBMaster.Execute(Variaveis.PrepConfig)