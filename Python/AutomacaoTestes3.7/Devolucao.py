# -*- coding: utf-8 -*-
import autoit
import os
import time
import Variaveis
import log
import SENHAFUNC

def Devolucao(Num,Seq):
    autoit.send("{F9}")
    try:
        log.EscreverLog('Devolução de Venda')
        autoit.win_wait_active("[Class:TFRM_LISTAVENDASDEVOL]", Variaveis.TTela)
        autoit.control_send("[CLASS:TFRM_LISTAVENDASDEVOL]", "TRzNumericEdit1",Num)
        time.sleep(Variaveis.TDig)
        autoit.send("{F5}")
        time.sleep(Variaveis.TDig)
        autoit.send("{F11}")
        time.sleep(Variaveis.TDig)
        autoit.send("{F10}")
        time.sleep(Variaveis.TDig)
        try:
            log.EscreverLog('Confirma Devolução de Venda')
            autoit.win_wait_active("[Class:TFRM_CONFIRMADEVOL]", Variaveis.TTela)
            autoit.control_click("[CLASS:TFRM_LISTAVENDASDEVOL]", "TVSMDBGrid1")
            time.sleep(Variaveis.TDig)
            autoit.send("{RIGHT}")
            log.EscreverLog('Seta para Direita')
            time.sleep(Variaveis.TDig)
            autoit.send("{SPACE}")
            log.EscreverLog('Barra de espaço')
            time.sleep(Variaveis.TDig)
            autoit.send("{DOWN}")
            log.EscreverLog('Seta para Baixo')

            if Seq == 1 :
                time.sleep(Variaveis.TDig)
                autoit.send("{DOWN}")
                log.EscreverLog('Seta para Baixo')

                time.sleep(Variaveis.TDig)
            autoit.send("{ENTER}")
            log.EscreverLog('{ENTER}')
            time.sleep(Variaveis.TDig)
            autoit.send("{F10}")
            log.EscreverLog('{F10}')
            time.sleep(Variaveis.TDig)
            SENHAFUNC.SENHAFUNC()
            time.sleep(Variaveis.TDig)
            autoit.send("{ENTER}")
            log.EscreverLog('{ENTER}')
            time.sleep(Variaveis.TDig)
            autoit.send("{F8}")
            log.EscreverLog('{F8}')
            time.sleep(Variaveis.TDig)
            autoit.send("{F8}")
            log.EscreverLog('{F8}')
            time.sleep(Variaveis.TDig)
            SENHAFUNC.SENHAFUNC()
            time.sleep(Variaveis.TDig)
            if Seq == 0:
                try:
                    log.EscreverLog('Gerar Vale Troca')
                    autoit.win_wait_active("[Class:TFRM_CONFIRMAVALETROCA]", Variaveis.TTela)
                    autoit.control_click("[Class:TFRM_CONFIRMAVALETROCA]", "TRzBitBtn1")
                    log.EscreverLog('Clicou Ok')
                    time.sleep(Variaveis.TEnter)
                except:
                    log.EscreverLog('Fecha tela')
            else:
                try:
                    log.EscreverLog('Devolver Dinheiro')
                    autoit.win_wait_active("[Class:TFRM_VSMTASKDIALOG]", Variaveis.TTela)
                    autoit.control_click("[Class:TFRM_VSMTASKDIALOG]", "TRzBitBtn1")
                    log.EscreverLog('Clicou Ok')
                    time.sleep(Variaveis.TEnter)
                except:
                    log.EscreverLog('Fecha tela')

        except:
            log.EscreverLog('Erro')

    except:
        log.EscreverLog('Erro')
    log.EscreverLog('Sai Função Devolução')
