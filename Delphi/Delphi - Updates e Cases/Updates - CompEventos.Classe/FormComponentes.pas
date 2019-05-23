unit FormComponentes;

interface

uses
  Winapi.Windows, Winapi.Messages,
  System.SysUtils, System.Variants,
   System.Classes, Vcl.Graphics,
  Vcl.Controls, Vcl.Forms,
  Vcl.Dialogs, Principal, Vcl.StdCtrls;

type
  TForm1 = class(TForm)
    Eventos1: TEventos;
    Memo1: TMemo;
    Button1: TButton;
    Edit1: TEdit;
    Label1: TLabel;
    procedure Eventos1Status(Sender: TObject);
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
begin
     //Eventos1.TamanhoString(Edit1.Text);
     Label1.Caption := IntToStr(Eventos1.TamanhoString(Edit1.Text));
end;

procedure TForm1.Eventos1Status(Sender: TObject);
begin
      Memo1.Lines.Add(TEventos(Sender).Nome);
end;



end.

