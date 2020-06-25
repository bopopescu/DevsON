# -*- coding: utf-8 -*-
# ------------------------- Tempo Add ----------------------------- #
Tempo               = 0
TempoAdd            = 0
TempoAddFinalVenda  = 0
# ------------------------- Contadores ---------------------------- #
Nro      = 0
# ------------------------- Parametros----------------------------- #
TesteRapido = 'N'
AtivaLog    ='S'
Datahora    = "2017-05-22 14:50:30"
Break       = 'N'
Retornou    = 0
Loop        = 0
NVezes      = 0
NQtdProd    = 0
Valida          ='S'
Log             ='N'
sBanco      = 'N'

# ---- Dados da Loja
CodLoja     = '0'
CodTerminal = '0'
UfLoja      = ''

# ---- Dados Para Venda
DocFiscal           = ''
NroPrevenda         = 0
NCupom              = 0
VendedorAutomatico  = 'N'
Medico              = '13'
CodProd             = 0
AtwDesc             = 0

# ---- Configuração Loja
ControlarTroco      = 'N'
PrevAuto            = 'N'
PedeCpf             = 'N'
Recebe              = 'N'
Troco               = 'N'


# ---- Clientes P/ Venda
TTipoCli=''
CliV    = "0"
CliE    = "0"
CliP    = "0"
CliC    = "0"
NCodCli = 0
Cli     = 0
sCPF    = ''

# ---- Dados do Vendedor
CodVendedor = '1'''
SenhaAdmin  = '1'

# ---- VARIAVEIS
SN                  = 'S'
Retorno     = 'N'
Passo       = 0
Tc          = 0
Texto       = ''

# ------------------------- Despesas ------------------------- #
CaixaDestino = '002'
ContaBanco   =9
CodDespE     =95
CodDespS     =94
# ------------------------- Despesas ------------------------- #
# ------------------------- Dados do Medico ------------------------------ #

# ------------------------- Tempo por tela ------------------------- #

'''
Tempo       = 0
TClick      = (1.0/1.0)
TTeclaF     = (15.0/10.0)
TGrid       = (75.0/100.0)

TDig        = (75.0/100.0)

TEnterR     = (5.0/100.0)
TEnter      = (1.0/1.0)
TEnterB     = (5.0/1.0)
TEnterM     = (8.0/1.0)
TEnterL     = (10.0/1.0)


TAlertaRR   = (5.0/10.0)
TAlertaR    = (1.0/1.0)    #2.00
TAlertaB    = (2.0/1.0)    #2.00
TAlertaM    = (2.0/1.0)    #5.00
TAlertaL    = (20.0/1.0)   #10.00

TSql        = (5.0/10)
TCodVend    = (175.0/100)
TSaiCodVend = (5.0/10)
TCliente    = (2.0/1.0)     #3.00
TConvenio   = (3.0/1.0)    #8.00


TTelaR      = 1   #1.00
TTela       = 3   #1.00
TTelaB      = 5   #1.00
TTelaM      = 7   #1.00
TTelaL      = 10  #1.00
TFinal      = 15  #2.00


TTAltW      = 5
TTelaCPF    = 10
TTelaPgto   = 20
TPgto       = 10
TVenda      = 30
'''
# ------------------------- Tempo por tela ------------------------- #

# ------------------------- Sqls ------------------------- #
NQuery      = 0
Query       = 'Sql'


LocCupom =\
            '''
            SELECT 
                V.CUPOM,
                V.CODCLI
            FROM MYOURO.VENDA V
                INNER JOIN MYOURO.PENDENTES P ON P.IDVENDA = V.IDVENDA AND P.STATUS ='A'
            WHERE 
                TIMESTAMP(V.DATAHORAVENDA,V.HORAVENDA) >= (SELECT DTACAO FROM MYFRONT.PYTHONCONFIG P WHERE P.ACAO = 'INI') 
                AND V.CODLOJA = %s       
                AND V.NUMPREVENDA = ''' % (CodLoja)

