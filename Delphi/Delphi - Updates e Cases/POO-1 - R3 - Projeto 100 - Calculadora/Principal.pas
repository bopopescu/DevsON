unit Principal;

interface

uses
  Winapi.Windows, Winapi.Messages, System.SysUtils, System.Variants, System.Classes, Vcl.Graphics,
  Vcl.Controls, Vcl.Forms, Vcl.Dialogs, Vcl.StdCtrls, Classe.Calculadora;

type
  TForm1 = class(TForm)
    Button1: TButton;
    edtValor1: TEdit;
    Label1: TLabel;
    Button2: TButton;
    Button3: TButton;
    Button4: TButton;
    edtValor2: TEdit;
    edtResultado: TEdit;
    procedure Button1Click(Sender: TObject);
    procedure Button2Click(Sender: TObject);
    procedure Button3Click(Sender: TObject);
    procedure Button4Click(Sender: TObject);
  private
    FCalculadora: iCalculadora;
    procedure SetCalculadora(const Value: iCalculadora);
    procedure Operacao; {Só vai saber a operacao quando o botao o chamar}
  public
    { Public declarations }
    property Calculadora : iCalculadora read FCalculadora write SetCalculadora;
  end;

var
  Form1: TForm1;

implementation

{$R *.dfm}


{ TForm1 }

procedure TForm1.Button1Click(Sender: TObject);
begin
    Calculadora := TSoma.Create;
    Operacao;
end;

procedure TForm1.Button2Click(Sender: TObject);
begin
    Calculadora := TSubtrair.Create;
    Operacao;
end;

procedure TForm1.Button3Click(Sender: TObject);
begin
    Calculadora := TDividir.Create;
    Operacao;
end;

procedure TForm1.Button4Click(Sender: TObject);
begin
    Calculadora := TMultiplicar.Create;
    Operacao;
end;

procedure TForm1.Operacao;
begin
    edtResultado.Text := FloatToStr(Calculadora.Operacao(StrToFloat(edtValor1.Text),StrToFloat(edtValor2.Text)));
end;

procedure TForm1.SetCalculadora(const Value: iCalculadora);
begin
  FCalculadora := Value;
end;

end.


