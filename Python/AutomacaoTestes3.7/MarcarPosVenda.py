# -*- coding: utf-8 -*-
import autoit
import os
import time
import Variaveis
import log


def MarcarPosVenda():
    time.sleep(Variaveis.TEnter)
    log.EscreverLog('Pos Venda')
    autoit.send("{CTRLDOWN}p{CTRLUP}")
    time.sleep(Variaveis.TDig)
    autoit.win_wait_active("[Class:TFRM_DADOSPOSVENDA]", Variaveis.TTelaL)
    time.sleep(Variaveis.TEnter)
    autoit.control_send("[Class:TFRM_DADOSPOSVENDA]", "TRzDBSpinEdit1", "30")
    time.sleep(Variaveis.TDig)
    time.sleep(Variaveis.TEnter)
    autoit.control_send("[Class:TFRM_DADOSPOSVENDA]", "TRzDBSpinEdit2", "1")
    time.sleep(Variaveis.TDig)
    time.sleep(Variaveis.TEnter)
    autoit.control_click("[Class:TFRM_DADOSPOSVENDA]", "TRzBitBtn2")
    time.sleep(Variaveis.TEnter)
    autoit.send("{ENTER}")
    time.sleep(Variaveis.TEnter)
