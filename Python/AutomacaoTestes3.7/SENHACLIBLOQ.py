# -*- coding: utf-8 -*-
import autoit
import os
import time
import Variaveis
import log
import Tecla
import Tempo


def SENHACLIBLOQ():
    try:
        log.EscreverLog('Valida se cliente esta bloqueado')
        Variaveis.Tempo = 0.50
        log.EscreverLog('Timer ' + str( Variaveis.Tempo))
        autoit.win_wait_active("[Class:TFRM_SENHACLIBLOQ]", Variaveis.Tempo)
        log.EscreverLog('Pede Senha')
        Tempo.Dig()
        autoit.control_send("[Class:TFRM_SENHACLIBLOQ]", "TRzButtonEdit1", Variaveis.SenhaAdmin)
        log.EscreverLog('Passa Senha')
        Tecla.Enter()
        log.EscreverLog('Senha Ok')
    except:
        log.EscreverLog('Não esta bloqueado')