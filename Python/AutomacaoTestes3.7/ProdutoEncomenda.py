    # -*- coding: utf-8 -*-
import autoit
import os
import time
import Variaveis
import log

import SENHAFUNC
import TemPromocao
import AltW
import MarcarPosVenda
import InformarLote
import InformarPsico



def Produto(Prod,Desc,Qtd,Antecipado):
    log.EscreverLog('Função lança produto')
    log.EscreverLog(Prod)
    time.sleep(Variaveis.TDig)
    log.EscreverLog('Lança produto')
    autoit.send(Prod)
    time.sleep(Variaveis.TEnter)
    log.EscreverLog('ENTER')
    autoit.send("{ENTER}")
    TemPromocao.TemPromocao()
    time.sleep(Variaveis.TDig)
    try:
        autoit.send("{ALTDOWN}{F6}{ALTUP}")
        log.EscreverLog('Abrindo tela lançar encomenda')
        autoit.win_wait_active("[Class:TFRM_INCLUIRENCOMENDAS]", Variaveis.TTela)

        if Antecipado == 'S':
            log.EscreverLog('Pagamento Antecipado')
            autoit.control_click("[Class:TFRM_INCLUIRENCOMENDAS]", 'TRzGroupButton1')
        else:
            log.EscreverLog('Pagamento Normal')
            autoit.control_click("[Class:TFRM_INCLUIRENCOMENDAS]", 'TRzNumericEdit3',)
        time.sleep(Variaveis.TEnter)
        autoit.send("{ENTER}")
        log.EscreverLog('ENTER')
        time.sleep(Variaveis.TEnter)
        autoit.send("{ENTER}")
        log.EscreverLog('ENTER')
        time.sleep(Variaveis.TDig)
        autoit.send('0')
        log.EscreverLog('0')
        time.sleep(Variaveis.TEnter)
        autoit.send("{ENTER}")
        log.EscreverLog('ENTER')
        time.sleep(Variaveis.TDig)
        autoit.send(Qtd)
        log.EscreverLog(Qtd)
        time.sleep(Variaveis.TEnter)
        autoit.send("{ENTER}")
        log.EscreverLog('ENTER')
        time.sleep(Variaveis.TEnter)
        autoit.send("{ENTER}")
        log.EscreverLog('ENTER')
        time.sleep(Variaveis.TEnter)
        autoit.send("{ENTER}")
        log.EscreverLog('ENTER')
        time.sleep(Variaveis.TEnter)
        log.EscreverLog('Confirma Encomenda')
        time.sleep(Variaveis.TEnter)
    except:
        log.EscreverLog('Error')

    if Desc != "0":
        AltW.AltW(Desc)
        time.sleep(Variaveis.TEnter)
        autoit.send("{ENTER}")
        log.EscreverLog('ENTER')
        time.sleep(Variaveis.TEnter)
        autoit.send("{ENTER}")
        log.EscreverLog('ENTER')
        time.sleep(Variaveis.TEnter)
    else:
        time.sleep(Variaveis.TEnter)
        autoit.send("{ENTER}")
        log.EscreverLog('ENTER')
    time.sleep(Variaveis.TEnter)
    autoit.send("{DOWN}")
    time.sleep(Variaveis.TEnter)
    log.EscreverLog('Seta pra baixo')
    log.EscreverLog('Sai função lança produto')
