# -*- coding: utf-8 -*-
import autoit
import time
import Variaveis
import log

import SENHAFUNC
import RecebeDinheiro
from DAO import FuncoesBD


def Entrega(Prev):
    log.EscreverLog('Entrada Função Entrega')
    FuncoesBD.LocalizaEntrega(Prev)
    if Variaveis.Retorna == 'S':
        autoit.send("{ALTDOWN}b{ALTUP}")
        log.EscreverLog("ALT+B")
        log.EscreverLog('Timer ' + str(Variaveis.TDig))
        time.sleep(Variaveis.TDig)

        try:
            log.EscreverLog('Chama Gerenciador de Entregas')
            log.EscreverLog('Timer ' + str(Variaveis.TTela))
            autoit.win_wait_active("[Class:TFRM_ENTREGASPENDENTES]", Variaveis.TTela)

            log.EscreverLog('Abriu Gerenciador de Entregas')
            log.EscreverLog('Timer ' + str(Variaveis.TDig))
            time.sleep(Variaveis.TDig)

            if Variaveis.Troco == "S":
                Texto ='Registrar saida de Troco para entrega Nº: ' + str(Variaveis.NCupom)
            else:
                Texto = 'Registrar Baixa de entrega Nº: ' + str(Variaveis.NCupom)

            log.EscreverLog(Texto)
            log.EscreverLog('Timer ' + str(Variaveis.TDig))
            time.sleep(Variaveis.TDig)

            log.EscreverLog("Digita numero Cupom: " + str(Variaveis.NCupom))
            autoit.control_set_text("[Class:TFRM_ENTREGASPENDENTES]","TRzEdit6", str(Variaveis.NCupom))
            log.EscreverLog('Timer ' + str(Variaveis.TDig))
            time.sleep(Variaveis.TDig)

            log.EscreverLog("Enter")
            autoit.send("{ENTER}")
            log.EscreverLog('Timer ' + str(Variaveis.TEnterL))
            time.sleep(Variaveis.TEnterL)

            log.EscreverLog("Clicar Botão Pesquisar")
            autoit.control_click("[Class:TFRM_ENTREGASPENDENTES]", "TRzBitBtn4")
            log.EscreverLog('Timer ' + str(Variaveis.TEnterL))
            time.sleep(Variaveis.TEnterL)


            log.EscreverLog("Seta Foco Grid Entrega")
            autoit.control_focus("[Class:TFRM_ENTREGASPENDENTES]", "TVSMDBGrid1")
            log.EscreverLog('Timer ' + str(Variaveis.TEnterL))
            time.sleep(Variaveis.TEnterL)


            log.EscreverLog("Barra de espaço")
            autoit.send("{SPACE}")
            log.EscreverLog('Timer ' + str(Variaveis.TEnterL))
            time.sleep(Variaveis.TEnterL)

            if Variaveis.Troco == "S":
                Texto ='Confirmando saida de Troco para entrega Nº: ' + str(Variaveis.NCupom)
            else:
                Texto ='Confirmando Baixa de entrega Nº: ' + str(Variaveis.NCupom)

            if Variaveis.Troco == "S":
                Variaveis.Texto = 'LANCA TROCO'
            else:
                Variaveis.Texto = 'BAIXA ENTREGA'


            Variaveis.Query = (
                '''
                INSERT IGNORE INTO PYTHONCONFIG
                (ACAO,DTACAO,NUMPREVENDA,TC,PASSO) SELECT '%s', NOW(),'%s','%s','%s'
                ''' % (str(Variaveis.Texto), int(Variaveis.NroPrevenda), int(Variaveis.Tc), int(Variaveis.Passo)))

            log.EscreverLog(Variaveis.Query)
            FuncoesBD.SqlSlave(str(Variaveis.Query))

            if Variaveis.Troco == "S":
                log.EscreverLog(Texto)

                autoit.send("{ALTDOWN}l{ALTUP}")
                log.EscreverLog("ALT+L")
                log.EscreverLog("Enter")
                log.EscreverLog('Timer ' + str(Variaveis.TDig))
                time.sleep(Variaveis.TDig)

                log.EscreverLog('Timer ' + str(Variaveis.TTela))
                autoit.win_wait_active("[Class:TFRM_LANCAMENTOTROCO]", Variaveis.TTela)

                autoit.control_click("[Class:TFRM_LANCAMENTOTROCO]", "TRzBmpButton1")
                log.EscreverLog('Timer ' + str(Variaveis.TEnter))
                time.sleep(Variaveis.TEnter)

                SENHAFUNC.SENHAFUNC()

                log.EscreverLog("{ESC}")
                autoit.send("{ESC}")
                log.EscreverLog('Timer ' + str(Variaveis.TDig))
                time.sleep(Variaveis.TDig)

                log.EscreverLog("{ESC}")
                autoit.send("{ESC}")
                log.EscreverLog('Timer ' + str(Variaveis.TDig))
                time.sleep(Variaveis.TDig)

            else:
                log.EscreverLog(Texto)
                autoit.control_click("[Class:TFRM_ENTREGASPENDENTES]", "TRzBitBtn3")
                log.EscreverLog('Timer ' + str(Variaveis.TEnter))
                time.sleep(Variaveis.TEnter)
                SENHAFUNC.SENHAFUNC()
                log.EscreverLog('Timer ' + str(Variaveis.TTela))
                autoit.win_wait_active("[Class:TFRM_ALTDADOSENTREG]", Variaveis.TTela)
                log.EscreverLog('Timer ' + str(Variaveis.TEnter))
                time.sleep(Variaveis.TEnter)
                autoit.control_click("[Class:TFRM_ALTDADOSENTREG]", "TRzBmpButton1")
                log.EscreverLog('Timer ' + str(Variaveis.TEnter))
                time.sleep(Variaveis.TEnter)
                if Variaveis.Recebe =="S" :
                    RecebeDinheiro.RecebeDinheiro()

                log.EscreverLog("{ESC}")
                autoit.send("{ESC}")
                log.EscreverLog('Timer ' + str(Variaveis.TDig))
                time.sleep(Variaveis.TDig)

                log.EscreverLog("{ESC}")
                autoit.send("{ESC}")
                log.EscreverLog('Timer ' + str(Variaveis.TDig))
                time.sleep(Variaveis.TDig)




        except:
            log.EscreverLog("Error")
    else:
        log.EscreverLog('Não existe Entrega')

    log.EscreverLog('Sai Função Baixa Entrega')
