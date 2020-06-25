# -*- coding: utf-8 -*-
import autoit
import os
import time
import Variaveis
import log


def InformarLote(Qtd):
    time.sleep(Variaveis.TEnter)
    log.EscreverLog('Informar Lote')
    autoit.send("{CTRLDOWN}l{CTRLUP}")
    time.sleep(Variaveis.TDig)
    autoit.win_wait_active("[Class:TFRM_OBRIGAITENSLOTE]", Variaveis.TTelaL)
    time.sleep(Variaveis.TDig)
    time.sleep(Variaveis.TEnter)
    autoit.control_click("[Class:TFRM_OBRIGAITENSLOTE]", "TVSMColorButton1")
    time.sleep(Variaveis.TEnter)
    log.EscreverLog('Selecionar Lote')
    time.sleep(Variaveis.TDig)
    autoit.win_wait_active("[Class:TFRM_ITENSLOTE]", Variaveis.TTelaL)
    time.sleep(Variaveis.TDig)
    autoit.send(Qtd)
    time.sleep(Variaveis.TEnter)
    autoit.send("{ENTER}")
    time.sleep(Variaveis.TEnter)
    time.sleep(Variaveis.TDig)
    autoit.control_click("[Class:TFRM_ITENSLOTE]", "TVSMColorButton1")
    time.sleep(Variaveis.TEnter)
    time.sleep(Variaveis.TDig)
    autoit.send("{ENTER}")
    time.sleep(Variaveis.TEnter)
    time.sleep(Variaveis.TFinal)
