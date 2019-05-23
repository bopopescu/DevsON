unit Cliente;

interface
type
  TCliente = class
    public
    Nome : String;
    Telefone : String;
    Endereco : String;
    Cidade : String;
    UF : String;
    constructor Create;
    procedure CadastrarClientePOO;
  end;

implementation

{ TCliente }



constructor TCliente.Create;
begin
    UF := 'SP';
end;

{ TCliente }

procedure TCliente.CadastrarClientePOO;
var
  Lista: TStringList;
begin
  Lista := TStringList.Create;
  try
    Lista := TStringList.Create;
    Lista.Add('Nome: ' + Nome);
    Lista.Add('Telefone: ' + Telefone);
    Lista.Add('Endereço: ' + Endereco);
    Lista.Add('Cidade: ' + Cidade);
    Lista.SaveToFile('Cliente.txt');
  finally
    Lista.Free;
  end;
end;

end.
