# -*- coding: utf-8 -*-
import autoit
import log
import Tecla
import Tempo

import os
import time
import Variaveis

def Documento(Doc):
    log.EscreverLog('Entra Função Doc')
    for x in range(0,3):
        Tecla.Esc()

    Tempo.Click()

    log.EscreverLog('Clicar Combo Operação')
    autoit.control_click("[Class:TFRM_VENDAS]", "TRzComboBox2")

    Tempo.Dig()

    if Doc == "PREV":
        autoit.control_send("[Class:TFRM_VENDAS]", "Edit2", "Pré-Venda")
        Tecla.Enter()
        log.EscreverLog('Pre-Venda Habilitado')

    if Doc == "ORC":
        autoit.control_send("[Class:TFRM_VENDAS]", "Edit2", 'Orçamento')
        Tecla.Enter()
        log.EscreverLog('Orcamento Habilitado')

    if Doc == "NFCE":
        autoit.control_send("[Class:TFRM_VENDAS]", "Edit2", "NFC Eletrônica")
        Tecla.Enter()
        log.EscreverLog('NFC Eletrônica')

    if Doc == "ECF":
        autoit.control_send("[Class:TFRM_VENDAS]", "Edit2", "Cupom Fiscal")
        Tecla.Enter()
        log.EscreverLog('Cupom Fiscal')

    if Doc == "SAT":
        autoit.control_send("[Class:TFRM_VENDAS]", "Edit2", "Sat")
        Tecla.Enter()
        log.EscreverLog('Sat')

    if Doc == "MOD2":
        autoit.control_send("[Class:TFRM_VENDAS]", "Edit2", "NF Modelo 2")
        Tecla.Enter()
        log.EscreverLog('NF Modelo 2')

    if Doc == "NFE":
        autoit.control_send("[Class:TFRM_VENDAS]", "Edit2", "NF Eletrônica")
        Tecla.Enter()
        log.EscreverLog('NF Eletrônica')

    log.EscreverLog('SAI FUNÇAO DOC')