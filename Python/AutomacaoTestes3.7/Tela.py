# -*- coding: utf-8 -*-
import autoit
import sys
import Variaveis
import Tempo
import Tela
import log
from random import choice
import Tecla
import Roteiro_Lanc
import ParametrosAddVariaveis

def LancamentoVenda():
    log.EscreverLog('Tela de Lançamento de Vendas')
    try:
        Variaveis.Tempo = (Variaveis.TempoAdd + 10)
        log.EscreverLog('Tempo. ate ' + str(Variaveis.Tempo) + ' segundos')
        autoit.win_wait_active("[Class:TFRM_VENDAS]", Variaveis.Tempo)
    except:
        Tempo.TeclaAcao()

def LancamentoNroPrevenda():
    log.EscreverLog('Tela de Informar Nro Prevenda')
    try:
        Variaveis.Tempo = (Variaveis.TempoAdd + 10)
        log.EscreverLog('Tempo. ate ' + str(Variaveis.Tempo) + ' segundos')
        autoit.win_wait_active("[Class:TFRM_NUMPREVENDA]", Variaveis.Tempo)
        log.EscreverLog('Tela de Nro Pre-venda')

        if Variaveis.DocFiscal == "PREV":
            if Variaveis.PrevAuto == 'S':
                log.EscreverLog('Numero de Pre-venda Automatico')
                log.EscreverLog('Confirma Pre-venda')
                autoit.control_click("[Class:TFRM_NUMPREVENDA]", "TVSMColorButton1")
                Tempo.Click()

            if Variaveis.PrevAuto == 'N':
                log.EscreverLog('Informar Numero de Pre-venda')
                Sai = 'N'
                while Sai == 'N':
                    log.EscreverLog("Numero Prevenda: " + str(Variaveis.NroPrevenda))
                    Variaveis.NroPrevenda = Variaveis.NroPrevenda + 1
                    log.EscreverLog("Numero Prevenda: " + str(Variaveis.NroPrevenda))
                    autoit.control_set_text("[Class:TFRM_NUMPREVENDA]", "TRzNumericEdit1", str(Variaveis.NroPrevenda))
                    Tempo.Dig()
                    log.EscreverLog("Confirmando Numero: " + str(Variaveis.NroPrevenda))
                    Tecla.Enter()
                    try:
                        Variaveis.Tempo = (Variaveis.TempoAdd + 1)
                        log.EscreverLog('Tempo. ate ' + str(Variaveis.Tempo) + ' segundos')
                        autoit.win_wait_active("[Class:TFRM_VSMTASKDIALOG]", Variaveis.Tempo)
                        log.EscreverLog(str(Variaveis.NroPrevenda) + ' Numero Pre-venda ja existente')
                        Tecla.Enter()
                        log.EscreverLog("Add Numero Proxima Prevenda: ")
                    except:
                        log.EscreverLog('Confirma Pre-venda')
                        autoit.control_click("[Class:TFRM_NUMPREVENDA]", "TVSMColorButton1")
                        Tempo.Click()
                        Sai = 'S'
    except:
        Tempo.TeclaAcao()







def TelaAlertaCrt(t, e):
    log.EscreverLog('Tela de Alerta Crt')
    try:
        Variaveis.Tempo = (Variaveis.TempoAdd + 3)
        log.EscreverLog('Tempo. ate ' + str(Variaveis.Tempo) + ' segundos')
        autoit.win_wait_active("[Class:TFRM_VSMTASKDIALOG]", Variaveis.Tempo)
        Tempo.Click()
        log.EscreverLog(str(t))
        autoit.control_click("[Class:TFRM_VSMTASKDIALOG]", "TVSMColorButton1")
        log.EscreverLog('Clicou Ok')
    except:
        log.EscreverLog(str(e))
    Tecla.Enter()


def AlertaRejeicao():
    log.EscreverLog('Tela de Alerta')
    try:
        Variaveis.Tempo = (Variaveis.TempoAddFinalVenda + 5)
        log.EscreverLog('Tempo ate ' + str(Variaveis.Tempo) + ' segundos')
        autoit.win_wait_active("[Class:TFRM_VSMTASKDIALOG]", Variaveis.Tempo)
        Tempo.EnterProduto()
        autoit.control_click("[Class:TFRM_VSMTASKDIALOG]", "TVSMColorButton1")
        log.EscreverLog('Clicou Ok')
    except:
        Tempo.EnterProduto()



