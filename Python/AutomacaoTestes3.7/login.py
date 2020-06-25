# -*- coding: utf-8 -*-
import autoit
import os
import time
import Variaveis
import ProcessoWindows

#from log import LogSistema
import log
import Tela

class LogarSistema(object):

    __sSistema = None
    __sArquivoMyOuro = "c:\\ourofarma\\ourofarma.exe"
    __sArqquivoMyFront = "c:\\ourofarma\\frontfarma.exe"

    def __init__(self, sAplicativo):
        self.__sSistema = sAplicativo
    ## End def __init__

    def login(self):
        log.EscreverLog("Função Login")
        if self.__sSistema == 'Ourofarma':
            pass
        elif self.__sSistema == 'FrontFarma':
            ## Inicio do Frontfarma
            if ProcessoWindows.ProcessoWindows("FRONTFARMA.exe"):
                os.system("taskkill /F /im frontfarma.exe")
                log.EscreverLog("Fechado Fechando Front")

            autoit.run(self.__sArqquivoMyFront)
            log.EscreverLog('Tempo.do a tela de login')

            TelaAlerta.TelaAlerta('Tempo.do alerta lista de servidores','Não teve Alerta Lista de Servidores')
            TelaAlerta.TelaAlerta('Tempo.do alerta para verificar a data do servidor','Não teve Alerta data')


            log.EscreverLog('Tempo.do a tela de login')
            autoit.win_wait_active("[Class:TFRM_LOGIN]", Variaveis.TTela)
            log.EscreverLog('Passando a senha')
            autoit.control_send("[CLASS:TFRM_LOGIN]", "TRzButtonEdit1", "1")
            time.sleep(Variaveis.TDig)
            autoit.send("{ENTER}")
            time.sleep(Variaveis.TEnter)
            log.EscreverLog('Confirmando senha')
            time.sleep(Variaveis.TEnter)

            try:
                log.EscreverLog('Tempo.do alerta de checkfront Nâo ativo')
                autoit.win_wait_active("[Class:TFRM_VSMTASKDIALOG]", Variaveis.TTela)
                log.EscreverLog('Botão ok')
                autoit.control_click("[Class:TFRM_VSMTASKDIALOG]", "TRzBitBtn1")
                log.EscreverLog('Clicou ok')
            except:
                log.EscreverLog('Não teve Alerta de checkfront Nâo ativo')

            try:
                log.EscreverLog('Tempo.do alerta para importar tabela IBPT')
                autoit.win_wait_active("[Class:TFRM_VSMTASKDIALOG]", Variaveis.TTela)
                log.EscreverLog('Botão Ok')
                autoit.control_click("[Class:TFRM_VSMTASKDIALOG]", "TRzBitBtn1")
                log.EscreverLog('Clicou Ok')
                time.sleep(Variaveis.TEnter)
            except:
                log.EscreverLog('Não teve Alerta Ibpt')

            log.EscreverLog('Tempo.do tela de venda')
            autoit.send("{ESC}")
            autoit.send("{ESC}")
            autoit.win_wait_active("[Class:TFRM_VENDAS]", Variaveis.TTela)
            autoit.send("{ESC}")
            autoit.send("{ESC}")
            log.EscreverLog('Tela venda aberta')
            time.sleep(Variaveis.TEnter)
            ## Final frontFarma
        else:
            log.EscreverLog('Sistema não definido')

    def Crtx(self):
        log.EscreverLog('Função CRTX')
        log.EscreverLog('ESC')
        autoit.send("{ESC}")
        log.EscreverLog('Timer ' + str(Variaveis.TDig))
        time.sleep(Variaveis.TDig)

        log.EscreverLog('ESC')
        autoit.send("{ESC}")
        log.EscreverLog('Timer ' + str(Variaveis.TDig))
        time.sleep(Variaveis.TDig)


        log.EscreverLog('Limpa Tela')
        autoit.send("{CTRLDOWN}x{CTRLUP}")
        log.EscreverLog('Timer ' + str(Variaveis.TDig))
        time.sleep(Variaveis.TDig)
        try:
            log.EscreverLog('Tempo.do alerta sem Produto ' + 'Timer ' + str(Variaveis.TTela))
            autoit.win_wait_active("[Class:TFRM_VSMTASKDIALOG]", Variaveis.TTela)
            log.EscreverLog('Botão Ok')

            autoit.control_click("[Class:TFRM_VSMTASKDIALOG]", "TRzBitBtn1")
            log.EscreverLog('Clicou Ok')
            log.EscreverLog('Timer ' + str(Variaveis.TDig))
            time.sleep(Variaveis.TDig)
        except:
            log.EscreverLog('Não teve Alerta, Limpando tela')


        log.EscreverLog('Enter')
        autoit.send("{ENTER}")
        log.EscreverLog('Timer ' + str(Variaveis.TEnterR))
        time.sleep(Variaveis.TEnter)
        log.EscreverLog('Sai Função CRTX')