# -*- coding: utf-8 -*-
import autoit
import os
import time
import Variaveis
import log
import Tecla
def SENHALIMITECREDITO():
    try:
        log.EscreverLog('Valida se o cliente tem limite')
        log.EscreverLog('Tempo. : ' + str(Variaveis.TAlertaM) + 'segundos')
        autoit.win_wait_active("[Class:TFRM_SENHALIMITECREDITO]", Variaveis.TTela)
        Tecla.TempoR()
        log.EscreverLog('Pede Senha')
        autoit.control_send("[Class:TFRM_SENHALIMITECREDITO]", "TRzButtonEdit1", Variaveis.SenhaAdmin)
        log.EscreverLog('Passa Senha')
        Tecla.Enter()
        log.EscreverLog('Senha Ok')
    except:
        log.EscreverLog('Cliente com limite disponivel')
