# -*- coding: utf-8 -*-
import autoit
import os
import time
import Variaveis
import log

import Produto

def VendaAltw():
    log.EscreverLog('Entra funcao Venda AltW')
    time.sleep(Variaveis.TEnter)
    log.EscreverLog('Tela Venda')
    log.EscreverLog('Clicar na Grid')
    autoit.control_click("[CLASS:TFRM_VENDAS]", "TVSMDBGrid3")
    log.EscreverLog("Entra loop Produtos")
    for Arry in Variaveis.AProdutoAltw:
        Produto.Produto(Arry[0],Arry[1],Arry[2],Arry[3])
        log.EscreverLog('Loop')
    log.EscreverLog("Sai loop Produtos")
    log.EscreverLog('Sai funcao Venda AltW')