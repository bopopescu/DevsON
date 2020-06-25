# -*- coding: utf-8 -*-
import autoit
import os
import time
import Variaveis
import log


def MostraDesconto():
    log.EscreverLog('Função Mostra desconto')
    log.EscreverLog('{ALT D - Mostra descontos aplicados')
    time.sleep(Variaveis.TDig)
    autoit.send("{ALTDOWN}d{ALTUP}")
    time.sleep(Variaveis.TTela)
    log.EscreverLog('{Fecha tela de descontos aplicados')
    time.sleep(Variaveis.TDig)
    autoit.send("{ESC}")