unit Mascaras;

interface

uses
  Winapi.Windows, Winapi.Messages, System.SysUtils, System.Variants, System.Classes, Vcl.Graphics,
  Vcl.Controls, Vcl.Forms, Vcl.Dialogs, Vcl.StdCtrls, Vcl.Mask;

type
  TForm1 = class(TForm)
    Button1: TButton;
    Edit1: TEdit;
    MaskEdit1: TMaskEdit;
    MaskEdit2: TMaskEdit;
    Button2: TButton;
    MaskEdit3: TMaskEdit;
    RadioButton1: TRadioButton;
    RadioButton2: TRadioButton;
    procedure Button1Click(Sender: TObject);
  private
    { Private declarations }
  public
    { Public declarations }
  end;

var
  Form1: TForm1;

implementation

{$R *.dfm}

procedure TForm1.Button1Click(Sender: TObject);
var
  Valor : Currency;
begin
   Valor := StrToCurr(Edit1.Text);
   // Edit1.Text := FormatCurr('00.000', Valor);
   Edit1.Text := FormatCurr('#,##0.000', Valor);
end;

end.
