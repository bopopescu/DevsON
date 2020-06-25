# -*- coding: utf-8 -*-
import autoit
import os
import time
import Variaveis
import log

import SENHAEMPBLOQ
import SENHACLIBLOQ
import SENHALIMITECREDITO
import Tecla
import Tempo



def Cliente(Tipo,Cod):
    log.EscreverLog('Função Cliente ')
    #Tempo.TempoL()
    #if(autoit.win_wait("[CLASS:TFRM_FINALVENDA]"))==1:
    Variaveis.Retorno = 0
    while Variaveis.Retorno == 0:
        Variaveis.Retorno = autoit.control_focus("[CLASS:TFRM_FINALVENDA]", "TRzDBButtonEdit6")
        Tempo.Loop()
    #else:
    #    Tempo.TempoL()
    try:
        #Tempo.TempoL()
        autoit.control_send("[CLASS:TFRM_FINALVENDA]", "TRzDBButtonEdit6", str(Cod))
        Tempo.Dig()
        log.EscreverLog('Passamdo codigo do Cliente:' + str(Cod))
        for x in range(0,2):
            Tecla.Enter()
        if Tipo == "TP" or Tipo =="TC":
            if Tipo == "P":
                SENHACLIBLOQ.SENHACLIBLOQ()
            if Tipo =="C":
                time.sleep(Variaveis.TConvenio)
                SENHAEMPBLOQ.SENHAEMPBLOQ()
                SENHACLIBLOQ.SENHACLIBLOQ()
                SENHALIMITECREDITO.SENHALIMITECREDITO()
    except:
        log.EscreverLog('Erro Função Cliente')

    log.EscreverLog('Sai Função Cliente')