def AlertaTelaVenda(t,e):
    log.EscreverLog('Tela Alerta')
    try:
        Variaveis.Tempo = (30)
        log.EscreverLog('Tempo ate ' + str(Variaveis.Tempo) + ' segundos')
        autoit.win_wait_active("[Class:TFRM_VSMTASKDIALOG]", Variaveis.Tempo)
        log.EscreverLog(str(t))
        Tempo.EnterProduto()
        autoit.control_click("[Class:TFRM_VSMTASKDIALOG]", "TVSMColorButton1")
        log.EscreverLog('Clicou Ok')
    except:
        log.EscreverLog(str(e))
        Tecla.F8LancamentoVenda()



def Alerta(t, e):
    log.EscreverLog('Tela de Alerta')
    try:
        Variaveis.Tempo = (Variaveis.TempoAddFinalVenda + 1)
        log.EscreverLog('Tempo ate ' + str(Variaveis.Tempo) + ' segundos')
        autoit.win_wait_active("[Class:TFRM_VSMTASKDIALOG]", Variaveis.Tempo)
        log.EscreverLog(str(t))
        Tempo.EnterProduto()
        autoit.control_click("[Class:TFRM_VSMTASKDIALOG]", "TVSMColorButton1")
        log.EscreverLog('Clicou Ok')
    except:
        log.EscreverLog(str(e))


def AlertaProduto(t, e):
    log.EscreverLog('Validações do Produto')
    try:
        Variaveis.Tempo = (Variaveis.TempoAdd + 0.15)
        log.EscreverLog('Tempo. ate ' + str(Variaveis.Tempo) + ' segundos')
        autoit.win_wait_active("[Class:TFRM_VSMTASKDIALOG]", Variaveis.Tempo)
        Tempo.Click()
        log.EscreverLog(str(t))
        autoit.control_click("[Class:TFRM_VSMTASKDIALOG]", "TVSMColorButton1")
        log.EscreverLog('Clicou Ok')
    except:
        log.EscreverLog(str(e))


def FinalVenda():
    log.EscreverLog('Tela de Finalização de Venda')
    try:
        Variaveis.Tempo = (Variaveis.TempoAddFinalVenda + 60)
        log.EscreverLog('Tempo. ate ' + str(Variaveis.Tempo) + ' segundos')
        autoit.win_wait_active("[Class:TFRM_FINALVENDA]", Variaveis.Tempo)
        Tempo.TeclaAcaoFinalVenda()
        log.EscreverLog('Clicando Campo Cliente')
        autoit.control_click("[Class:TFRM_FINALVENDA]", "TRzDBButtonEdit6")
        log.EscreverLog('Campo Cliente')
    except:
        Tempo.TelaFinalVenda()

def Autorizando():
    log.EscreverLog('Atorizando Venda')
    try:
        Variaveis.Tempo = (Variaveis.TempoAddFinalVenda + 10)
        log.EscreverLog('Tempo. ate ' + str(Variaveis.Tempo) + ' segundos')
        autoit.win_wait_active("[Class:TFRM_FINALVENDA.pnlStatusForm]", Variaveis.Tempo)
        Tempo.TelaFinalVenda()
    except:
        Tempo.TelaFinalVenda()



def LISTAFORMAPAGTO():
    log.EscreverLog("Listar Forma de Pagamento para Remover")
    try:
        Variaveis.Tempo = (Variaveis.TempoAddFinalVenda + 5)
        log.EscreverLog('Tempo. ate ' + str(Variaveis.Tempo) + ' segundos')
        autoit.win_wait_active("[Class:TFRM_LISTAFORMAPAGTO]", Variaveis.Tempo)
        log.EscreverLog("Remover Forma de Pagamento")
        autoit.control_click("[Class:TFRM_LISTAFORMAPAGTO]", "TVSMColorButton1")
        log.EscreverLog("Removendo Forma Pagamento")
        Tempo.TeclaAcao()
    except:
        Tempo.TeclaAcao()


def ComprovanteNFCe():
    log.EscreverLog('Tela Comprovante NFCe')
    try:
        Variaveis.Tempo = (Variaveis.TempoAdd + 5)
        log.EscreverLog('Tempo. ate ' + str(Variaveis.Tempo) + ' segundos')
        autoit.win_wait_active("[Class:TForm]", Variaveis.Tempo)
        log.EscreverLog('Tela Comprovante')
        Tecla.Esc()
        Variaveis.Tempo = (Variaveis.TempoAdd + 5)
        log.EscreverLog('Tempo. ate ' + str(Variaveis.Tempo) + ' segundos')
        autoit.win_wait_active("[Class:TFRM_TELACOMPROVANTE]", Variaveis.Tempo)
        Tecla.Esc()
        Tempo.TeclaAcao()
        log.EscreverLog('Fecha Comprovante')
    except:
        log.EscreverLog('Impressao Direta')


