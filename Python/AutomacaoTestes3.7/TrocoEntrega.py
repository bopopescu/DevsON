# -*- coding: utf-8 -*-
import autoit
import os
import time
import Variaveis
import log

def TrocoEntrega(Troco):
    time.sleep(Variaveis.TEnter)
    log.EscreverLog('Função troco para entrega')
    log.EscreverLog('{ENTER}')
    autoit.send('{ENTER}')
    time.sleep(Variaveis.TEnter)
    log.EscreverLog('Troco para')
    log.EscreverLog(Troco)
    autoit.send(Troco)
    time.sleep(Variaveis.TEnter)
    log.EscreverLog('{ENTER}')
    autoit.send("{ENTER}")