sLocPrevenda    =\
                '''
                SELECT  
                    V.CODVENDA,  
                    V.NUMPREVENDA,  
                    IF(V.IDENDENTREGA > 0,IF(V.ENTREG_FORMAPGTO="A","S","N"),IF(V.TIPOVENDA = "C","N","S")) AS RECEBE,  
                    V.IDENDENTREGA,  
                    V.CODCLIENTE,  
                    V.TIPOVENDA,  
                    V.ENTREG_FORMAPGTO,  
                    V.STATUSVENDA  
                FROM VENDAS V  
                WHERE  
                V.CODLOJA =  %s  
                AND  V.STATUSVENDA ="P"  
                ORDER BY  
                    TIMESTAMP(V.DATAVENDA,V.HORAVENDA);
                ''' % (CodLoja)


sLocPrevendaN   ='SELECT ' \
                 'V.CODVENDA, ' \
                 'V.NUMPREVENDA, ' \
                 'IF(V.IDENDENTREGA > 0,IF(V.ENTREG_FORMAPGTO="A","S","N"),IF(V.TIPOVENDA = "C","N","S")) AS RECEBE, ' \
                 'V.IDENDENTREGA, ' \
                 'V.CODCLIENTE, ' \
                 'V.TIPOVENDA, ' \
                 'V.ENTREG_FORMAPGTO, ' \
                 'V.STATUSVENDA ' \
                 'FROM VENDAS V ' \
                 'WHERE ' \
                 'V.CODLOJA = ' + str(CodLoja) + ' AND ' \
                 'V.STATUSVENDA ="P" ' \
                 'AND V.NUMPREVENDA = '


LocPrevenda = sLocPrevenda



sLocEntrega     ='SELECT ' \
                'VD.CODLOJA, ' \
                'TIMESTAMP(VD.DATAHORAVENDA,VD.HORAVENDA) AS DATAVENDA, ' \
                'VD.NUMPREVENDA, ' \
                'COALESCE(VD.MODELO, 0) AS MODELO, ' \
                'COALESCE(VD.SERIE, 0) AS SERIE, ' \
                'VD.CUPOM, ' \
                'E.TIPOVENDA, ' \
                'E.ENTREG_FORMAPGTO, ' \
                'E.VALTROCOPARA, ' \
                'E.DATATROCO, ' \
                'E.CODCAIXATROCOSAI, ' \
                'if(COALESCE(E.CODCAIXATROCOSAI,0) = 0 and E.VALTROCOPARA > 0,"S","N") as TROCO, ' \
                'CASE ' \
                'E.ENTREG_FORMAPGTO ' \
                'WHEN "O" THEN "S" ' \
                'WHEN "Q" THEN "S" ' \
                'WHEN "D" THEN "S" ' \
                'ELSE "N"   ' \
                'END AS RECEBE,' \
                'CASE E.TIPOVENDA ' \
                'WHEN "V" THEN "À Vista" ' \
                'WHEN "E" THEN "Especial" ' \
                'WHEN "P" THEN "Prazo" ' \
                'WHEN "C" THEN "Convênio" ' \
                'WHEN "T" THEN "Transferência" ' \
                'WHEN "M" THEN "Entrega Avulsa" ' \
                'END AS DESCRTIPOVENDA, ' \
                'CASE E.ENTREG_FORMAPGTO ' \
                'WHEN "A" THEN "Antecipado no Caixa" ' \
                'WHEN "R" THEN "Reembolso Postal" ' \
                'WHEN "C" THEN "Convênio" ' \
                'WHEN "P" THEN "À Prazo" ' \
                'WHEN "O" THEN "Cartão" ' \
                'WHEN "Q" THEN "Cheque" ' \
                'WHEN "D" THEN "Dinheiro" ' \
                'END AS DESCRENTREG_FORMAPGTO, ' \
                'CASE E.TIPOENTREGA ' \
                'WHEN "C" THEN "Cobrança" ' \
                'WHEN "D" THEN "Entregar Documentos" ' \
                'WHEN "M" THEN "Compras" ' \
                'WHEN "P" THEN "Pagamentos" ' \
                'WHEN "R" THEN "Recebimentos" ' \
                'WHEN "V" THEN "Venda" ' \
                'END AS DESCRTIPOENTREGA ' \
                'FROM ENTREGAS E ' \
                'inner JOIN VENDA VD ON (VD.IDVENDA = E.IDVENDA) ' \
                'WHERE ' \
                'E.CODLOJADIG =  ' + str(CodLoja) + ' AND ' \
                'E.STATUS = "P" ' \
                'ORDER BY ' \
                'TIMESTAMP(VD.DATAHORAVENDA,VD.HORAVENDA);'


