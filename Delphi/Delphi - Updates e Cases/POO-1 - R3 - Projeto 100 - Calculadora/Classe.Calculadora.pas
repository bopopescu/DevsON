unit Classe.Calculadora;

interface


type
    iCalculadora = interface
      ['{9D5EAAD8-9C87-4A4A-96DD-98B4DDA09977}']
       // CTRL+SHIHT+C ´para criar a assinatura
       function Operacao(Num1, Num2 : double) : double;
       //herdar de mais de uma classe, usando interface

    end;

    TSoma = class(TInterfacedObject,iCalculadora)
        function Operacao(Num1, Num2 : double) : double;
    end;

    TSubtrair = class(TInterfacedObject,iCalculadora)
        function Operacao(Num1, Num2 : double) : double;
    end;

    TMultiplicar = class(TInterfacedObject,iCalculadora)
        function Operacao(Num1, Num2 : double) : double;
    end;

    TDividir = class(TInterfacedObject,iCalculadora)
        function Operacao(Num1, Num2 : double) : double;
    end;

implementation

uses
  System.SysUtils;

{ TSoma }

function TSoma.Operacao(Num1, Num2: double): double;
begin
     Result := Num1 + Num2;
end;

{ TDividir }

function TDividir.Operacao(Num1, Num2: double): double;
begin
    if Num2<=0  then
       raise Exception.Create('Valor não pode ser dividido por zero');
    Result := Num1 / Num2;
end;

{ TMultiplicar }

function TMultiplicar.Operacao(Num1, Num2: double): double;
begin
    Result := Num1 * Num2;
end;

{ TSubtrair }

function TSubtrair.Operacao(Num1, Num2: double): double;
begin
    Result := Num1 - Num2;
end;

end.
