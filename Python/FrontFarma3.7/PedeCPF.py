# -*- coding: utf-8 -*-
import autoit
import Variaveis
import log
from DAO import FuncoesBD
import Tecla
import Tempo

def PedeCPF():
    sSql = "SELECT COALESCE(CF.STATUS,'S') " \
           "FROM myouro.LOJAS L " \
           "INNER JOIN myouro.CIDADES C ON C.CODCID = L.CODCID " \
           "LEFT JOIN myouro.CONFIGURACAO CF ON CF.CHAVE = CONCAT(C.UFCID,'_PEDECPF') " \
           "WHERE L.CODLOJA  = %s " % (Variaveis.CodLoja)

    log.EscreverLog('Executando Sql:' + str(sSql))
    Resultado = FuncoesBD.ComDBSlave.Select(str(sSql))


    if Resultado.__len__() > 0:
        Result = Resultado[0]
        Variaveis.PedeCpf = str(Result[0])

    if Variaveis.PedeCpf =='S':
        log.EscreverLog("Função Pede CPF")
        try:
            Tempo.TeclaAcao()
            autoit.win_wait_active("[Class:TFRM_VENDACPF]", Variaveis.Tempo)
            log.EscreverLog("Pede CPF")
            autoit.control_click("[Class:TFRM_VENDACPF]", "TVSMColorButton3")
            log.EscreverLog("Fecha Pede CPF")
        except:
            log.EscreverLog('Não pediu CPF')
    if Variaveis.PedeCpf == 'N':
        log.EscreverLog('Não pediu CPF')
        Tecla.TempoM()