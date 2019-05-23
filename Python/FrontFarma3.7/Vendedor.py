# -*- coding: utf-8 -*-
import autoit
import Variaveis
import log
from DAO import FuncoesBD
import Tecla
import Tempo

def Vendedor(Doc,Tipo) :
    #if(autoit.win_wait("[CLASS:TFRM_FINALVENDA]"))==1:
    Variaveis.Retorno = 0
    while Variaveis.Retorno  == 0:
        Variaveis.Retorno = autoit.control_focus("[CLASS:TFRM_FINALVENDA]", "TRzDBButtonEdit1")
        Tempo.Loop()
        Tecla.LimpaTexto()

    #Tempo.Dig()
    log.EscreverLog('Função Vendedor')
    if Variaveis.CodVendedor == '0':
        sSql =  'SELECT  ' \
                'V.CODVEND ' \
                'FROM myouro.VENDEDORES V ' \
                'WHERE V.SITUACAO ="A" AND ' \
                '( V.BLOQUEARVENDA_EMOUTRALOJA = "N" ' \
                'OR V.CODLOJA =' + str(Variaveis.CodLoja) + ')' \
                'ORDER BY RAND() LIMIT 0,1'

        log.EscreverLog('Executando Sql:' + str(sSql))

        Resultado = FuncoesBD.ComDBSlave.Select(sSql)
        if Resultado.__len__() > 0:
            Result = Resultado[0]
            Variaveis.CodVendedor = str(Result[0])
    Tempo.ClickFinalVenda()

    autoit.control_click("[CLASS:TFRM_FINALVENDA]", "TRzDBButtonEdit1")

    Tecla.LimpaTexto()
    Tempo.TeclaAcao()
    log.EscreverLog('Vendedor :' + str(Variaveis.CodVendedor))
    autoit.send(str(Variaveis.CodVendedor))
    Tecla.Enter()


    if Doc == "ORC":
        Tempo.TelaAcao()
        autoit.win_wait_active("[Class:TFRM_SENHAFUNC]", Variaveis.Tempo)

        log.EscreverLog('Senha Libera Orcamento')
        autoit.control_send("[CLASS:TFRM_SENHAFUNC]", "TRzButtonEdit1", Variaveis.SenhaAdmin)
        Tempo.Dig()
        Tecla.Enter()
    Tempo.TempoR()
    log.EscreverLog('Sai Função Vendedor')