# -*- coding: utf-8 -*-
import autoit
import time
import Variaveis
import log
import SENHAFUNC
from DAO import FuncoesBD


def Estorno(Num):
    autoit.send('Entra Função Estorno')
    FuncoesBD.LocalizaCupom(Num)
    if Variaveis.Retorna == 'S':
        autoit.send("{ALTDOWN}x{ALTUP}")
        SENHAFUNC.SENHAFUNC()
        try:
            log.EscreverLog('Estorno de Venda')
            autoit.win_wait_active("[Class:TFRM_ESTORNO]", Variaveis.TTela)
            autoit.control_send("[CLASS:TFRM_ESTORNO]", "TRzNumericEdit1",str(Variaveis.LocCupom))
            time.sleep(Variaveis.TDig)
            autoit.control_click("[CLASS:TFRM_ESTORNO]", "TRzBitBtn2")
            time.sleep(Variaveis.TDig)
            autoit.control_click("[CLASS:TFRM_ESTORNO]", "TVSMDBGrid1")
            time.sleep(Variaveis.TDig)
            autoit.send("{SPACE}")
            time.sleep(Variaveis.TDig)
            autoit.control_click("[CLASS:TFRM_ESTORNO]", "TRzBitBtn1")
            time.sleep(Variaveis.TAlertaB)
            autoit.send("{ENTER}")
            time.sleep(Variaveis.TAlertaB)
            autoit.send("{ENTER}")
        except:
            log.EscreverLog('Erro')
    else:
        log.EscreverLog('Cupom não encontrado')
    log.EscreverLog('Sai Função Estorno')

