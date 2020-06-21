unit Cloud.Controller;

interface

uses Cloud.Interfaces,
     Generics.Collections,
     Cloud.Dto.Pessoa,
     Cloud.Dto.Pessoa.Endereco,
     System.SysUtils,
     Cloud.Pessoa.View,
     Vcl.Forms,
     vcl.controls,
     DBClient,
     Cloud.Dto.Tabela;

  type
    TCloudController = class(TInterfacedObject ,ICloudController)
    private
      constructor Create;
      destructor Destroy; override;
    protected

    public
      class function New : ICloudController;
      function IncluirPessoaNaLista(Dados: array of variant): TCloudPessoa;
      function IncluirEnderenco (Dados: array of variant): TCloudEndereco;
      procedure CriarCliente(var FListaPessoas: TObjectList<TCloudPessoa>);
      function AddPessoa(var FListaPessoas: TObjectList<TCloudPessoa>) : Boolean;
      function DeletePessoa(var FListaPessoas: TObjectList<TCloudPessoa>;iIdDeletar : Integer): Boolean;
      function UpdatePessoa(var FListaPessoas: TObjectList<TCloudPessoa>;iIDAtualizar : Integer): Boolean;
      function CadastrarEndereco(var FListaPessoas: TObjectList<TCloudPessoa>; iIDAtualizar: Integer): Boolean;
      function EnviarEmail(Pessoa : TCloudPessoa; emailDestino : string): String;
      class procedure PreencherDataSet<T : TCloudTabela>(var ClientDataSet: TClientDataSet; FLista: TObjectList<T>;sField : string = 'Nome');
    published

    end;

implementation

uses
  Cloud.Pessoa.Endereco.View,
  Cloud.Model.EnvioEmail, Cloud.Model.Pessoa;

  { TCloudController }

function TCloudController.AddPessoa(var FListaPessoas: TObjectList<TCloudPessoa>) : Boolean;
begin
   Result := False;
   Application.CreateForm(TCloudPessoaView, CloudPessoaView);
   try
      CloudPessoaView.iId := FListaPessoas.Count + 1;

      if CloudPessoaView.ShowModal = mrOk then
      begin
          FListaPessoas.Add(IncluirPessoaNaLista(CloudPessoaView.Dados));
          Result := True;
      end;

   finally
      CloudPessoaView.Free;
   end;
end;

function TCloudController.CadastrarEndereco(var FListaPessoas: TObjectList<TCloudPessoa>; iIDAtualizar: Integer): Boolean;
begin
   Result := False;
   Application.CreateForm(TCloudPessoaEnderecoView, CloudPessoaEnderecoView);
   try
      CloudPessoaEnderecoView.iIdPessoa := iIDAtualizar;
      if (FListaPessoas[iIDAtualizar].Endereco <> nil) and (FListaPessoas[iIDAtualizar].Endereco.Count > 0) then
         CloudPessoaEnderecoView.iId := FListaPessoas[iIDAtualizar].Endereco.Count + 1
      else
         CloudPessoaEnderecoView.iId := 1;

      if CloudPessoaEnderecoView.ShowModal = mrOk then
      begin
         FListaPessoas[iIDAtualizar].Endereco.Add(IncluirEnderenco(CloudPessoaEnderecoView.Dados));
         Result := True;
      end;
   finally
      CloudPessoaEnderecoView.Free;
   end;
end;

constructor TCloudController.Create;
begin

end;

procedure TCloudController.CriarCliente(
  var FListaPessoas: TObjectList<TCloudPessoa>);
begin
     // Cria a lista de objetos
  FListaPessoas := TObjectList<TCloudPessoa>.Create;

  FListaPessoas.Add(IncluirPessoaNaLista(['1', 'Hugo Weaving', '4655442115', '042.888.210-29',
    '(18)98806-8389', 'wg.o.costa@gmail.com']));

  FListaPessoas.Add(IncluirPessoaNaLista(['2', 'Sarah Connor', '270622986', '592.482.300-83',
    '(18)98806-8389', 'wg.o.costa@gmail.com']));

  FListaPessoas.Add(IncluirPessoaNaLista(['3', 'Lara Croft', '473309543', '873.041.730-92',
    '(18)98806-8389', 'wg.o.costa@gmail.com']));

  FListaPessoas.Add(IncluirPessoaNaLista(['4', 'Martin Riggs', '163254837', '663.309.170-27',
    '(18)98806-8389', 'chamados.vsm@gmail.com']));

  FListaPessoas.Add(IncluirPessoaNaLista(['5', 'Tony Stark', '492436642', '765.994.940-30',
    '(18)98806-8389', 'wg.o.costa@gmail.com']));

  FListaPessoas.Add(IncluirPessoaNaLista(['6', 'Beatrice Prior', '188516281', '723.685.450-69',
    '(18)98806-8389', 'wg.o.costa@gmail.com']));

  FListaPessoas.Add(IncluirPessoaNaLista(['7', 'John Mcclane', '162520256', '375.524.420-93',
    '(18)98806-8389', 'chamados.vsm@gmail.com']));

  FListaPessoas.Add(IncluirPessoaNaLista(['8', 'Ellie Sattler', '207529085', '888.569.350-40',
    '(18)98806-8389', 'chamados.vsm@gmail.com']));
