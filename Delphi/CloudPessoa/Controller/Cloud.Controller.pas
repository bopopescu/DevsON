unit Cloud.Controller;

interface

uses Cloud.Interfaces,
     DBClient,
     Generics.Collections,
     Cloud.Pessoa,
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
      function IncluirFuncionario(Dados: array of variant): TCloudPessoa;
      procedure CriarCliente(var FListaFuncionarios: TObjectList<TCloudPessoa>);
      function AddCliente(var FListaFuncionarios: TObjectList<TCloudPessoa>) : Boolean;
    published

    end;

implementation

uses
  System.RTTI;
{ TCloudController }

function TCloudController.AddCliente(var FListaFuncionarios: TObjectList<TCloudPessoa>) : Boolean;
begin
   Result := False;
   Application.CreateForm(TCloudPessoaView, CloudPessoaView);
   try
      CloudPessoaView.iId := FListaFuncionarios.Count + 1;

      if CloudPessoaView.ShowModal = mrOk then
      begin
          FListaFuncionarios.Add(IncluirFuncionario(CloudPessoaView.Dados));
          Result := True;
      end;

   finally
      CloudPessoaView.Free;
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

  FListaFuncionarios.Add(IncluirFuncionario(['1', 'Hugo Weaving', 'Solteiro(a)', 'Masculino',
    '3', '22/01/1985']));

  FListaFuncionarios.Add(IncluirFuncionario(['2', 'Sarah Connor', 'Casado(a)', 'Feminino',
    '5', '07/05/1978']));

  FListaFuncionarios.Add(IncluirFuncionario(['3', 'Lara Croft', 'Vi�vo(a)', 'Feminino',
    '9', '18/12/1991']));

  FListaFuncionarios.Add(IncluirFuncionario(['4', 'Martin Riggs', 'Casado(a)', 'Masculino',
    '2', '30/04/1982']));

  FListaFuncionarios.Add(IncluirFuncionario(['5', 'Tony Stark', 'Divorciado(a)', 'Masculino',
    '4', '05/06/1975']));

  FListaFuncionarios.Add(IncluirFuncionario(['6', 'Beatrice Prior', 'Solteiro(a)', 'Feminino',
    '6', '20/07/1993']));

  FListaFuncionarios.Add(IncluirFuncionario(['7', 'John Mcclane', 'Casado(a)', 'Masculino',
    '1', '11/09/1980']));

  FListaFuncionarios.Add(IncluirFuncionario(['8', 'Ellie Sattler', 'Solteiro(a)', 'Feminino',
    '8', '27/10/1995']));
end;

destructor TCloudController.Destroy;
begin

  inherited;
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

function TCloudController.IncluirFuncionario(Dados: array of variant): TCloudPessoa;
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