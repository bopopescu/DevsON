# -*- coding: utf-8 -*-
import autoit
import os
import time

import log
import Tempo
import Tela

def Crtx():
    log.EscreverLog('Entra Funçao Crt X')
    Tempo.TeclaAcao()
    log.EscreverLog('Crt X')
    autoit.send("{CTRLDOWN}x{CTRLUP}")
    Tela.TelaAlertaCrt('Tela Vazia','Sem Alerta')
    Tempo.TeclaAcao()
    log.EscreverLog('Sai Funçao Crt X')