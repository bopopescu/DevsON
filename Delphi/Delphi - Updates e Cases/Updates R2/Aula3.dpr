program Aula3;

uses
  System.StartUpCopy,
  FMX.Forms,
  Classes in 'Classes.pas' {Form1};

{$R *.res}

begin
  Application.Initialize;
  Application.CreateForm(TForm1, Form1);
  Application.Run;
end.
