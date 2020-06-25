# -*- coding: utf-8 -*-
import autoit
import os
import time
import Variaveis
import log



def PgtoAntecipado():
    time.sleep(Variaveis.TEnter)
    log.EscreverLog('Função Pgto Antecipado')
    log.EscreverLog("Entregador")
    autoit.control_click("[Class:TFRM_DADOSENTREGA]", "TVSMGroupButton7")
    time.sleep(Variaveis.TEnter)
    autoit.control_click("[Class:TFRM_DADOSENTREGA]", "TVSMGroupButton1")
    time.sleep(Variaveis.TEnter)
    log.EscreverLog('Sai Pgto Antecipado')
