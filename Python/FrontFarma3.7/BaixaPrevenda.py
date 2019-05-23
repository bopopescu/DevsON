# -*- coding: utf-8 -*-
import autoit
import os
import time
import Variaveis
import log
import F8
import PedeCPF
import RecebeDinheiro
from DAO import FuncoesBD


def BaixaPrevenda(Prev):
    FuncoesBD.LocalizaPrevenda(Prev)
    log.EscreverLog('Entra Função Baixa Prevenda')
    if Variaveis.Retorna == 'S':
        log.EscreverLog('Tempo. : ' + str(Variaveis.TCliIncial) + ' segundos')
        time.sleep(Variaveis.TCliIncial)
        autoit.mouse_click("left", 500, 300, 1)
        autoit.send("{F5}")
        log.EscreverLog("F5")
        log.EscreverLog('Timer ' + str(Variaveis.TDig))
        time.sleep(Variaveis.TDig)
        log.EscreverLog('Existe Prevenda para Baixar')
        try:
            log.EscreverLog('Timer ' + str(Variaveis.TTela))
            autoit.win_wait_active("[Class:TFRM_VSMTASKDIALOG]", Variaveis.TTela)
            log.EscreverLog('Sem Prevenda')
            log.EscreverLog('Timer ' + str(Variaveis.TDig))
            time.sleep(Variaveis.TDig)
            autoit.control_click("[Class:TFRM_VSMTASKDIALOG]", "TRzBitBtn1")
            log.EscreverLog('Timer ' + str(Variaveis.TEnter))
            time.sleep(Variaveis.TEnter)
            log.EscreverLog('Clicou ok')
            log.EscreverLog('Timer ' + str(Variaveis.TEnter))
            time.sleep(Variaveis.TEnter)
        except:
            log.EscreverLog("Tem Prevenda")
            try:
                log.EscreverLog('Abriu F5')
                log.EscreverLog('Timer ' + str(Variaveis.TTela))

                time.sleep(Variaveis.TTela)

                autoit.win_wait_active("[Class:TFRM_PREVENDAS]", Variaveis.TTela)
                log.EscreverLog('Timer ' + str(Variaveis.TDig))
                time.sleep(Variaveis.TDig)

                Variaveis.Query = (
                    '''
                    INSERT IGNORE INTO PYTHONCONFIG
                    (ACAO,DTACAO,NUMPREVENDA,TC,PASSO) SELECT "BAIXAR PREVENDA", NOW(), %s,%s,%s
                    ''' % (int(Variaveis.NroPrevenda), int(Variaveis.Tc), int(Variaveis.Passo)))

                FuncoesBD.SqlSlave(str(Variaveis.Query))

                Texto ='Baixando a Prevenda Nº: ' + str(Variaveis.NroPrevenda)
                if Variaveis.Recebe == "S":
                    Texto = Texto + ' Com Recebimento'
                log.EscreverLog(Texto)
                log.EscreverLog('Timer ' + str(Variaveis.TDig))
                time.sleep(Variaveis.TDig)
                autoit.control_set_text("[Class:TFRM_PREVENDAS]","TRzEdit1", Variaveis.NroPrevenda)
                log.EscreverLog('Timer ' + str(Variaveis.TEnter))
                time.sleep(Variaveis.TEnter)
                log.EscreverLog("Enter")
                autoit.send("{ENTER}")
                log.EscreverLog('Timer ' + str(Variaveis.TEnter))
                time.sleep(Variaveis.TEnter)
                log.EscreverLog("Enter")
                autoit.send("{ENTER}")
                log.EscreverLog('Timer ' + str(Variaveis.TTela))
                autoit.win_wait_active("[Class:TFRM_FINALVENDA]", Variaveis.TTela)
                log.EscreverLog("Esperou Tela Final Venda")
                log.EscreverLog('Chamaou Funcao F8')
                F8.F8()
                log.EscreverLog("Enter")
                autoit.send("{ENTER}")
                log.EscreverLog('Timer ' + str(Variaveis.TEnter))
                time.sleep(Variaveis.TEnter)
                PedeCPF.PedeCPF()
                if Variaveis.Recebe =="S" :
                    RecebeDinheiro.RecebeDinheiro()
            except:
                log.EscreverLog("Error")
                os.system('pause')
    else:
        log.EscreverLog('Não Existe Prevenda para Baixar')

    log.EscreverLog("Sai F5")