def ComprovanteDANFe():
    log.EscreverLog('Comprovante DANFe')
    try:
        Variaveis.Tempo = (Variaveis.TempoAdd + 5)
        log.EscreverLog('Tempo. ate ' + str(Variaveis.Tempo) + ' segundos')
        autoit.win_wait_active("[Class:TFRM_TELACOMPROVANTE]", Variaveis.Tempo)
        log.EscreverLog('Comprovante DANFe')
        Tecla.Esc()
        log.EscreverLog('Fecha Comprovante')
    except:
        log.EscreverLog('Sem Impressao')


def Rejeicao():
    log.EscreverLog('Valida Rejeição')
    try:
        Variaveis.Tempo = (Variaveis.TempoAdd + 5)
        log.EscreverLog('Tempo. ate ' + str(Variaveis.Tempo) + ' segundos')
        autoit.win_wait_active("[Class:TFRM_REJEICAONFE2]", Variaveis.Tempo)
        log.EscreverLog('Rejeição')
        Tecla.Esc()
        Tecla.Enter()
        Tecla.Esc()
        Tela.LISTAFORMAPAGTO()
        Tecla.Crtx()
        sys.exit()
    except:
        Tempo.TeclaAcao()


def ValidacaoNF_NFC():
    log.EscreverLog('Validacao NF/NFC')
    try:
        Variaveis.Tempo = (Variaveis.TempoAddFinalVenda + 5)
        log.EscreverLog('Tempo. ate ' + str(Variaveis.Tempo) + ' segundos')
        autoit.win_wait_active("[Class:TfrmMostraMensagensNFe]", Variaveis.Tempo)
        log.EscreverLog("Validações NF-e / NFC-e")
        autoit.control_click("[Class:TfrmMostraMensagensNFe]", "TVSMColorButton1")
        log.EscreverLog("Confirmou Validação")
        Tempo.Click()
        Tela.LISTAFORMAPAGTO()
        for x in range(0, 3):
            Tecla.Esc()
        Tecla.Crtx()
        Variaveis.Break = 'S'
        Roteiro_Lanc.Roteiro()
    except:
        Tempo.TeclaAcao()


def ValidacaoFinalVenda():
    log.EscreverLog('ValidacaoFinalVenda')
    try:
        Variaveis.Tempo = (Variaveis.TempoAdd + 0.25)
        log.EscreverLog('Tempo. ate ' + str(Variaveis.Tempo) + ' segundos')
        autoit.win_wait_active("[Class:TfrmMostraMensagens]", Variaveis.Tempo)
        log.EscreverLog("Massage de Validação")
        Tecla.Esc()
        Tela.LISTAFORMAPAGTO()
        Tecla.Crtx()
        sys.exit()
    except:
        Tempo.TeclaAcao()



def TratamentoRejeicoes():
    log.EscreverLog('Tratamento de Rejeicoes')
    try:
        Tecla.CrtE()
        Tecla.CrtR()

        Variaveis.Tempo = (Variaveis.TempoAdd + 1)
        log.EscreverLog('Tempo. ate ' + str(Variaveis.Tempo) + ' segundos')
        autoit.win_wait_active("[Class:TFRM_REJEICAONFE2]", Variaveis.Tempo)
        for x in range(0, 1000):
            log.EscreverLog("Tratar Rejeicoes")
            Tempo.TelaAcao()
            autoit.control_click("[Class:TFRM_REJEICAONFE2]", "TVSMColorButton1")
            Tempo.TelaAcao()
            Tela.AlertaRejeicao()
            Tela.AlertaRejeicao()
            Tempo.TeclaAcao()
    except:
        Tempo.TeclaAcao()


def Validacao():
    try:
        Variaveis.Tempo = (Variaveis.TempoAdd + 0.05)
        log.EscreverLog('Tempo. ate ' + str(Variaveis.Tempo) + ' segundos')
        autoit.win_wait_active("[Class:TfrmMostraMensagens]", Variaveis.Tempo)
        log.EscreverLog("Messagem de Validação")
        Tecla.Esc()
    except:
        log.EscreverLog("Sem Alerta")

def PedeCPF():
    if Variaveis.PedeCpf == 'S':
        log.EscreverLog("Função Pede CPF")
        try:
            Variaveis.Tempo = (Variaveis.TempoAddFinalVenda + 10)
            log.EscreverLog('Tempo. ate ' + str(Variaveis.Tempo) + ' segundos')
            autoit.win_wait_active("[Class:TFRM_VENDACPF]", Variaveis.Tempo)
            log.EscreverLog("Pede CPF")
            Tempo.Dig()
            ParametrosAddVariaveis.GeraCpf()
            autoit.control_send("[Class:TFRM_VENDACPF]", "TRzDBEdit1",str(Variaveis.sCPF))
            Tempo.Click()
            autoit.control_click("[Class:TFRM_VENDACPF]", "TVSMColorButton3")
            log.EscreverLog("Fecha Pede CPF")
        except:
            log.EscreverLog('Não pediu CPF')
    if Variaveis.PedeCpf == 'N':
        log.EscreverLog('Não pediu CPF')


