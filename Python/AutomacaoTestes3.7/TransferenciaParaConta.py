# -*- coding: utf-8 -*-
import autoit
import os
import time
import Variaveis
import log
import SENHAFUNC
import RecebeDinheiro

def TransferenciaParaConta(Tipo,Valor):
    log.EscreverLog('Entrada Função Transferencia Para Conta')
    log.EscreverLog("{ALTDOWN}L{ALTUP}")
    autoit.send("{ALTDOWN}l{ALTUP}")
    log.EscreverLog('Timer ' + str(Variaveis.TTela))
    time.sleep(Variaveis.TTela)

    SENHAFUNC.SENHAFUNC()

    log.EscreverLog('Timer ' + str(Variaveis.TTela))
    autoit.win_wait_active("[Class:TFRM_LANCCAIXAMENU]", Variaveis.TTela)

    log.EscreverLog("{ALTDOWN}R{ALTUP}")
    autoit.send("{ALTDOWN}r{ALTUP}")
    log.EscreverLog('Timer ' + str(Variaveis.TDig))
    time.sleep(Variaveis.TDig)

    log.EscreverLog('Timer ' + str(Variaveis.TTela) + ' Tela TFRM_RETIRADATRANSF')
    autoit.win_wait_active("[Class:TFRM_RETIRADATRANSF]", Variaveis.TTela)

    autoit.control_click("[Class:TFRM_RETIRADATRANSF]",'TRzGroupButton1')
    log.EscreverLog('Timer ' + str(Variaveis.TEnterR) + ' Click')
    time.sleep(Variaveis.TEnterR)

    log.EscreverLog("{ENTER}")
    autoit.send("{ENTER}")
    log.EscreverLog('Timer ' + str(Variaveis.TEnterR))
    time.sleep(Variaveis.TEnterR)

    log.EscreverLog("Valor")
    autoit.send(str(Valor))
    log.EscreverLog('Timer ' + str(Variaveis.TDig))
    time.sleep(Variaveis.TDig)

    log.EscreverLog("{ENTER}")
    autoit.send("{ENTER}")
    log.EscreverLog('Timer ' + str(Variaveis.TEnter))
    time.sleep(Variaveis.TEnter)

    log.EscreverLog("Selecionar Tipo")
    autoit.control_click("[Class:TFRM_RETIRADATRANSF]", "Edit1")
    log.EscreverLog('Timer ' + str(Variaveis.TEnterR))
    time.sleep(Variaveis.TEnterR)

    if Tipo == "CX":
        log.EscreverLog('CC')
        log.EscreverLog('Timer ' + str(Variaveis.TEnterR))
        time.sleep(Variaveis.TEnterR)
        autoit.send("{DOWN}")


    if Tipo == "CC":
        log.EscreverLog('CC')
        log.EscreverLog('Timer ' + str(Variaveis.TEnterR))
        time.sleep(Variaveis.TEnterR)
        autoit.send("{DOWN}")
        log.EscreverLog('Timer ' + str(Variaveis.TEnterR))
        time.sleep(Variaveis.TEnterR)
        autoit.send("{DOWN}")

        #autoit.control_send("[Class:TFRM_RETIRADATRANSF]", "Edit1", "Conta")

    log.EscreverLog('Timer ' + str(Variaveis.TEnterR))
    time.sleep(Variaveis.TEnterR)

    log.EscreverLog("{ENTER}")
    autoit.send("{ENTER}")
    log.EscreverLog('Timer ' + str(Variaveis.TEnterR))
    time.sleep(Variaveis.TEnterR)

    if Tipo == "CX":
        log.EscreverLog("Caixa Destino :" + str(Variaveis.CaixaDestino))
        autoit.send(str(Variaveis.CaixaDestino))
        log.EscreverLog('Timer ' + str(Variaveis.TEnterR))
        time.sleep(Variaveis.TEnterR)

    if Tipo == "CC":
        log.EscreverLog("CodLoja :" + str(Variaveis.CodLoja))
        autoit.send(str(Variaveis.CodLoja))
        log.EscreverLog('Timer ' + str(Variaveis.TEnterR))
        time.sleep(Variaveis.TEnterR)

        log.EscreverLog("{ENTER}")
        autoit.send("{ENTER}")
        log.EscreverLog('Timer ' + str(Variaveis.TEnterR))
        time.sleep(Variaveis.TEnterR)

        autoit.send("{HOME}{SHIFTDOWN}{END}{SHIFTUP}{BACKSPACE}")


        log.EscreverLog("Conta :" + str(Variaveis.ContaBanco))
        autoit.send(str(Variaveis.ContaBanco))
        log.EscreverLog('Timer ' + str(Variaveis.TEnterR))
        time.sleep(Variaveis.TEnterR
                   )

    log.EscreverLog("{ENTER}")
    autoit.send("{ENTER}")
    log.EscreverLog('Timer ' + str(Variaveis.TEnterR))
    time.sleep(Variaveis.TEnterR)

    log.EscreverLog("{ENTER}")
    autoit.send("{ENTER}")
    log.EscreverLog('Timer ' + str(Variaveis.TEnterR))
    time.sleep(Variaveis.TEnterR)

    log.EscreverLog("{ESC}")
    autoit.send("{ESC}")
    log.EscreverLog('Timer ' + str(Variaveis.TEnter))
    time.sleep(Variaveis.TEnter)


    log.EscreverLog("{ESC}")
    autoit.send("{ESC}")
    log.EscreverLog('Timer ' + str(Variaveis.TEnter))
    time.sleep(Variaveis.TEnter)

    log.EscreverLog('Sai Função Lançamento de Despesas')