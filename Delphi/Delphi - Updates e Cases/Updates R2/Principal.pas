unit Principal;

interface

uses
  Winapi.Windows, Winapi.Messages, System.SysUtils, System.Variants, System.Classes, Vcl.Graphics,
  Vcl.Controls, Vcl.Forms, Vcl.Dialogs, Cliente, Vcl.StdCtrls;

type
  TForm1 = class(TForm)
    Button1: TButton;
    Button2: TButton;
    procedure Button1Click(Sender: TObject);
    procedure Button2Click(Sender: TObject);
  private
    { Private declarations }
  public
    { Public declarations }
  procedure CadastrarCliente(Nome, Telefone, Endereco, Cidade : String);
  procedure CadastrarClientePOO(Value : TCliente);

  end;

var
  Form1: TForm1;

implementation


{$R *.dfm}

procedure TForm1.Button1Click(Sender: TObject);
begin
    CadastrarCliente('WG','1','2','3');
end;

procedure TForm1.Button2Click(Sender: TObject);
var
  Cliente : TCliente;
begin
  Cliente := TCliente.Create;
  try
    Cliente.Nome := 'Thulio';
    Cliente.Endereco := 'Thulio';
    Cliente.Telefone := 'Thulio';
    Cliente.Cidade := 'Thulio';
    CadastrarClientePOO(Cliente);
  finally
    Cliente.Free;
  end;
end;

procedure TForm1.CadastrarCliente(Nome, Telefone, Endereco, Cidade : String);
var
Lista : TStringList;
begin
try
    Lista := TStringList.Create;
    Lista.Add('Nome: ' + Nome);
    Lista.Add('Telefone: ' + Telefone);
    Lista.Add('Endereço: ' + Endereco);
    Lista.Add('Cidade: ' + Cidade);
    Lista.SaveToFile('Cliente.ini');
finally
    Lista.Free;
end;


end;

procedure TForm1.CadastrarClientePOO(Value : TCliente);
var
Lista : TStringList;
begin
    Lista := TStringList.Create;
    try
    Lista := TStringList.Create;
    Lista.Add('Nome: ' + Value.Nome);
    Lista.Add('Telefone: ' + Value.Telefone);
    Lista.Add('Endereço: ' + Value.Endereco);
    Lista.Add('Cidade: ' + Value.Cidade);
    Lista.SaveToFile('Cliente.txt');
    finally
       Lista.Free;
    end;
end;

end.
