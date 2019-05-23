# -*- coding: utf-8 -*-
import autoit
import os
import time
import Variaveis
import log
import SENHAFUNC
import Tecla
import Tempo

def AltW(Desc):
    log.EscreverLog('Função AltW no produto')
    Tempo.TeclaAcao()
    autoit.send("{ALTDOWN}w{ALTUP}")
    try:
        Variaveis.Tempo = (2)
        log.EscreverLog('Tempo. ate ' + str(Variaveis.Tempo) + ' segundos')
        autoit.win_wait_active("[Class:TFRM_ALTW]", Variaveis.Tempo)
        log.EscreverLog('Aplicar desconto de ' + str(Desc) +'%')
        Tempo.Dig()
        autoit.send(Desc)
        Tecla.Enter()
        SENHAFUNC.SENHAFUNC()
    except:
        log.EscreverLog('Não abriu a tela AltW')
        Tecla.Enter()
    for x in range(0,4):
        Tecla.Enter()
    log.EscreverLog('Sai Função AltW no produto')