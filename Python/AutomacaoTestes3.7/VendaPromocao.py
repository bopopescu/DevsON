# -*- coding: utf-8 -*-
import autoit
import os
import time
import Variaveis
import log

import Produto


def VendaPromocao():
    log.EscreverLog('Entra funcao VendaPrmocao')
    time.sleep(Variaveis.TEnter)
    log.EscreverLog('Tela Venda')
    log.EscreverLog('Clicar na Grid')
    autoit.control_click("[CLASS:TFRM_VENDAS]", "TVSMDBGrid3")
    log.EscreverLog("Entra loop Produtos")
    for Arry in Variaveis.AProdPromocao:
        Produto.Produto(Arry[0],Arry[1],Arry[2],Arry[3])
        log.EscreverLog('Loop')
    log.EscreverLog("Sai loop Produtos AltW")
    log.EscreverLog('Sai funcao VendaPrmocao')