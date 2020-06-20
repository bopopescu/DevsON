program ProjCloudPessoas;

uses
  Vcl.Forms,
  uFormulario in 'uFormulario.pas' {fFormulario},
  Cloud.Controller in 'Controller\Cloud.Controller.pas',
  Cloud.Interfaces in 'Controller\Cloud.Interfaces.pas',
  Cloud.Pessoa.Endereco.View in 'View\Cloud.Pessoa.Endereco.View.pas' {Form1},
  Cloud.Pessoa.View in 'View\Cloud.Pessoa.View.pas' {CloudPessoaView},
  CloudBuscaCEP in 'Componentes\CloudBuscaCEP.pas',
  Cloud.Dto.Pessoa.Endereco in 'DTO\Cloud.Dto.Pessoa.Endereco.pas',
  Cloud.Dto.Pessoa in 'DTO\Cloud.Dto.Pessoa.pas',
  Cloud.Model.EnvioEmail in 'Model\Cloud.Model.EnvioEmail.pas',
  CloudServiceEmail in 'Componentes\CloudServiceEmail.pas',
  CloudServiceXML in 'Componentes\CloudServiceXML.pas',
  Cloud.Dto.Email in 'DTO\Cloud.Dto.Email.pas',
  Cloud.Model.Pessoa in 'Model\Cloud.Model.Pessoa.pas',
  Cloud.Dto.Tabela in 'DTO\Cloud.Dto.Tabela.pas';

{$R *.res}

begin
  Application.Initialize;
  Application.MainFormOnTaskbar := True;
  Application.CreateForm(TfFormulario, fFormulario);
  Application.Run;
end.