end;

function TCloudController.DeletePessoa(var FListaPessoas: TObjectList<TCloudPessoa>;iIdDeletar : Integer): Boolean;
var
   iContador : Integer;
begin
   for iContador := 0 to Pred(FListaPessoas.Count) do
   begin
      if FListaPessoas[iContador].ID = iIdDeletar then
      begin
         FListaPessoas.Delete(iContador);
         Exit(True);
      end;

   end;
   Result := True;
end;

destructor TCloudController.Destroy;
begin

  inherited;
end;

function TCloudController.EnviarEmail(Pessoa : TCloudPessoa; emailDestino : string): String;
begin
   Result := '';
   if not TCloudModelPessoa.New.ValidaEmail(emailDestino) then
   begin
      Result := 'Informe um e-mail v�lido';
      Exit;
   end;

   if (Pessoa <> nil) and (Pessoa.ID > 0) and (emailDestino <> EmptyStr) then
   begin
      if TCloudModelEnvioEmail.
                               New.
                               setPessoa(Pessoa).
                               setEmailDestino(emailDestino).
                               &End.
                               EnviarEmail then
         Result := 'E-mail enviado com sucesso para: '+ emailDestino
      else
         Result := 'N�o foi poss�vel Enviar a Mensagem';
   end;
end;

class function TCloudController.New: ICloudController;
begin
   Result := Self.Create;
end;

class procedure TCloudController.PreencherDataSet<T>(var ClientDataSet: TClientDataSet; FLista: TObjectList<T>;sField : string = 'Nome');
begin
   TCloudTabela.PreencherDataSet<T>(ClientDataSet,FLista,sField);
end;

function TCloudController.UpdatePessoa(var FListaPessoas: TObjectList<TCloudPessoa>;iIDAtualizar : Integer): Boolean;
begin
   Result := False;
   Application.CreateForm(TCloudPessoaView, CloudPessoaView);
   try
      CloudPessoaView.iId := iIDAtualizar;
      CloudPessoaView.edtNome.Text     := FListaPessoas[iIDAtualizar].Nome;
      CloudPessoaView.edtCPF.Text      := FListaPessoas[iIDAtualizar].cpf;
      CloudPessoaView.edtRG.Text       := FListaPessoas[iIDAtualizar].Identidade;
      CloudPessoaView.edtTelefone.Text := FListaPessoas[iIDAtualizar].Telefone;
      CloudPessoaView.edtEmail.Text    := FListaPessoas[iIDAtualizar].Email;

      if CloudPessoaView.ShowModal = mrOk then
      begin
         FListaPessoas[iIDAtualizar].Nome       := CloudPessoaView.edtNome.Text;
         FListaPessoas[iIDAtualizar].cpf        := CloudPessoaView.edtCPF.Text ;
         FListaPessoas[iIDAtualizar].Identidade := CloudPessoaView.edtRG.Text ;
         FListaPessoas[iIDAtualizar].Telefone   := CloudPessoaView.edtTelefone.Text;
         FListaPessoas[iIDAtualizar].Email      := CloudPessoaView.edtEmail.Text ;
         Result := True;
      end;

   finally
      CloudPessoaView.Free;
   end;
end;

function TCloudController.IncluirEnderenco(Dados: array of variant): TCloudEndereco;
begin
   result := TCloudEndereco.Create;
   result.ID            := Dados[0];
   result.idPessoa      := Dados[1];
   result.logradouro    := Dados[2];
   result.Cep           := Dados[3];
   result.Numero        := Dados[4];
   result.Complemento   := Dados[5];
   result.Bairro        := Dados[6];
   result.Cidade        := Dados[7];
   result.Estado        := Dados[8];
   result.Pais          := Dados[9];
end;

function TCloudController.IncluirPessoaNaLista(Dados: array of variant): TCloudPessoa;
begin
   result := TCloudPessoa.Create;
   result.id := Dados[0];
   result.Nome := Dados[1];
   result.Identidade := Dados[2];
   result.CPF := Dados[3];
   result.Telefone := Dados[4];
   result.Email := Dados[5];
end;

end.
