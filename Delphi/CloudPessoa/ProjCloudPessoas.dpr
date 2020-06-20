program ProjCloudPessoas;

uses
  Vcl.Forms,
  uFormulario in 'uFormulario.pas' {fFormulario},
  Cloud.Pessoa in 'DTO\Cloud.Pessoa.pas',
  Cloud.Controller in 'Controller\Cloud.Controller.pas',
  Cloud.Interfaces in 'Controller\Cloud.Interfaces.pas',
  Cloud.Pessoa.View in 'View\Cloud.Pessoa.View.pas' {Form1},
  Cloud.Endereco in 'DTO\Cloud.Endereco.pas';

{$R *.res}

begin
  Application.Initialize;
  Application.MainFormOnTaskbar := True;
  Application.CreateForm(TfFormulario, fFormulario);
  Application.Run;
end.
