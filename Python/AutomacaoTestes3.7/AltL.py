# -*- coding: utf-8 -*-
import autoit
import os
import time
import Variaveis
import log
import SENHAFUNC
import RecebeDinheiro

def AltL(Es,Valor):
    log.EscreverLog('Entra Função Lançamento de Despesas')
    log.EscreverLog("{ALTDOWN}L{ALTUP}")
    autoit.send("{ALTDOWN}l{ALTUP}")
    log.EscreverLog('Timer ' + str(Variaveis.TDig))
    time.sleep(Variaveis.TDig)

    SENHAFUNC.SENHAFUNC()

    log.EscreverLog('Timer ' + str(Variaveis.TTela))
    autoit.win_wait_active("[Class:TFRM_LANCCAIXAMENU]", Variaveis.TTela)

    log.EscreverLog("{ALTDOWN}L{ALTUP}")
    autoit.send("{ALTDOWN}l{ALTUP}")
    log.EscreverLog('Timer ' + str(Variaveis.TDig))
    time.sleep(Variaveis.TDig)

    log.EscreverLog('Timer ' + str(Variaveis.TTela))
    autoit.win_wait_active("[Class:TFRM_LANCCAIXA]", Variaveis.TTela)

    if Es == 'E':
        log.EscreverLog("Informar Despesa: " + str(Variaveis.CodDespE))
        autoit.control_send("[Class:TFRM_LANCCAIXA]", 'TRzButtonEdit1', str(Variaveis.CodDespE))
        log.EscreverLog('Timer ' + str(Variaveis.TDig))
        time.sleep(Variaveis.TDig)

    if Es == 'S':
        log.EscreverLog("Informar Despesa")
        autoit.control_send("[Class:TFRM_LANCCAIXA]", 'TRzButtonEdit1', str(Variaveis.CodDespS))
        log.EscreverLog('Timer ' + str(Variaveis.TDig))
        time.sleep(Variaveis.TDig)

    log.EscreverLog("{ENTER}")
    autoit.send("{ENTER}")
    log.EscreverLog('Timer ' + str(Variaveis.TEnter))
    time.sleep(Variaveis.TEnter)

    log.EscreverLog("Valor :" + str(Valor))
    autoit.control_set_text("[Class:TFRM_LANCCAIXA]",'TRzNumericEdit1',str(Valor))
    log.EscreverLog('Timer ' + str(Variaveis.TDig))
    time.sleep(Variaveis.TDig)

    log.EscreverLog("{ENTER}")
    autoit.send("{ENTER}")
    log.EscreverLog('Timer ' + str(Variaveis.TEnter))
    time.sleep(Variaveis.TEnter)


    log.EscreverLog("{F6}")
    autoit.send("{F6}")
    log.EscreverLog('Timer ' + str(Variaveis.TEnterR))
    time.sleep(Variaveis.TEnterR)


    log.EscreverLog("{F10}")
    autoit.send("{F10}")
    log.EscreverLog('Timer ' + str(Variaveis.TEnterR))
    time.sleep(Variaveis.TEnterR)



    if Es == 'E':
        log.EscreverLog('Timer ' + str(Variaveis.TTela) + ' Tela TFRM_FORMAPAGTO')
        autoit.win_wait_active("[Class:TFRM_FORMAPAGTO]", Variaveis.TTela)
        log.EscreverLog("{F10}")
        autoit.send("{F10}")
        log.EscreverLog('Timer ' + str(Variaveis.TEnterR))
        time.sleep(Variaveis.TEnterR)


    if Es == 'S':
        log.EscreverLog('Timer ' + str(Variaveis.TTela))
        autoit.win_wait_active("[Class:TFRM_LANCCAIXAPAGTO]", Variaveis.TTela)
        autoit.control_click("[Class:TFRM_LANCCAIXAPAGTO]",'TRzBitBtn1')
        log.EscreverLog('Timer ' + str(Variaveis.TEnterR))
        time.sleep(Variaveis.TEnterR)


    log.EscreverLog("{ESC}")
    autoit.send("{ESC}")
    log.EscreverLog('Timer ' + str(Variaveis.TEnterR))
    time.sleep(Variaveis.TEnterR)


    log.EscreverLog("{ESC}")
    autoit.send("{ESC}")
    log.EscreverLog('Timer ' + str(Variaveis.TEnterR))
    time.sleep(Variaveis.TEnterR)

    log.EscreverLog('Sai Função Lançamento de Despesas')