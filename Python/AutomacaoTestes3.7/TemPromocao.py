# -*- coding: utf-8 -*-
import autoit
import os
import time
import Variaveis
import log

# -*- coding: utf-8 -*-
import autoit
import os
import time
import Variaveis
import log
import Tecla

def TemPromocao():
    log.EscreverLog('Entra Funçao Tem Promoçao')
    try:
        log.EscreverLog('Valida se o produto tem promoção')
        Variaveis.Tempo = (Variaveis.TempoAdd + 0.15)
        log.EscreverLog('Tempo. ate ' + str(Variaveis.Tempo) + ' segundos')
        autoit.win_wait_active("[Class:TFRM_TIPOPROMOCAO]", Variaveis.Tempo)
        log.EscreverLog('Confirma promoção')
        Tecla.Enter()
    except:
        log.EscreverLog('Produto sem promoção')
    log.EscreverLog('Sai Funçao Tem Promoçao')


