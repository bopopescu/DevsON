# -*- coding: utf-8 -*-
import autoit
import os
import time
import Variaveis
import log

def DadosEntrega():
    log.EscreverLog('Timer ' + str(Variaveis.TTela))
    time.sleep(Variaveis.TTela)

    log.EscreverLog('Função Dados de entrega')
    log.EscreverLog("Alt e")
    autoit.send("{ALTDOWN}e{ALTUP}")
    log.EscreverLog('Timer ' + str(Variaveis.TDig))
    time.sleep(Variaveis.TDig)


    log.EscreverLog("Tempo.tela de Dados Entrega")
    log.EscreverLog('Timer ' + str(Variaveis.TTela))
    autoit.win_wait_active("[Class:TFRM_DADOSENTREGA]", Variaveis.TTela)
    log.EscreverLog("Telefone")
    autoit.send("0000000000")
    log.EscreverLog('Timer ' + str(Variaveis.TDig))
    time.sleep(Variaveis.TDig)
    autoit.send("{ENTER}")
    log.EscreverLog('Timer ' + str(Variaveis.TEnter))
    time.sleep(Variaveis.TEnter)

    log.EscreverLog("Endereço")
    autoit.send("AQUI TESTE ENTREGA, 6666")
    log.EscreverLog('Timer ' + str(Variaveis.TDig))
    time.sleep(Variaveis.TDig)
    autoit.send("{ENTER}")
    log.EscreverLog('Timer ' + str(Variaveis.TEnter))
    time.sleep(Variaveis.TEnter)

    log.EscreverLog("Bairro")
    autoit.send("Centro")
    log.EscreverLog('Timer ' + str(Variaveis.TDig))
    time.sleep(Variaveis.TDig)
    autoit.send("{ENTER}")
    log.EscreverLog('Timer ' + str(Variaveis.TEnter))
    time.sleep(Variaveis.TEnter)

    log.EscreverLog("Cidade")


    if Variaveis.DocFiscal == "NFCE":
        autoit.send("P")
        log.EscreverLog('Timer ' + str(Variaveis.TDig))
        time.sleep(Variaveis.TDig)

    else:
        autoit.send("A")
        log.EscreverLog('Timer ' + str(Variaveis.TDig))
        time.sleep(Variaveis.TDig)

    log.EscreverLog('Timer ' + str(Variaveis.TTela))
    autoit.win_wait_active("[Class:TFRM_LOCALIZAR]", Variaveis.TTela)

    if Variaveis.DocFiscal == "NFCE":
        autoit.send("EDRA PRETA")
        log.EscreverLog('Timer ' + str(Variaveis.TDig))
        time.sleep(Variaveis.TDig)
    else:
        autoit.send("SSIS")
        log.EscreverLog('Timer ' + str(Variaveis.TDig))
        time.sleep(Variaveis.TDig)

    autoit.send("{ENTER}")
    log.EscreverLog('Timer ' + str(Variaveis.TEnter))
    time.sleep(Variaveis.TEnter)


    autoit.send("{ENTER}")
    log.EscreverLog('Timer ' + str(Variaveis.TEnter))
    time.sleep(Variaveis.TEnter)


    autoit.send("{ENTER}")
    log.EscreverLog('Timer ' + str(Variaveis.TEnter))
    time.sleep(Variaveis.TEnter)


    log.EscreverLog("Cep")
    autoit.send("19645000")
    log.EscreverLog('Timer ' + str(Variaveis.TDig))
    time.sleep(Variaveis.TDig)
    autoit.send("{ENTER}")
    log.EscreverLog('Timer ' + str(Variaveis.TEnter))
    time.sleep(Variaveis.TEnter)

    autoit.send("{ENTER}")
    log.EscreverLog('Timer ' + str(Variaveis.TEnter))
    time.sleep(Variaveis.TEnter)

    autoit.send("{ENTER}")
    log.EscreverLog('Timer ' + str(Variaveis.TEnter))
    time.sleep(Variaveis.TEnter)

    autoit.send("{ENTER}")
    log.EscreverLog('Timer ' + str(Variaveis.TEnter))
    time.sleep(Variaveis.TEnter)

    log.EscreverLog("Entregar para")
    autoit.send("TESTE ENTREGA")
    log.EscreverLog('Timer ' + str(Variaveis.TDig))
    time.sleep(Variaveis.TDig)

    autoit.send("{ENTER}")
    log.EscreverLog('Timer ' + str(Variaveis.TEnter))
    time.sleep(Variaveis.TEnter)

    autoit.send("{ENTER}")
    log.EscreverLog('Timer ' + str(Variaveis.TEnter))
    time.sleep(Variaveis.TEnter)

    autoit.send("{ENTER}")
    log.EscreverLog('Timer ' + str(Variaveis.TEnter))
    time.sleep(Variaveis.TEnter)

    autoit.send("{ENTER}")
    log.EscreverLog('Timer ' + str(Variaveis.TEnter))
    time.sleep(Variaveis.TEnter)

    log.EscreverLog('Sai Função Dados de entrega')