# -*- coding: utf-8 -*-
import autoit
import os
import time
import Variaveis
import log
import Tecla
import Tela
import Tempo
def SENHAFUNC():
    try:
        log.EscreverLog('Entra Função SenhaFunc')
        try:
            Variaveis.Tempo = (0.25)
            log.EscreverLog('Tempo. ate ' + str(Variaveis.Tempo) + ' segundos')
            autoit.win_wait_active("[Class:TFRM_SENHAFUNC]", Variaveis.Tempo)
            Tela.Alerta('Acima do limite', 'Desconto aceito')
            log.EscreverLog('Pede Senha')
            Tempo.Dig()
            autoit.control_set_text("[Class:TFRM_SENHAFUNC]", "TRzButtonEdit1", Variaveis.SenhaAdmin)
            log.EscreverLog('Passa Senha')
            Tecla.Enter()
            log.EscreverLog('Senha Ok')
        except:
            Tecla.Enter()
            Variaveis.Tempo = (0.25)
            log.EscreverLog('Tempo. ate ' + str(Variaveis.Tempo) + ' segundos')
            autoit.win_wait_active("[Class:TFRM_SENHAFUNC]", Variaveis.Tempo)
            log.EscreverLog('Pede Senha')
            Tecla.TempoR()
            autoit.control_set_text("[Class:TFRM_SENHAFUNC]", "TRzButtonEdit1", Variaveis.SenhaAdmin)
            log.EscreverLog('Passa Senha')
            Tecla.Enter()
            log.EscreverLog('Senha Ok')
    except:
        log.EscreverLog('Sem Senha')
    log.EscreverLog('Sai Função SenhaFunc')