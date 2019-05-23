unit ClasseCliente;

interface

uses
  System.Classes, Conexao.MySQL, Interfaces;

type
  TClasseAmiga = class  // Caso esteja na mesma Unit, as classes compartilham de objetos privados
    strict private // usado para encapsular dentro da mesma Unit com classes diferentes
      Teste : String;
    public
    procedure TesteSoftware;
  end;

type
  TPessoa = class
    strict private // usado para encapsular dentro da mesma Unit com classes diferentes
    FDataNascimento: TDateTime;
    FDataNascimentoPP: TDateTime;
    FNome2: String; // property criada Get
    FFEndereco : String;
    FTelefone2 : String; //Criado FTelefone, mas não um para o Set separado, ou seja
    // Gerenciando ambos
    // Conexao :  TConexaoMySQL;   Usando Interfaces deixa de usar a conexaoMysql    Aula 16
    Conexao :  IConexao;

    procedure SetDataNascimentoPP(const Value: TDateTime);
    procedure SetNome2(const Value: String);
    function GetEndereco: String;
    procedure SetEndereco(const Value: String); // property criada Set
    public
    Nome: String;
    Telefone: String;
    Endereco : String;
    Cidade: String;
    UF: String;

    //DataNascimento: TDateTime;
    Saldo: Currency;
    //    constructor Create; // Alterado na implentação da Interfaces - Aula 16
    constructor Create(aConexao : IConexao);
    procedure Cadastrar;
    procedure CriarFinanceiro;
    function Idade : Integer;
    procedure SetDataNascimento(aValue : String);
    //property DataNascimentoPP : TDateTime - ctrl+shift+c ele cria o resto
    // read Get - write Set
    property DataNascimentoPP : TDateTime read FDataNascimentoPP write SetDataNascimentoPP;
    property Nome2  :String read FNome2 write SetNome2;
    // Criando na mãe, é possível dar problema
    property Telefone2 :  String read FTelefone2 write FTelefone2;
    // Criando os Gets e Sets na linha abaixo e dando o    ctrl+shift+c  ele vai criar no padrão
    property Endereco2 : String read GetEndereco write SetEndereco;
  end;

implementation

uses
   System.SysUtils;

procedure TPessoa.Cadastrar;
var
Lista : TStringList;
begin
    Lista := TStringList.Create;
    try
      Lista.Add('Nome: ' + Nome);
      Lista.Add('Telefone: ' + Telefone);
      Lista.Add('Nome: ' + Nome);
      Lista.Add('End: ' + Endereco);
      Lista.Add('Cidade: ' + Cidade);
      Lista.Add('UF: ' + UF);
      Lista.SaveToFile(Nome + '_Cliente.txt');

      Conexao.Gravar;
    finally
      Lista.Free;
    end;

end;


constructor TPessoa.Create(aConexao : IConexao);
begin
    // Toda vez que criar a classe, executa o Create      Aula 16
     // Conexao := TConexaoMySQL.Create;

     // Removemido a linha acima na implementação da Interfaces

     // Aula 16 - Fim
     Conexao := aConexao;
     UF := 'SP';
     Saldo := 1000;
end;

procedure TPessoa.CriarFinanceiro;
var
Lista : TStringList;
begin
    Lista := TStringList.Create;
    try
      Lista.Add('Nome: ' + Nome);
      Lista.Add('Saldo: ' + CurrToStr(Saldo));
      Lista.SaveToFile(Nome + '_Financeiro.txt');
    finally
      Lista.Free;
    end;
end;

function TPessoa.GetEndereco: String;
begin
      Result := FFEndereco + 'Teste Apai';
end;

function TPessoa.Idade: Integer;
begin
        Result := Trunc((Now - FDataNascimento) / 365.25) ;
end;

procedure TPessoa.SetDataNascimento(aValue: String);
var
    aClasse : TClasseAmiga;
begin
    //aClasse.Teste;
    // Aqui é possível a função acessando o objeto privado de outra classe

    if not TryStrToDateTime(aValue, FDataNascimento) then
      raise Exception.Create('A Data é Inválida');
    FDataNascimento := StrToDateTime(aValue);

end;

procedure TPessoa.SetDataNascimentoPP(const Value: TDateTime);
begin
  FDataNascimentoPP := Value;
end;

procedure TPessoa.SetEndereco(const Value: String);
begin
     FFEndereco := Value;
end;

procedure TPessoa.SetNome2(const Value: String);
begin
  if Value='' then
  raise Exception.Create('Nome não pode ser vazio');

  FNome2 := Value;
end;

{ TClasseAmiga }

procedure TClasseAmiga.TesteSoftware;
var
      aClasse : TPessoa;
begin
    // aClasse.FDataNascimento;// Objeto privado acessado na classe amiga
end;

end.
