# -*- coding: utf-8 -*-
import autoit
import os
import time
import Variaveis
import log



def Entrega():
    log.EscreverLog('Função Dados de entrega')
    log.EscreverLog("Alt e")
    autoit.send("{ALTDOWN}e{ALTUP}")
    log.EscreverLog('Timer ' + str(Variaveis.TDig))
    time.sleep(Variaveis.TDig)


    log.EscreverLog("Tempo.tela de Dados Entrega")
    log.EscreverLog('Timer ' + str(Variaveis.TTela))
    autoit.win_wait_active("[Class:TFRM_DADOSENTREGA]", Variaveis.TTela)

    autoit.control_click("[Class:TFRM_DADOSENTREGA]", "TRzDBNumericEdit4")
    log.EscreverLog('Timer ' + str(Variaveis.TEnter))
    time.sleep(Variaveis.TEnter)
    log.EscreverLog('Sai Função Dados de entrega')