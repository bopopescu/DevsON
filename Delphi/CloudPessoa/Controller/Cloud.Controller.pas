unit Cloud.Controller;

interface

uses Cloud.Interfaces,
     DBClient,
     Generics.Collections,
     Cloud.Dto.Pessoa,
     Cloud.Dto.Pessoa.Endereco,
     System.SysUtils,
     Cloud.Pessoa.View,
     Vcl.Forms,
     vcl.controls;

  type
    TCloudController = class(TInterfacedObject ,ICloudController)
    private
      constructor Create;
      destructor Destroy; override;
    protected

    public

      class function New : ICloudController;
      procedure PreencherDataSet(var ClientDataSet: TClientDataSet;
                              FListaFuncionarios: TObjectList<TCloudPessoa>);
      function IncluirPessoaNaLista(Dados: array of variant): TCloudPessoa;
      function IncluirEnderenco (Dados: array of variant): TCloudEndereco;
      procedure CriarCliente(var FListaFuncionarios: TObjectList<TCloudPessoa>);
      function AddPessoa(var FListaFuncionarios: TObjectList<TCloudPessoa>) : Boolean;
      function DeletePessoa(var FListaFuncionarios: TObjectList<TCloudPessoa>;iIdDeletar : Integer): Boolean;
      function UpdatePessoa(var FListaFuncionarios: TObjectList<TCloudPessoa>;iIDAtualizar : Integer): Boolean;
      function CadastrarEndereco(var FListaFuncionarios: TObjectList<TCloudPessoa>;iIDAtualizar : Integer): Boolean;
      function EnviarEmail(Pessoa : TCloudPessoa; emailDestino : string): Boolean;
    published

    end;

implementation

uses
  System.RTTI,
  Cloud.Pessoa.Endereco.View,
  Cloud.Model.EnvioEmail;
{ TCloudController }

function TCloudController.AddPessoa(var FListaFuncionarios: TObjectList<TCloudPessoa>) : Boolean;
begin
   Result := False;
   Application.CreateForm(TCloudPessoaView, CloudPessoaView);
   try
      CloudPessoaView.iId := FListaFuncionarios.Count + 1;

      if CloudPessoaView.ShowModal = mrOk then
      begin
          FListaFuncionarios.Add(IncluirPessoaNaLista(CloudPessoaView.Dados));
          Result := True;
      end;

   finally
      CloudPessoaView.Free;
   end;
end;

function TCloudController.CadastrarEndereco(var FListaFuncionarios: TObjectList<TCloudPessoa>; iIDAtualizar: Integer): Boolean;
var
   endTemp : TCloudEndereco;
begin
   Result := False;
   Application.CreateForm(TCloudPessoaEnderecoView, CloudPessoaEnderecoView);
   endTemp := TCloudEndereco.Create;
   try
      CloudPessoaEnderecoView.iIdPessoa := iIDAtualizar;
      CloudPessoaEnderecoView.iId := FListaFuncionarios[iIDAtualizar].Endereco.Count + 1;
      if CloudPessoaEnderecoView.ShowModal = mrOk then
      begin
         endTemp := IncluirEnderenco(CloudPessoaEnderecoView.Dados);
         FListaFuncionarios[iIDAtualizar].Endereco.Add(endTemp);

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
  var FListaFuncionarios: TObjectList<TCloudPessoa>);
begin
     // Cria a lista de objetos
  FListaFuncionarios := TObjectList<TCloudPessoa>.Create;

  FListaFuncionarios.Add(IncluirPessoaNaLista(['1', 'Hugo Weaving', 'Solteiro(a)', 'Masculino',
    '3', '22/01/1985']));

  FListaFuncionarios.Add(IncluirPessoaNaLista(['2', 'Sarah Connor', 'Casado(a)', 'Feminino',
    '5', '07/05/1978']));

  FListaFuncionarios.Add(IncluirPessoaNaLista(['3', 'Lara Croft', 'Vi�vo(a)', 'Feminino',
    '9', '18/12/1991']));

  FListaFuncionarios.Add(IncluirPessoaNaLista(['4', 'Martin Riggs', 'Casado(a)', 'Masculino',
    '2', '30/04/1982']));

  FListaFuncionarios.Add(IncluirPessoaNaLista(['5', 'Tony Stark', 'Divorciado(a)', 'Masculino',
    '4', '05/06/1975']));

  FListaFuncionarios.Add(IncluirPessoaNaLista(['6', 'Beatrice Prior', 'Solteiro(a)', 'Feminino',
    '6', '20/07/1993']));

  FListaFuncionarios.Add(IncluirPessoaNaLista(['7', 'John Mcclane', 'Casado(a)', 'Masculino',
    '1', '11/09/1980']));

  FListaFuncionarios.Add(IncluirPessoaNaLista(['8', 'Ellie Sattler', 'Solteiro(a)', 'Feminino',
    '8', '27/10/1995']));
