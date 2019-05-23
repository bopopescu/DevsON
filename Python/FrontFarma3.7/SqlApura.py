# -*- coding: utf-8 -*-
import Variaveis
import log
from DAO import FuncoesBD


def SqlApura(SeqQuery,Nro):
    if SeqQuery == 'PREV':
        sSql = 'DROP TABLE IF EXISTS PYTHONVENDAS;'
        log.EscreverLog(sSql)
        FuncoesBD.SqlSlave(sSql)
        sSql = '''CREATE TABLE PYTHONVENDAS
                SELECT
                '00' AS SEQ,
                TIMESTAMP(V.DATAVENDA,V.HORAVENDA) AS DATAHORA,
                '%s' AS TC,
                '%s' AS PASSO,
                'PREVENDA' AS ACAO,
                V.NUMPREVENDA,
                V.CODVENDA AS IDVENDA,
                'VENDAS' AS TABELA,
                'CODCAIXA' AS CAMPO, 
                IF(V.CODCAIXA > 0,'PREENCHIDO','') AS VALOR,
                'IDFECHAMENTO' AS CAMPO2, 
                IF(V.IDFECHAMENTO > 0,'PREENCHIDO','') AS VALOR2
                FROM VENDAS V
                WHERE V.NUMPREVENDA = '%s';
                ''' % (str(Variaveis.Tc),str(Variaveis.Passo),str(Variaveis.Nro))
        log.EscreverLog(sSql)
        FuncoesBD.SqlSlave(sSql)

        sSql=   '''INSERT IGNORE INTO PYTHONCONFIG
                (
                    DTACAO,
                    TC,
                    PASSO,
                    ACAO,
                    NUMPREVENDA,
                    CHAVE,
                    TABELA,
                    CAMPO,
                    VALOR
                    )
                    SELECT
                    P.DATAHORA,
                    P.TC,
                    P.PASSO,
                    P.ACAO,
                    P.NUMPREVENDA,
                    P.IDVENDA,
                    P.TABELA,
                    P.CAMPO,
                    P.VALOR
                    FROM 
                    (
                    SELECT 
                    P.SEQ,
                    P.DATAHORA,
                    P.TC,
                    P.PASSO,
                    P.ACAO,
                    P.NUMPREVENDA,
                    P.IDVENDA,
                    P.TABELA,
                    P.CAMPO,
                    P.VALOR
                    FROM PYTHONVENDAS P
                    
                    UNION ALL 
                    
                    SELECT 
                    P.SEQ,
                    P.DATAHORA,
                    P.TC,
                    P.PASSO,
                    P.ACAO,
                    P.NUMPREVENDA,
                    P.IDVENDA,
                    P.TABELA,
                    P.CAMPO2,
                    P.VALOR2
                    FROM PYTHONVENDAS P
                    ) P
                    ORDER BY
                    P.TC,
                    P.PASSO,
                    P.NUMPREVENDA,
                    P.SEQ,
                    P.TABELA,
                    P.DATAHORA,
                    P.CAMPO;
                '''
        log.EscreverLog(sSql)
        FuncoesBD.SqlSlave(sSql)

    if SeqQuery == 'E':
        sSql = 'DROP TABLE IF EXISTS PYTHONENCOMENDA;'
        log.EscreverLog(sSql)
        FuncoesBD.SqlSlave(sSql)
        sSql=   '''CREATE TABLE PYTHONENCOMENDA
                    SELECT
                    '99' as SEQ,
                    TIMESTAMP(M.DATALANC,M.HORALANC) AS DATAHORA,
                    '%s' as TC,
                    '%s' as PASSO,
                    'ENCOMENDA' AS ACAO,
                    M.IDMOVCAIXA - 
                    (SELECT MIN(MM.IDMOVCAIXA) - 1001 FROM MYOURO.MOVCAIXA MM 
                    WHERE TIMESTAMP(MM.DATALANC,MM.HORALANC) >= '%s'
                    )AS NUMPREVENDA,
                    
                    'MOVCAIXA' AS TABELA,
                    'CODCAIXA' AS CAMPO,
                    IF(M.CODCAIXA>0,'PREENCHIDO','') AS VALOR,
                    
                    'IDFECHAMENTO' AS CAMPO2,
                    IF(M.IDFECHAMENTO>0,'PREENCHIDO','') AS VALOR2,
                    
                    'RECEBIMENTO' AS RTABELA,
                    'CODCAIXA' AS RCAMPO,
                    IF(R.CODCAIXA>0,'PREENCHIDO','') AS RVALOR,
                    
                    'IDFECHAMENTO' AS RCAMPO2,
                    IF(R.IDFECHAMENTO>0,'PREENCHIDO','') AS RVALOR2
                    
                    FROM MYOURO.MOVCAIXA M
                    INNER JOIN MYOURO.RECEBIMENTO_ORIGEM RO ON RO.IDMOVCAIXA = M.IDMOVCAIXA
                    INNER JOIN MYOURO.RECEBIMENTOS R ON R.IDRECEBIMENTO = RO.IDRECEBIMENTO
                    INNER JOIN MYOURO.PAGTOANTECIPADO PA ON PA.IDMOVCAIXA = M.IDMOVCAIXA
                    WHERE TIMESTAMP(M.DATALANC,M.HORALANC) >= '%s' ;
                ''' % (str(Variaveis.Tc),str(Variaveis.Passo),Variaveis.Datahora,Variaveis.Datahora)
        log.EscreverLog(sSql)
        FuncoesBD.SqlSlave(sSql)


        sSql = '''INSERT IGNORE INTO PYTHONCONFIG
                    (
                    DTACAO,
                    TC,
                    PASSO,
                    ACAO,
                    NUMPREVENDA,
                    TABELA,
                    CAMPO,
                    VALOR
                    )
                    SELECT
                    P.DATAHORA,
                    P.TC,
                    P.PASSO,
                    P.ACAO,
                    P.NUMPREVENDA,
                    P.TABELA,
                    P.CAMPO,
                    P.VALOR
                    FROM 
                    (
                    SELECT 
                    P.SEQ,
                    P.DATAHORA,
                    P.TC,
                    P.PASSO,
                    P.ACAO,
                    P.NUMPREVENDA,
                    P.TABELA,
                    P.CAMPO,
                    P.VALOR
                    FROM PYTHONENCOMENDA P

                    UNION 

                    SELECT 
                    P.SEQ,
                    P.DATAHORA,
                    P.TC,
                    P.PASSO,
                    P.ACAO,
                    P.NUMPREVENDA,
                    P.TABELA,
                    P.CAMPO2,
                    P.VALOR2
                    FROM PYTHONENCOMENDA P


                    UNION ALL 

                    SELECT 
                    P.SEQ,
                    P.DATAHORA,
                    P.TC,
                    P.PASSO,
                    P.ACAO,
                    P.NUMPREVENDA,
                    P.RTABELA,
                    P.RCAMPO,
                    P.RVALOR
                    FROM PYTHONENCOMENDA P

                    UNION 

                    SELECT 
                    P.SEQ,
                    P.DATAHORA,
                    P.TC,
                    P.PASSO,
                    P.ACAO,
                    P.NUMPREVENDA,
                    P.RTABELA,
                    P.RCAMPO2,
                    P.RVALOR2
                    FROM PYTHONENCOMENDA P



                    ) P
                    ORDER BY
                    P.TC,
                    P.PASSO,
                    P.NUMPREVENDA,
                    P.SEQ,
                    P.TABELA,
                    P.DATAHORA,
                    P.CAMPO;
               '''
        log.EscreverLog(sSql)
        FuncoesBD.SqlSlave(sSql)


    if SeqQuery !='E' and SeqQuery !='PREV' and SeqQuery >= 0:
        sSql = 'DROP TABLE IF EXISTS PYTHONVENDA;'
        log.EscreverLog(sSql)
        FuncoesBD.SqlSlave(sSql)
        if SeqQuery == 0:
            sSql =  '''
                    CREATE TABLE PYTHONVENDA
                    SELECT
                    V.SEQ,
                    V.DATAHORA,
                    P.TC,P.PASSO,P.ACAO,
                    V.NUMPREVENDA,
                    V.IDVENDA,
                    V.TABELA,
                    V.CAMPO,
                    V.VALOR,
                    V.CAMPO2,
                    V.VALOR2
                    FROM
                        (
                            SELECT 
                                '01' AS  SEQ,
                                TIMESTAMP(V.DATALANC,V.HORALANC) AS DATAHORA,
                                V.NUMPREVENDA,
                                V.IDVENDA,
                                'VENDA' AS TABELA,
                                'CODCAIXA' AS CAMPO, 
                                IF(V.CODCAIXA > 0,'PREENCHIDO','') AS VALOR,
                                'IDFECHAMENTO' AS CAMPO2, 
                                IF(V.IDFECHAMENTO > 0,'PREENCHIDO','') AS VALOR2
                            FROM MYOURO.VENDA V
                                WHERE 
                            V.DATALANC >=	(
                                            SELECT 
                                                MIN(DATE(P.DTACAO)) 
                                            FROM MYFRONT.PYTHONCONFIG P 
                                                WHERE 
                                            P.ACAO = 'BAIXAR PREVENDA' 
                                            AND P.TC = '%s' AND P.PASSO = '%s'
                                            )
                        ) V
                        INNER JOIN	( 
                                        SELECT 
                                            P.DTACAO,
                                            P.ACAO,
                                            P.TC,
                                            P.PASSO,
                                            P.NUMPREVENDA 
                                        FROM MYFRONT.PYTHONCONFIG P
                                            WHERE 
                                        P.ACAO = 'BAIXAR PREVENDA' 
                                        AND P.TC = '%s' AND P.PASSO = '%s'
                                    ) P ON V.NUMPREVENDA = P.NUMPREVENDA
                                    GROUP BY V.IDVENDA;
    
                    ''' %(str(Variaveis.Tc),str(Variaveis.Passo),str(Variaveis.Tc),str(Variaveis.Passo))
        if SeqQuery == 1:
            sSql =  '''
                    CREATE TABLE PYTHONVENDA
                    SELECT 
                    '01' AS  SEQ,
                    TIMESTAMP(V.DATALANC,V.HORALANC) AS DATAHORA,
                    '%s' as TC,
                    '%s' as PASSO,
                    'SAIDA DE TROCO' as ACAO,
                    '%s' as NUMPREVENDA,
                    V.IDVENDA,
                    'VENDA' AS TABELA,
                    'CODCAIXA' AS CAMPO, 
                    IF(V.CODCAIXA > 0,'PREENCHIDO','') AS VALOR,
                    'IDFECHAMENTO' AS CAMPO2, 
                    IF(V.IDFECHAMENTO > 0,'PREENCHIDO','') AS VALOR2
                    from MYOURO.VENDA V
                    where 
                        TIMESTAMP(V.DATALANC,V.HORATRANSMISSAO) >= (select DTACAO from MYFRONT.PYTHONCONFIG where ID = 1)
                        and V.NUMPREVENDA = '%s' ;
                    ''' %(str(Variaveis.Tc),str(Variaveis.Passo),str(Nro),str(Nro))

        if SeqQuery == 2:
            sSql =  '''
                    CREATE TABLE PYTHONVENDA
                    SELECT
                    V.SEQ,
                    V.DATAHORA,
                    V.CODCAIXA AS TC,
                    '0' AS PASSO,
                    'FECHAMENTO DE CAIXA' AS ACAO,
                    V.NUMPREVENDA,
                    V.IDVENDA,
                    V.TABELA,
                    V.CAMPO,
                    V.VALOR,
                    V.CAMPO2,
                    V.VALOR2
                    FROM
                        (
                            SELECT 
                                '01' AS  SEQ,
                                TIMESTAMP(V.DATALANC,V.HORALANC) AS DATAHORA,
                                V.NUMPREVENDA,
                                V.IDVENDA,
                                V.CODCAIXA,
                                'VENDA' AS TABELA,
                                'CODCAIXA' AS CAMPO, 
                                IF(V.CODCAIXA > 0,'PREENCHIDO','') AS VALOR,
                                'IDFECHAMENTO' AS CAMPO2, 
                                IF(V.IDFECHAMENTO > 0,'PREENCHIDO','') AS VALOR2
                            FROM MYOURO.VENDA V
                                WHERE 
                            V.DATALANC >=   DATE('%s') 
                        ) V
                        WHERE V.NUMPREVENDA = '%s'
                        GROUP BY V.IDVENDA;
    
                    ''' %(str(Variaveis.Datahora),str(Nro))

        if SeqQuery == 3:
            sSql = '''
                    CREATE TABLE PYTHONVENDA
                    SELECT
                    V.SEQ,
                    V.DATAHORA,
                    '%s' AS TC,
                    '%s' AS PASSO,
                    'BAIXA PREVENDA' AS ACAO,
                    V.NUMPREVENDA,
                    V.IDVENDA,
                    V.TABELA,
                    V.CAMPO,
                    V.VALOR,
                    V.CAMPO2,
                    V.VALOR2
                    FROM
                        (
                            SELECT 
                                '01' AS  SEQ,
                                TIMESTAMP(V.DATALANC,V.HORALANC) AS DATAHORA,
                                V.NUMPREVENDA,
                                V.IDVENDA,
                                V.CODCAIXA,
                                'VENDA' AS TABELA,
                                'CODCAIXA' AS CAMPO, 
                                IF(V.CODCAIXA > 0,'PREENCHIDO','') AS VALOR,
                                'IDFECHAMENTO' AS CAMPO2, 
                                IF(V.IDFECHAMENTO > 0,'PREENCHIDO','') AS VALOR2
                            FROM MYOURO.VENDA V
                                WHERE 
                            V.DATALANC >=   DATE('%s') 
                        ) V
                        WHERE V.NUMPREVENDA = '%s'
                        GROUP BY V.IDVENDA;

                    ''' % (str(Variaveis.Tc),str(Variaveis.Passo),str(Variaveis.Datahora), str(Nro))

        if SeqQuery == 4:
            sSql = '''
                     CREATE TABLE PYTHONVENDA
                     SELECT
                     V.SEQ,
                     V.DATAHORA,
                     '%s' AS TC,
                     '%s' AS PASSO,
                     '%s' AS ACAO,
                     V.NUMPREVENDA,
                     V.IDVENDA,
                     V.TABELA,
                     V.CAMPO,
                     V.VALOR,
                     V.CAMPO2,
                     V.VALOR2
                     FROM
                         (
                             SELECT 
                                 '01' AS  SEQ,
                                 TIMESTAMP(V.DATALANC,V.HORALANC) AS DATAHORA,
                                 V.NUMPREVENDA,
                                 V.IDVENDA,
                                 V.CODCAIXA,
                                 'VENDA' AS TABELA,
                                 'CODCAIXA' AS CAMPO, 
                                 IF(V.CODCAIXA > 0,'PREENCHIDO','') AS VALOR,
                                 'IDFECHAMENTO' AS CAMPO2, 
                                 IF(V.IDFECHAMENTO > 0,'PREENCHIDO','') AS VALOR2
                             FROM MYOURO.VENDA V
                                 WHERE 
                             TIMESTAMP(V.DATALANC,V.HORALANC) >=  '%s' 
                         ) V
                         GROUP BY V.IDVENDA;

                     ''' % (str(Variaveis.Tc),str(Variaveis.Passo),str(Variaveis.Texto),str(Variaveis.Datahora))

        log.EscreverLog(sSql)
        FuncoesBD.SqlSlave(sSql)

        sSql = 'ALTER TABLE MYFRONT.PYTHONVENDA ADD INDEX IDVENDA(IDVENDA)'
        log.EscreverLog(sSql)
        FuncoesBD.SqlSlave(sSql)

        sSql =  'DROP TABLE IF EXISTS PYTHONENTREGA;'
        log.EscreverLog(sSql)
        FuncoesBD.SqlSlave(sSql)

        sSql =  '''CREATE TABLE PYTHONENTREGA
                    SELECT
                    '02' AS  SEQ,
                    TIMESTAMP(E.DATAVENDA,E.HORAVENDA) AS DATAHORA,
                    P.TC,
                    P.PASSO,
                    P.ACAO,
                    P.NUMPREVENDA,
                    'ENTREGA' AS TABELA,
                    
                    'CODCAIXA' AS CAMPO,
                    IF(E.CODCAIXA > 0,'PREENCHIDO','') AS VALOR,
                    
                    'IDFECHAMENTO' AS CAMPO2,
                    IF(E.IDFECHAMENTO > 0,'PREENCHIDO','') AS VALOR2,
                    
                    'CODCAIXATROCOSAI' AS CAMPO3,
                    IF(E.CODCAIXATROCOSAI > 0,'PREENCHIDO','') AS VALOR3,
                    
                    'IDFECHAMENTOTROCOPEND' AS CAMPO4,
                    IF(E.IDFECHAMENTOTROCOPEND > 0,'PREENCHIDO','') AS VALOR4,
                    
                    'CODCAIXATROCOENT' AS CAMPO5,
                    IF(E.CODCAIXATROCOENT > 0,'PREENCHIDO','') AS VALOR5
                    
                    FROM  MYOURO.ENTREGAS E
                        INNER JOIN ( 
                                    SELECT
                                    P.IDVENDA,
                                    P.TC,
                                    P.PASSO,
                                    P.ACAO,
                                    P.NUMPREVENDA
                                    FROM 
                                    MYFRONT.PYTHONVENDA P
                                    GROUP BY P.IDVENDA
                                    ) P ON P.IDVENDA = E.IDVENDA;
                '''

        log.EscreverLog(sSql)
        FuncoesBD.SqlSlave(sSql)

        sSql ='DROP TABLE IF EXISTS PYTHONPENDENTES;'
        log.EscreverLog(sSql)
        FuncoesBD.SqlSlave(sSql)

        sSql =  '''CREATE TABLE PYTHONPENDENTES
                SELECT
                '03' AS  SEQ,
                TIMESTAMP(E.DATAHORAVENDA,E.HORAVENDA) AS DATAHORA,
                P.TC,
                P.PASSO,
                P.ACAO,
                P.NUMPREVENDA,
                'PENDENTES' AS TABELA,
                
                'CODCAIXA' AS CAMPO,
                IF(E.CODCAIXA > 0,'PREENCHIDO','') AS VALOR,
                
                'IDFECHAMENTO' AS CAMPO2,
                IF(E.IDFECHAMENTO > 0,'PREENCHIDO','') AS VALOR2
                
                FROM  MYOURO.PENDENTES E
                INNER JOIN ( 
                            SELECT
                            P.IDVENDA,
                            P.TC,
                            P.PASSO,
                            P.ACAO,
                            P.NUMPREVENDA
                            FROM 
                            MYFRONT.PYTHONVENDA P
                            GROUP BY P.IDVENDA
                            ) P ON P.IDVENDA = E.IDVENDA;
    
                '''
        log.EscreverLog(sSql)
        FuncoesBD.SqlSlave(sSql)

        sSql ='DROP TABLE IF EXISTS PYTHONRECEBIMENTOS;'
        log.EscreverLog(sSql)
        FuncoesBD.SqlSlave(sSql)

        sSql =  '''CREATE TABLE PYTHONRECEBIMENTOS
                SELECT
                '04' AS  SEQ,
                TIMESTAMP(E.DATAHORAVENDA,E.HORAVENDA) AS DATAHORA,
                P.TC,
                P.PASSO,
                P.ACAO,
                P.NUMPREVENDA,
                'RECEBIMENTOS' AS TABELA,
                
                'CODCAIXA' AS CAMPO,
                IF(R.CODCAIXA > 0,'PREENCHIDO','') AS VALOR,
                
                
                'IDFECHAMENTO' AS CAMPO2,
                IF(E.IDFECHAMENTO > 0,'PREENCHIDO','') AS VALOR2
                
                FROM  MYOURO.PAGOS E
                INNER JOIN MYOURO.RECEBIMENTO_ORIGEM RO ON RO.IDPAGO = E.IDPAGO
                INNER JOIN MYOURO.RECEBIMENTOS R ON R.IDRECEBIMENTO = RO.IDRECEBIMENTO
                INNER JOIN ( 
                            SELECT
                            P.IDVENDA,
                            P.TC,
                            P.PASSO,
                            P.ACAO,
                            P.NUMPREVENDA
                            FROM 
                            MYFRONT.PYTHONVENDA P
                            GROUP BY P.IDVENDA
                            ) P ON P.IDVENDA = E.IDVENDA;
                
                '''

        log.EscreverLog(sSql)
        FuncoesBD.SqlSlave(sSql)

        sSql ='DROP TABLE IF EXISTS PYTHONPAGOS;'
        log.EscreverLog(sSql)
        FuncoesBD.SqlSlave(sSql)

        sSql =  '''CREATE TABLE PYTHONPAGOS
                SELECT
                '05' AS  SEQ,
                TIMESTAMP(E.DATAHORAVENDA,E.HORAVENDA) AS DATAHORA,
                P.TC,
                P.PASSO,
                P.ACAO,
                P.NUMPREVENDA,
                'PAGOS' AS TABELA,
                
                'CODCAIXA' AS CAMPO,
                IF(E.CODCAIXA > 0,'PREENCHIDO','') AS VALOR,
                
                
                
                'IDFECHAMENTOVENDA' AS CAMPO2,
                IF(E.IDFECHAMENTOVENDA > 0,'PREENCHIDO','') AS VALOR2,
                
                'IDFECHAMENTO' AS CAMPO3,
                IF(E.IDFECHAMENTO > 0,'PREENCHIDO','') AS VALOR3
                
                FROM  MYOURO.PAGOS E
                INNER JOIN ( 
                            SELECT
                            P.IDVENDA,
                            P.TC,
                            P.PASSO,
                            P.ACAO,
                            P.NUMPREVENDA
                            FROM 
                            MYFRONT.PYTHONVENDA P
                            GROUP BY P.IDVENDA
                            ) P ON P.IDVENDA = E.IDVENDA;
                '''
        log.EscreverLog(sSql)
        FuncoesBD.SqlSlave(sSql)

        sSql ='DROP TABLE IF EXISTS PYTHONCREDITOUTILIZACAO;'
        log.EscreverLog(sSql)
        FuncoesBD.SqlSlave(sSql)

        sSql =  '''
                CREATE TABLE PYTHONCREDITOUTILIZACAO
                SELECT
                '06' AS  SEQ,
                TIMESTAMP(E.DATAHORAVENDA,E.HORAVENDA) AS DATAHORA,
                P.TC,
                P.PASSO,
                P.ACAO,
                P.NUMPREVENDA,
                'CREDITOUTILIZACAO' AS TABELA,
                
                'CODCAIXA' AS CAMPO,
                IF(CU.CODCAIXA > 0,'PREENCHIDO','') AS VALOR,
                
                
                'IDFECHAMENTO' AS CAMPO2,
                IF(CU.IDFECHAMENTO > 0,'PREENCHIDO','') AS VALOR2
                
                FROM  MYOURO.PAGOS E
                INNER JOIN MYOURO.CREDITOUTILIZACAO CU ON CU.IDPAGO = E.IDPAGO
                INNER JOIN ( 
                            SELECT
                            P.IDVENDA,
                            P.TC,
                            P.PASSO,
                            P.ACAO,
                            P.NUMPREVENDA
                            FROM 
                            MYFRONT.PYTHONVENDA P
                            GROUP BY P.IDVENDA
                            ) P ON P.IDVENDA = E.IDVENDA;
                '''
        log.EscreverLog(sSql)
        FuncoesBD.SqlSlave(sSql)

        sSql ='DROP TABLE IF EXISTS PYTHONDEVOLUCAO;'
        log.EscreverLog(sSql)
        FuncoesBD.SqlSlave(sSql)

        sSql =  '''
                CREATE TABLE PYTHONDEVOLUCAO
                SELECT
                '07' AS  SEQ,
                TIMESTAMP(E.DATAHORADEVOLUC,E.HORADEVOLUC) AS DATAHORA,
                P.TC,
                P.PASSO,
                P.ACAO,
                P.NUMPREVENDA,
                'DEVOLUCAO' AS TABELA,
                
                'CODCAIXA' AS CAMPO,
                IF(E.CODCAIXA > 0,'PREENCHIDO','') AS VALOR,
                
                
                'IDFECHAMENTO' AS CAMPO2,
                IF(E.IDFECHAMENTO > 0,'PREENCHIDO','') AS VALOR2,
                
                
                'CODCAIXACRED' AS CAMPO3,
                IF(E.CODCAIXACRED > 0,'PREENCHIDO','') AS VALOR3,
                
                
                'IDFECHAMENTOCREDITO' AS CAMPO4,
                IF(E.IDFECHAMENTOCREDITO > 0,'PREENCHIDO','') AS VALOR4
                
                FROM  MYOURO.DEVOLUCAO E
                INNER JOIN MYOURO.VENDAPRODUTOS VP ON VP.IDVENDAPRODUTOS = E.IDVENDAPRODUTOORIGEM
                INNER JOIN ( 
                            SELECT
                            P.IDVENDA,
                            P.TC,
                            P.PASSO,
                            P.ACAO,
                            P.NUMPREVENDA
                            FROM 
                            MYFRONT.PYTHONVENDA P
                            GROUP BY P.IDVENDA
                            ) P ON P.IDVENDA = E.IDVENDA;
                '''
        log.EscreverLog(sSql)
        FuncoesBD.SqlSlave(sSql)

        sSql ='DROP TABLE IF EXISTS PYTHONNOTASDIVACAODEVOL;'
        log.EscreverLog(sSql)
        FuncoesBD.SqlSlave(sSql)

        sSql =  '''CREATE TABLE PYTHONNOTASDIVACAODEVOL
                SELECT
                '08' AS  SEQ,
                TIMESTAMP(D.DATAHORADEVOLUC,D.HORADEVOLUC) AS DATAHORA,
                P.TC,
                P.PASSO,
                P.ACAO,
                P.NUMPREVENDA,
                'PAGOS' AS TABELA,
                
                'CODCAIXA' AS CAMPO,
                IF(E.CODCAIXA > 0,'PREENCHIDO','') AS VALOR,
                
                
                'IDFECHAMENTO' AS CAMPO2,
                IF(E.IDFECHAMENTO > 0,'PREENCHIDO','') AS VALOR2
                
                
                FROM( 
                    SELECT
                        P.*
                    FROM MYFRONT.PYTHONVENDA P
                    GROUP BY P.IDVENDA
                    ) P 
                INNER JOIN MYOURO.VENDAPRODUTOS VP ON P.IDVENDA = VP.IDVENDA
                INNER JOIN MYOURO.DEVOLUCAO D ON VP.IDVENDAPRODUTOS = D.IDVENDAPRODUTOORIGEM 
                INNER JOIN MYOURO.ITENSNOTASDIV I ON I.IDDEVOLUCAO = D.IDDEVOLUCAO 
                INNER JOIN MYOURO.NOTASDIVACAODEVOL E ON  E.IDNOTASDIV = I.IDNOTASDIV;
                '''
        log.EscreverLog(sSql)
        FuncoesBD.SqlSlave(sSql)

        sSql ='DROP TABLE IF EXISTS PYTHONESTORNOS;'
        log.EscreverLog(sSql)
        FuncoesBD.SqlSlave(sSql)
        sSql =  '''CREATE TABLE PYTHONESTORNOS
                SELECT
                '09' AS  SEQ,
                TIMESTAMP(E.DATAVENDA,E.HORAVENDA) AS DATAHORA,
                P.TC,
                P.PASSO,
                P.ACAO,
                P.NUMPREVENDA,
                'ENTREGA' AS TABELA,
                
                'CODCAIXA' AS CAMPO,
                IF(E.CODCAIXA > 0,'PREENCHIDO','') AS VALOR,
                
                'IDFECHAMENTO' AS CAMPO2,
                IF(E.IDFECHAMENTO > 0,'PREENCHIDO','') AS VALOR2
                
                FROM  MYOURO.ESTORNOS E
                INNER JOIN ( 
                            SELECT
                            P.IDVENDA,
                            P.TC,
                            P.PASSO,
                            P.ACAO,
                            P.NUMPREVENDA
                            FROM 
                            MYFRONT.PYTHONVENDA P
                            GROUP BY P.IDVENDA
                            ) P ON P.IDVENDA = E.IDVENDA;
                '''
        log.EscreverLog(sSql)
        FuncoesBD.SqlSlave(sSql)



        sSql = '''INSERT IGNORE INTO PYTHONCONFIG
                    (
                    DTACAO,
                    TC,
                    PASSO,
                    ACAO,
                    NUMPREVENDA,
                    TABELA,
                    CAMPO,
                    VALOR
                    )
                    SELECT
                    P.DATAHORA,
                    P.TC,
                    P.PASSO,
                    P.ACAO,
                    P.NUMPREVENDA,
                    P.TABELA,
                    P.CAMPO,
                    P.VALOR
                    FROM 
                    (
                    SELECT 
                    P.SEQ,
                    P.DATAHORA,
                    P.TC,
                    P.PASSO,
                    P.ACAO,
                    P.NUMPREVENDA,
                    P.TABELA,
                    P.CAMPO,
                    P.VALOR
                    FROM PYTHONVENDA P
                    
                    UNION ALL 
                    
                    SELECT 
                    P.SEQ,
                    P.DATAHORA,
                    P.TC,
                    P.PASSO,
                    P.ACAO,
                    P.NUMPREVENDA,
                    P.TABELA,
                    P.CAMPO2,
                    P.VALOR2
                    FROM PYTHONVENDA P
                    
                    UNION ALL 
                    
                    SELECT 
                    P.SEQ,
                    P.DATAHORA,
                    P.TC,
                    P.PASSO,
                    P.ACAO,
                    P.NUMPREVENDA,
                    P.TABELA,
                    P.CAMPO,
                    P.VALOR
                    FROM PYTHONENTREGA P
                    
                    UNION ALL 
                    
                    SELECT 
                    P.SEQ,
                    P.DATAHORA,
                    P.TC,
                    P.PASSO,
                    P.ACAO,
                    P.NUMPREVENDA,
                    P.TABELA,
                    P.CAMPO2,
                    P.VALOR2
                    FROM PYTHONENTREGA P
                    
                    UNION ALL 
                    
                    SELECT 
                    P.SEQ,
                    P.DATAHORA,
                    P.TC,
                    P.PASSO,
                    P.ACAO,
                    P.NUMPREVENDA,
                    P.TABELA,
                    P.CAMPO3,
                    P.VALOR3
                    FROM PYTHONENTREGA P
                    
                    UNION ALL 
                    
                    SELECT 
                    P.SEQ,
                    P.DATAHORA,
                    P.TC,
                    P.PASSO,
                    P.ACAO,
                    P.NUMPREVENDA,
                    P.TABELA,
                    P.CAMPO4,
                    P.VALOR4
                    FROM PYTHONENTREGA P
                    
                    UNION ALL 
                    
                    SELECT 
                    P.SEQ,
                    P.DATAHORA,
                    P.TC,
                    P.PASSO,
                    P.ACAO,
                    P.NUMPREVENDA,
                    P.TABELA,
                    P.CAMPO5,
                    P.VALOR5
                    FROM PYTHONENTREGA P
                    
                    UNION ALL
                    
                    SELECT 
                    P.SEQ,
                    P.DATAHORA,
                    P.TC,
                    P.PASSO,
                    P.ACAO,
                    P.NUMPREVENDA,
                    P.TABELA,
                    P.CAMPO,
                    P.VALOR
                    FROM PYTHONPENDENTES P
                    
                    UNION ALL 
                    
                    SELECT 
                    P.SEQ,
                    P.DATAHORA,
                    P.TC,
                    P.PASSO,
                    P.ACAO,
                    P.NUMPREVENDA,
                    P.TABELA,
                    P.CAMPO2,
                    P.VALOR2
                    FROM PYTHONPENDENTES P
                    
                    UNION ALL 
                    
                    SELECT 
                    P.SEQ,
                    P.DATAHORA,
                    P.TC,
                    P.PASSO,
                    P.ACAO,
                    P.NUMPREVENDA,
                    P.TABELA,
                    P.CAMPO,
                    P.VALOR
                    FROM PYTHONRECEBIMENTOS P
                    
                    UNION ALL 
                    
                    SELECT 
                    P.SEQ,
                    P.DATAHORA,
                    P.TC,
                    P.PASSO,
                    P.ACAO,
                    P.NUMPREVENDA,
                    P.TABELA,
                    P.CAMPO2,
                    P.VALOR2
                    FROM PYTHONRECEBIMENTOS P
                    
                    UNION ALL 
                    
                    SELECT 
                    P.SEQ,
                    P.DATAHORA,
                    P.TC,
                    P.PASSO,
                    P.ACAO,
                    P.NUMPREVENDA,
                    P.TABELA,
                    P.CAMPO,
                    P.VALOR
                    FROM PYTHONPAGOS P
                    
                    UNION ALL 
                    
                    SELECT 
                    P.SEQ,
                    P.DATAHORA,
                    P.TC,
                    P.PASSO,
                    P.ACAO,
                    P.NUMPREVENDA,
                    P.TABELA,
                    P.CAMPO2,
                    P.VALOR2
                    FROM PYTHONPAGOS P
                    
                    UNION ALL 
                    
                    SELECT 
                    P.SEQ,
                    P.DATAHORA,
                    P.TC,
                    P.PASSO,
                    P.ACAO,
                    P.NUMPREVENDA,
                    P.TABELA,
                    P.CAMPO3,
                    P.VALOR3
                    FROM PYTHONPAGOS P
                    
                    UNION ALL 
                    
                    SELECT 
                    P.SEQ,
                    P.DATAHORA,
                    P.TC,
                    P.PASSO,
                    P.ACAO,
                    P.NUMPREVENDA,
                    P.TABELA,
                    P.CAMPO,
                    P.VALOR
                    FROM PYTHONCREDITOUTILIZACAO P
                    
                    UNION ALL 
                    
                    SELECT 
                    P.SEQ,
                    P.DATAHORA,
                    P.TC,
                    P.PASSO,
                    P.ACAO,
                    P.NUMPREVENDA,
                    P.TABELA,
                    P.CAMPO2,
                    P.VALOR2
                    FROM PYTHONCREDITOUTILIZACAO P
                    
                    UNION ALL 
                    
                    SELECT 
                    P.SEQ,
                    P.DATAHORA,
                    P.TC,
                    P.PASSO,
                    P.ACAO,
                    P.NUMPREVENDA,
                    P.TABELA,
                    P.CAMPO,
                    P.VALOR
                    FROM PYTHONDEVOLUCAO P
                    
                    UNION ALL 
                    
                    SELECT 
                    P.SEQ,
                    P.DATAHORA,
                    P.TC,
                    P.PASSO,
                    P.ACAO,
                    P.NUMPREVENDA,
                    P.TABELA,
                    P.CAMPO2,
                    P.VALOR2
                    FROM PYTHONDEVOLUCAO P
                    
                    UNION ALL 
                    
                    SELECT 
                    P.SEQ,
                    P.DATAHORA,
                    P.TC,
                    P.PASSO,
                    P.ACAO,
                    P.NUMPREVENDA,
                    P.TABELA,
                    P.CAMPO3,
                    P.VALOR3
                    FROM PYTHONDEVOLUCAO P
                    
                    UNION ALL 
                    
                    SELECT 
                    P.SEQ,
                    P.DATAHORA,
                    P.TC,
                    P.PASSO,
                    P.ACAO,
                    P.NUMPREVENDA,
                    P.TABELA,
                    P.CAMPO4,
                    P.VALOR4
                    FROM PYTHONDEVOLUCAO P
                    
                    UNION ALL 
                    
                    SELECT 
                    P.SEQ,
                    P.DATAHORA,
                    P.TC,
                    P.PASSO,
                    P.ACAO,
                    P.NUMPREVENDA,
                    P.TABELA,
                    P.CAMPO,
                    P.VALOR
                    FROM PYTHONNOTASDIVACAODEVOL P
                    
                    UNION ALL 
                    
                    SELECT 
                    P.SEQ,
                    P.DATAHORA,
                    P.TC,
                    P.PASSO,
                    P.ACAO,
                    P.NUMPREVENDA,
                    P.TABELA,
                    P.CAMPO2,
                    P.VALOR2
                    FROM PYTHONNOTASDIVACAODEVOL P
                    
                    UNION ALL 
                    
                    SELECT 
                    P.SEQ,
                    P.DATAHORA,
                    P.TC,
                    P.PASSO,
                    P.ACAO,
                    P.NUMPREVENDA,
                    P.TABELA,
                    P.CAMPO,
                    P.VALOR
                    FROM PYTHONESTORNOS P
                    
                    UNION ALL 
                    
                    SELECT 
                    P.SEQ,
                    P.DATAHORA,
                    P.TC,
                    P.PASSO,
                    P.ACAO,
                    P.NUMPREVENDA,
                    P.TABELA,
                    P.CAMPO2,
                    P.VALOR2
                    FROM PYTHONESTORNOS P
                    
                    ) P
                    ORDER BY
                    P.TC,
                    P.PASSO,
                    P.NUMPREVENDA,
                    P.SEQ,
                    P.TABELA,
                    P.DATAHORA,
                    P.CAMPO;
               '''

        log.EscreverLog(sSql)
        FuncoesBD.SqlSlave(sSql)
        log.EscreverLog('Sai SqlApura')