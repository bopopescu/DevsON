unit Classes;

interface

uses
  System.SysUtils, System.Types, System.UITypes, System.Classes, System.Variants,
  FMX.Types, FMX.Controls, FMX.Forms, FMX.Graphics, FMX.Dialogs,
  FMX.Controls.Presentation, FMX.StdCtrls, FMX.ScrollBox, FMX.Memo;

type
  TConfig = record
    Host : String;
    Path : String;
    Usuario : String;
    Senha : String;
  end;

  TCaneca = class

  end;

  TGarrafa = class
    Cor: String;
    Modelo: String;
    Tampa: String;
    Caneca: TCaneca;
    constructor Create;
    destructor Destroy; override;
    procedure ArmazenaLiquido(Liquido: String);
  end;

  TRoda = class
    Tamanho: Integer;
    Material: String;
   end;

  TMotor = class
    Potencia : Integer;
    Combustivel : String;
  end;

  TCarro = class
    Cor: String;
    Marca: String;
    Modelo : String;
    Roda : TRoda;
    Motor : TMotor;
    constructor Create;
    destructor Destroy; override;
  end;




  TForm1 = class(TForm)
    Button1: TButton;
    Button2: TButton;
    Memo1: TMemo;
    //procedure FormCreate(Sender: TObject);
    procedure Button1Click(Sender: TObject);
    procedure Button2Click(Sender: TObject);
  private
    procedure ExibeMemo(Config: TConfig);
    { Private declarations }
  public
    { Public declarations }
  end;

  TLivro = class
  public
    Titulo: String;
    Autor: String;
    function Paginacao(Pagina: Integer): String;
  end;

  TAutor = class
  public
    Livro: Classes.TLivro;
  end;

  TGibi = class(TLivro)
  end;

var
  Form1: TForm1;

implementation

{$R *.fmx}

function TLivro.Paginacao(Pagina: Integer): String;
begin
end;

procedure TGarrafa.ArmazenaLiquido(Liquido: string);
begin
  //teste;
end;

procedure TForm1.Button1Click(Sender: TObject);
var
  MinhaGarrafa: TGarrafa;
begin
    MinhaGarrafa := nil;
    if Assigned(MinhaGarrafa) then
        ShowMessage('Estou estanciado')
    else
        MinhaGarrafa := TGarrafa.Create;
        ShowMessage('Não Estou estanciado');


  try
      MinhaGarrafa.Modelo := 'Vidro';
      MinhaGarrafa.Cor := 'Vermelha';
  finally
      // MinhaGarrafa.Free;
      FreeAndNil(MinhaGarrafa);// Atribuindo valor nulo a memoria
  end;



end;
// Exemplo de Record
procedure TForm1.Button2Click(Sender: TObject);
  var
  Config : TConfig;
begin
  Config.Host := 'localhost';
  Config.Path := '3306';
  Config.Usuario := 'root';
  Config.Senha := 'drogaria';
  ExibeMemo(Config);
end;

procedure TForm1.ExibeMemo(Config: TConfig);
begin
  Memo1.Lines.Add(Config.Host);
  Memo1.Lines.Add(Config.Path);
  Memo1.Lines.Add(Config.Usuario);
  Memo1.Lines.Add(Config.Senha);
end;

constructor TCarro.Create;
begin
   Roda := TRoda.Create;
   Motor := TMotor.Create;
end;

destructor TCarro.Destroy;
begin
   Motor.Free;
   Roda.Free;
   inherited;
end;

end.
