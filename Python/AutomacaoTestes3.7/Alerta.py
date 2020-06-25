# -*- coding: utf-8 -*-
import autoit
import os
import time
import Variaveis
import log

import Tempo
import Tecla



def TelaAlertaCrt(t,e):
    try:
        Variaveis.Tempo = (5)
        autoit.win_wait_active("[Class:TFRM_VSMTASKDIALOG]", Variaveis.Tempo)
        Tempo.Click()
        log.EscreverLog(str(t))
        autoit.control_click("[Class:TFRM_VSMTASKDIALOG]", "TVSMColorButton1")
        log.EscreverLog('Clicou Ok')
    except:
        log.EscreverLog(str(e))
    Tecla.Enter()



def TelaAlerta(t,e):
    try:
        Variaveis.Tempo = (5)
        autoit.win_wait_active("[Class:TFRM_VSMTASKDIALOG]", Variaveis.Tempo)
        Tempo.Click()
        log.EscreverLog(str(t))
        autoit.control_click("[Class:TFRM_VSMTASKDIALOG]", "TVSMColorButton1")
        log.EscreverLog('Clicou Ok')
    except:
        log.EscreverLog(str(e))
    Tempo.TeclaAcao()