end;

function TCloudController.DeletePessoa(var FListaFuncionarios: TObjectList<TCloudPessoa>;iIdDeletar : Integer): Boolean;
var
   iContador : Integer;
begin
   for iContador := 0 to Pred(FListaFuncionarios.Count) do
   begin
      if FListaFuncionarios[iContador].ID = iIdDeletar then
      begin
         FListaFuncionarios.Delete(iContador);
         Exit(True);
      end;

   end;
   Result := True;
end;

destructor TCloudController.Destroy;
begin

  inherited;
end;

function TCloudController.EnviarEmail(Pessoa: TCloudPessoa;
  emailDestino: string): Boolean;
begin
   Result := False;
   if (Pessoa <> nil) and (Pessoa.ID > 0) and (emailDestino <> EmptyStr) then
   begin
      Result := TCloudModelEnvioEmail.
                               New.
                               setPessoa(Pessoa).
                               setEmailDestino(emailDestino).
                               &End.
                               EnviarEmail;
   end;
end;

class function TCloudController.New: ICloudController;
begin
   Result := Self.Create;
end;

procedure TCloudController.PreencherDataSet(var ClientDataSet: TClientDataSet;
  FListaFuncionarios: TObjectList<TCloudPessoa>);
var
  Contexto: TRttiContext;
  Tipo: TRttiType;
  PropriedadeNome: TRttiProperty;
  Funcionario: TCloudPessoa;
begin
   ClientDataSet.Close;
   ClientDataSet.CreateDataSet;
   // Cria o contexto do RTTI
   Contexto := TRttiContext.Create;
   try
      // Obt�m as informa��es de RTTI da classe TFuncionario
      Tipo := Contexto.GetType(TCloudPessoa.ClassInfo);

      // Obt�m um objeto referente � propriedade "Nome" da classe TFuncionario
      PropriedadeNome := Tipo.GetProperty('Nome');

      // Percorre a lista de objetos, inserindo o valor da propriedade "Nome" do ClientDataSet
      for Funcionario in FListaFuncionarios do
      ClientDataSet.AppendRecord([PropriedadeNome.GetValue(Funcionario).AsString]);

      ClientDataSet.First;
   finally
      Contexto.Free;
   end;
end;

function TCloudController.UpdatePessoa(var FListaFuncionarios: TObjectList<TCloudPessoa>;iIDAtualizar : Integer): Boolean;
begin
   Result := False;
   Application.CreateForm(TCloudPessoaView, CloudPessoaView);
   try
      CloudPessoaView.iId := iIDAtualizar;
      CloudPessoaView.edtNome.Text := FListaFuncionarios[iIDAtualizar].Nome;
      CloudPessoaView.edtCPF.Text := FListaFuncionarios[iIDAtualizar].cpf;
      CloudPessoaView.edtRG.Text := FListaFuncionarios[iIDAtualizar].Identidade;
      CloudPessoaView.edtTelefone.Text := FListaFuncionarios[iIDAtualizar].Telefone;
      CloudPessoaView.edtEmail.Text := FListaFuncionarios[iIDAtualizar].Email;

      if CloudPessoaView.ShowModal = mrOk then
      begin
         FListaFuncionarios[iIDAtualizar].Nome := CloudPessoaView.edtNome.Text;
         FListaFuncionarios[iIDAtualizar].cpf := CloudPessoaView.edtCPF.Text ;
         FListaFuncionarios[iIDAtualizar].Identidade := CloudPessoaView.edtRG.Text ;
         FListaFuncionarios[iIDAtualizar].Telefone := CloudPessoaView.edtTelefone.Text;
         FListaFuncionarios[iIDAtualizar].Email := CloudPessoaView.edtEmail.Text ;
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
   result.endereco      := Dados[2];
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
