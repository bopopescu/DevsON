# -*- coding: utf-8 -*-
import autoit
import os
import time
import Variaveis
import log
import SENHAFUNC
import Tecla


def Desconto(Desc,Arred):
    log.EscreverLog('Função Desconto')
    Tecla.TempoR()
    autoit.control_click("[Class:TFRM_FINALVENDA]", "TRzNumericEdit4")
    Tecla.TempoR()
    log.EscreverLog('Desconto de: ' + str(Desc) + '%')
    autoit.control_set_text("[Class:TFRM_FINALVENDA]", "TRzNumericEdit4", Desc)

    Tecla.Enter()

    SENHAFUNC.SENHAFUNC()

    autoit.control_click("[Class:TFRM_FINALVENDA]", "TRzNumericEdit3")
    Tecla.TempoR()
    log.EscreverLog('Arredondamento de: ' +str(Arred) + 'R$')
    autoit.control_set_text("[Class:TFRM_FINALVENDA]", "TRzNumericEdit3", Arred)

    Tecla.Enter()
    try:
        log.EscreverLog('Alerta de Arredondamento')
        autoit.win_wait_active("[Class:TFRM_VSMTASKDIALOG]", Variaveis.TTela)
        Tecla.TempoR()
        autoit.control_click("[Class:TFRM_VSMTASKDIALOG]", "TRzBitBtn1")
        Tecla.TempoR()
        log.EscreverLog('Botão ok')
        log.EscreverLog('Clicou ok')
    except:
        log.EscreverLog('Não teve alerta de Arredondamento')