sLocEntregaN    ='SELECT ' \
                'VD.CODLOJA, ' \
                'TIMESTAMP(VD.DATAHORAVENDA,VD.HORAVENDA) AS DATAVENDA, ' \
                'VD.NUMPREVENDA, ' \
                'COALESCE(VD.MODELO, 0) AS MODELO, ' \
                'COALESCE(VD.SERIE, 0) AS SERIE, ' \
                'VD.CUPOM, ' \
                'E.TIPOVENDA, ' \
                'E.ENTREG_FORMAPGTO, ' \
                'E.VALTROCOPARA, ' \
                'E.DATATROCO, ' \
                'E.CODCAIXATROCOSAI, ' \
                'if(COALESCE(E.CODCAIXATROCOSAI,0) = 0 and E.VALTROCOPARA > 0,"S","N") as TROCO, ' \
                'CASE ' \
                'E.ENTREG_FORMAPGTO ' \
                'WHEN "O" THEN "S" ' \
                'WHEN "Q" THEN "S" ' \
                'WHEN "D" THEN "S" ' \
                'ELSE "N"   ' \
                'END AS RECEBE,' \
                'CASE E.TIPOVENDA ' \
                'WHEN "V" THEN "À Vista" ' \
                'WHEN "E" THEN "Especial" ' \
                'WHEN "P" THEN "Prazo" ' \
                'WHEN "C" THEN "Convênio" ' \
                'WHEN "T" THEN "Transferência" ' \
                'WHEN "M" THEN "Entrega Avulsa" ' \
                'END AS DESCRTIPOVENDA, ' \
                'CASE E.ENTREG_FORMAPGTO ' \
                'WHEN "A" THEN "Antecipado no Caixa" ' \
                'WHEN "R" THEN "Reembolso Postal" ' \
                'WHEN "C" THEN "Convênio" ' \
                'WHEN "P" THEN "À Prazo" ' \
                'WHEN "O" THEN "Cartão" ' \
                'WHEN "Q" THEN "Cheque" ' \
                'WHEN "D" THEN "Dinheiro" ' \
                'END AS DESCRENTREG_FORMAPGTO, ' \
                'CASE E.TIPOENTREGA ' \
                'WHEN "C" THEN "Cobrança" ' \
                'WHEN "D" THEN "Entregar Documentos" ' \
                'WHEN "M" THEN "Compras" ' \
                'WHEN "P" THEN "Pagamentos" ' \
                'WHEN "R" THEN "Recebimentos" ' \
                'WHEN "V" THEN "Venda" ' \
                'END AS DESCRTIPOENTREGA ' \
                'FROM ENTREGAS E ' \
                'inner JOIN VENDA VD ON (VD.IDVENDA = E.IDVENDA) ' \
                'WHERE ' \
                'E.CODLOJADIG =  ' + str(CodLoja) + ' AND ' \
                'E.STATUS = "P" ' \
                'AND VD.NUMPREVENDA =  '

LocEntrega = sLocEntrega



# ------------------------- Produtos para Venda -------------------------- #
#Codido Produto
#Desconto
#Qtde
#Tipo produto
# N - Normal / Pos - Pos-Venda / L - Lote / P - Psico

AProduto        = [['1','0','1','N'],['2','0','1','N'],['3','0','1','N'],['4','0','1','N'],['5','0','1','N'],['6','0','1','N'],['7','0','1','N'],['8','0','1','N'],['11','0','1','N'],['12','0','1','N']]

AProdEncomenda   = [["7","0","2","S"]]

AProdutoAltw    = [["2","3","3","N"],["9","10","3","N"],["10","0","3","N"]]

AProdPromocao   = [["2","0","3","N"],["9","0","3","N"],["10","0","3","N"]]

AProdPromoltw   = [["2","0","3","N"],["9","0","3","N"],["10","0","3","N"]]

AProdutoLote = [["11","0","1","Pos"], ["15","0","1","L"], ["2649","0","1","P"]]

# ------------------------- Produtos para Venda -------------------------- #