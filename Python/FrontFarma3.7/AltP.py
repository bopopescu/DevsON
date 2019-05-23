# -*- coding: utf-8 -*-

import autoit
import time
import Variaveis
import log
from DAO import FuncoesBD
import SENHAFUNC
import RecebeDinheiro

def AltP(Num):
    log.EscreverLog('Entra Função de Recebimento')
    log.EscreverLog("{ALTDOWN}p{ALTUP}")
    autoit.send("{ALTDOWN}p{ALTUP}")
    log.EscreverLog('Timer ' + str(Variaveis.TDig))
    time.sleep(Variaveis.TDig)

    SENHAFUNC.SENHAFUNC()

    log.EscreverLog('Timer ' + str(Variaveis.TTela))
    autoit.win_wait_active("[Class:TFRM_RECEBIMENTO]", Variaveis.TTela)
    FuncoesBD.LocalizaCupom(Num)
    if Variaveis.Retorna == 'S':
        sCupom = Variaveis.NCupom
        sCli = Variaveis.NCodCli
    else:
        sCupom = 0

    if sCupom == 0:
        log.EscreverLog("{ESC}")
        autoit.send("{ESC}")
        log.EscreverLog('Timer ' + str(Variaveis.TDig))
        time.sleep(Variaveis.TEnterL)
        log.EscreverLog("Cupom Não encontrado")
    else:
        log.EscreverLog('Codigo Cliente :' + str(sCli))
        autoit.send(sCli)
        log.EscreverLog('Timer ' + str(Variaveis.TDig))
        time.sleep(Variaveis.TDig)

        log.EscreverLog("{ENTER}")
        autoit.send("{ENTER}")
        log.EscreverLog('Timer ' + str(Variaveis.TEnterL))
        time.sleep(Variaveis.TEnterL)

        log.EscreverLog("{ALTDOWN}{SPACE}{ALTUP}")
        autoit.send("{ALTDOWN}{SPACE}{ALTUP}")
        log.EscreverLog('Timer ' + str(Variaveis.TDig))
        time.sleep(Variaveis.TDig)

        log.EscreverLog("{F4}")
        autoit.send("{F4}")
        log.EscreverLog('Timer ' + str(Variaveis.TTela))
        time.sleep(Variaveis.TTela)

        log.EscreverLog("Seleciona Cupom")
        autoit.control_send("[Class:TFRM_RECEBIMENTO]",'TRzNumericEdit1',sCupom)
        log.EscreverLog('Timer ' + str(Variaveis.TDig))
        time.sleep(Variaveis.TDig)

        log.EscreverLog("{ENTER}")
        autoit.send("{ENTER}")
        log.EscreverLog('Timer ' + str(Variaveis.TEnter))
        time.sleep(Variaveis.TEnter)


        log.EscreverLog("{ESC}")
        autoit.send("{ESC}")
        log.EscreverLog('Timer ' + str(Variaveis.TDig))
        time.sleep(Variaveis.TEnterL)


        log.EscreverLog("{F10}")
        autoit.send("{F10}")
        log.EscreverLog('Timer ' + str(Variaveis.TDig))
        time.sleep(Variaveis.TDig)

        SENHAFUNC.SENHAFUNC()

        RecebeDinheiro.RecebeDinheiro()

        log.EscreverLog("{ENTER}")
        autoit.send("{ENTER}")
        log.EscreverLog('Timer ' + str(Variaveis.TEnterL))
        time.sleep(Variaveis.TEnterL)

        log.EscreverLog("{ESC}")
        autoit.send("{ESC}")
        log.EscreverLog('Timer ' + str(Variaveis.TDig))
        time.sleep(Variaveis.TDig)

    log.EscreverLog('Saida Função de Recebimento')