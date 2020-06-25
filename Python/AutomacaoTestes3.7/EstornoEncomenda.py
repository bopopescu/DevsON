# -*- coding: utf-8 -*-
import autoit
import os
import time
import Variaveis
import log
import SENHAFUNC

def Estorno(Tipo):
    log.EscreverLog("Alt + S")
    autoit.send("{ALTDOWN}s{ALTUP}")
    log.EscreverLog('Timer ' + str(Variaveis.TDig))
    time.sleep(Variaveis.TDig)

    SENHAFUNC.SENHAFUNC()
    try:
        log.EscreverLog('Entra Função Estorno Encomenda')

        log.EscreverLog("PGUP")
        autoit.send("{PGUP}")
        log.EscreverLog('Timer ' + str(Variaveis.TEnterL))
        time.sleep(Variaveis.TEnterL)

        log.EscreverLog("DEL")
        autoit.send("{DEL}")
        log.EscreverLog('Timer ' + str(Variaveis.TDig))
        time.sleep(Variaveis.TDig)

        SENHAFUNC.SENHAFUNC()

        if Tipo == 'C':
            log.EscreverLog("F6")
            autoit.send("{F6}")
        if Tipo == 'D':
            log.EscreverLog("F7")
            autoit.send("{F7}")

        log.EscreverLog('Timer ' + str(Variaveis.TDig))
        time.sleep(Variaveis.TDig)

        log.EscreverLog('Timer ' + str(Variaveis.TTela))
        autoit.win_wait_active("[Class:TFRM_CONFIRMAVALETROCA]", Variaveis.TTela)

        log.EscreverLog("{SPACE}")
        autoit.send("{SPACE}")
        log.EscreverLog('Timer ' + str(Variaveis.TDig))
        time.sleep(Variaveis.TDig)

        SENHAFUNC.SENHAFUNC()

    except:
        log.EscreverLog('Erro')

    log.EscreverLog("{ESC}")
    autoit.send("{ESC}")
    log.EscreverLog('Timer ' + str(Variaveis.TDig))
    time.sleep(Variaveis.TDig)

    log.EscreverLog('Sai Função Estorno encomenda')

