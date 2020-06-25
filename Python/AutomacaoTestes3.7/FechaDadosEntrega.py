# -*- coding: utf-8 -*-
import autoit
import os
import time
import Variaveis
import log



def FechaDadosEntrega():
    log.EscreverLog('Função Fecha Dados Entrega')
    log.EscreverLog("Entregador")
    autoit.control_click("[Class:TFRM_DADOSENTREGA]", "TRzButtonPair2")
    log.EscreverLog('Timer ' + str(Variaveis.TEnter))
    time.sleep(Variaveis.TEnter)

    log.EscreverLog("{ENTER}")
    autoit.send("{ENTER}")
    log.EscreverLog('Timer ' + str(Variaveis.TEnter))
    time.sleep(Variaveis.TEnter)

    log.EscreverLog("{ENTER}")
    autoit.send("{ENTER}")
    log.EscreverLog('Timer ' + str(Variaveis.TEnter))
    time.sleep(Variaveis.TEnter)

    log.EscreverLog("Finalizar Entrega")
    autoit.control_click("[Class:TFRM_DADOSENTREGA]", "TRzBmpButton1")
    log.EscreverLog('Timer ' + str(Variaveis.TEnter))
    time.sleep(Variaveis.TEnter)

    log.EscreverLog('Sai Função Fecha Dados Entrega')