def RecebeDinheiro():
    log.EscreverLog("Função RecebeDinheiro")
    try:
        log.EscreverLog("Forma Paganento")
        Variaveis.Tempo = (Variaveis.TempoAddFinalVenda + 5)
        log.EscreverLog('Tempo. ate ' + str(Variaveis.Tempo) + ' segundos')
        autoit.win_wait_active("[Class:TFRM_FORMAPAGTOOFF]", Variaveis.Tempo)
        log.EscreverLog("Abriu Forma Paganento")
        Recebe = choice([0, 1, 2])

        if Recebe == 1 or Recebe == 2:
            Tempo.TeclaAcaoFinalVenda()
            log.EscreverLog('Zerando Forma Dinheiro')
            autoit.control_set_text("[Class:TFRM_FORMAPAGTOOFF]", "TRzNumericEdit3", 0)
            Tecla.Enter()
            log.EscreverLog('Forma Pagamento Cheque')

        if Recebe == 2:
            Tempo.TeclaAcaoFinalVenda()
            log.EscreverLog('Zerando Forma Cheque')
            autoit.control_set_text("[Class:TFRM_FORMAPAGTOOFF]", "TRzNumericEdit2", 0)
            Tecla.Enter()
            log.EscreverLog('Forma Pagamento Cartão')

        if Recebe == 0:
            log.EscreverLog('Forma Pagamento Dinheiro')

        Tecla.TempoM()

        autoit.control_click("[Class:TFRM_FORMAPAGTOOFF]", "TVSMColorButton2")
        log.EscreverLog("Confirma Forma Pagamento")

        Tecla.TempoM()

        if Recebe == 1:
            try:
                Variaveis.Tempo = (Variaveis.TempoAddFinalVenda + 5)
                log.EscreverLog('Tempo. ate ' + str(Variaveis.Tempo) + ' segundos')
                autoit.win_wait_active("[Class:TFRM_CHEQUE]", Variaveis.Tempo)
                autoit.control_set_text("[Class:TFRM_CHEQUE]", "TRzButtonEdit2", str(Variaveis.CPF))
                Tecla.Enter()

                autoit.control_click("[Class:TFRM_CHEQUE]", "TRzNumericEdit1")
                Tecla.TempoM()
                Tecla.LimpaTexto()
                autoit.control_set_text("[Class:TFRM_CHEQUE]", "TRzNumericEdit1", '18')

                Tecla.Enter()

                autoit.control_set_text("[Class:TFRM_CHEQUE]", "TRzNumericEdit5", '1')

                Tecla.Enter()

                autoit.control_click("[Class:TFRM_CHEQUE]", "TVSMColorButton3")
                Tecla.TempoM()



            except:
                log.EscreverLog('Timer ' + str(Variaveis.TAlertaR))

        if Recebe == 2:
            try:
                Variaveis.Tempo = (Variaveis.TempoAddFinalVenda + 5)
                log.EscreverLog('Tempo. ate ' + str(Variaveis.Tempo) + ' segundos')
                autoit.win_wait_active("[Class:TFRM_SELECIONACARTAO]", Variaveis.Tempo)
                autoit.control_set_text("[Class:TFRM_SELECIONACARTAO]", "TRzEdit1", '00000')
                Tecla.TempoM()

                autoit.control_click("[Class:TFRM_SELECIONACARTAO]", "TVSMColorButton2")
                Tecla.TempoM()
            except:
                log.EscreverLog('Timer ' + str(Variaveis.TAlertaR))

        Tecla.TempoM()

        try:
            Variaveis.Tempo = (Variaveis.TempoAddFinalVenda + 5)
            log.EscreverLog('Tempo. ate ' + str(Variaveis.Tempo) + ' segundos')
            autoit.win_wait_active("[Class:TFRM_REJEICAONFE2]", Variaveis.Tempo)
            log.EscreverLog('Tratamento de Rejeições')
            Tecla.TempoM()
            autoit.control_click("[Class:TFRM_SELECIONACARTAO]", "TVSMColorButton2")
            Tecla.TempoL()
            Tela.Alerta('Nota Rejeitada', 'Sem Alerta')
            for x in range(0, 3):
                Tecla.Esc()
        except:
            log.EscreverLog('Nota Aceita')

        log.EscreverLog("Fecha Forma Paganento")
        Tecla.TempoM()
    except:
        log.EscreverLog("Venda Prazo ou Convenio não Abre Forma Pagamento")
    log.EscreverLog("Sai Função RecebeDinheiro")
    Tempo.TelaAcao()


