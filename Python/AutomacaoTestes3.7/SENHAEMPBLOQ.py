# -*- coding: utf-8 -*-
import autoit
import os
import time
import Variaveis
import log
import Tecla

def SENHAEMPBLOQ():
    log.EscreverLog("SENHAEMPBLOQ")
    try:
        try:
            log.EscreverLog('Tempo. : ' + str(Variaveis.TTela) + 'segundos')
            autoit.win_wait_active("[Class:TFRM_VSMTASKDIALOG]", Variaveis.TTela)
            log.EscreverLog('Clicar Botão Ok')
            Tecla.TempoR()
            autoit.control_click("[Class:TFRM_VSMTASKDIALOG]", "TRzBitBtn1")
            log.EscreverLog('Clicou Ok')
        except:
            log.EscreverLog('Não teve Alerta')

        try:
            log.EscreverLog('Tempo. : ' + str(Variaveis.TTela) + 'segundos')
            autoit.win_wait_active("[Class:TFRM_SENHAEMPBLOQ]", Variaveis.TTela)
            log.EscreverLog('Valida se a empresa esta bloqueada')
            log.EscreverLog('Pede Senha')
            Tecla.TempoR()
            autoit.control_send("[Class:TFRM_SENHAEMPBLOQ]", "TRzButtonEdit1", Variaveis.SenhaAdmin)
            log.EscreverLog('Passa Senha')
            Tecla.Enter()
        except:
            log.EscreverLog('Não esta Bloqueada')

        for x in range(0,3):
            Tecla.Enter()

    except:
        log.EscreverLog('Não esta bloqueada')