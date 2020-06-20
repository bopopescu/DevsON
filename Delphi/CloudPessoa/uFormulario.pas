unit uFormulario;

interface

uses
  Winapi.Windows,
  Winapi.Messages,
  System.SysUtils,
  System.Variants,
  System.Classes,
  Vcl.Graphics,
  Vcl.Controls,
  Vcl.Forms,
  Vcl.Dialogs,
  System.Generics.Collections,
  Vcl.StdCtrls,
  Vcl.ExtCtrls,
  Vcl.ComCtrls,
  DBClient,
  Data.DB, Vcl.Grids,
  Vcl.DBGrids,
  Cloud.Controller,
  Cloud.Dto.Pessoa;

type
  TfFormulario = class(TForm)
    CampoID: TEdit;
    CampoNome: TEdit;
    LabelCodigo: TLabel;
    LabelNome: TLabel;
    LabelSenioridade: TLabel;
    LabelDataNascimento: TLabel;
    LabelCorUniforme: TLabel;
    DBGrid1: TDBGrid;
    DS_PESSOAS: TDataSource;
    CDS_PESSOAS: TClientDataSet;
    CDS_PESSOASNome: TStringField;
    dbEnderencos: TDBGrid;
    btnAddPessoa: TButton;
    CampoIdentidade: TEdit;
    CampoCPF: TEdit;
    CampoTelefone: TEdit;
    CampoEmail: TEdit;
    btnDelPessoa: TButton;
    btnAtualizarPessoa: TButton;
    btnCadEndereco: TButton;
    btnEnvioEmail: TButton;
    edtEmailDestino: TEdit;
    pnlTitulo: TPanel;
    lblTitulo: TLabel;
    Panel1: TPanel;
    DS_ENDERECOS: TDataSource;
    CDS_ENDERECOS: TClientDataSet;
    StringField1: TStringField;
    pnlEndereco: TPanel;
    lblBairro: TLabel;
    lblCEP: TLabel;
    lblCidade: TLabel;
    lblComplemento: TLabel;
    lblEstado: TLabel;
    lblLogradouro: TLabel;
    lblNumero: TLabel;
    lblPais: TLabel;
    CampoBairro: TEdit;
    CampoCidade: TEdit;
    CampoComplemento: TEdit;
    CampoEstado: TEdit;
    CampoLogradouro: TEdit;
    CampoNumero: TEdit;
    CampoPais: TEdit;
    edtCep: TEdit;
    procedure FormCreate(Sender: TObject);
    procedure CDS_PESSOASAfterScroll(DataSet: TDataSet);
    procedure FormDestroy(Sender: TObject);
    procedure btnAddPessoaClick(Sender: TObject);
    procedure btnDelPessoaClick(Sender: TObject);
    procedure btnAtualizarPessoaClick(Sender: TObject);
    procedure btnCadEnderecoClick(Sender: TObject);
    procedure btnEnvioEmailClick(Sender: TObject);
    procedure CDS_ENDERECOSAfterScroll(DataSet: TDataSet);
  private
    FListaFuncionarios: TObjectList<TCloudPessoa>;

    procedure PreencherCampos(Funcionario: TCloudPessoa);
  end;

var
  fFormulario: TfFormulario;

implementation

uses
  System.RTTI;

{$R *.dfm}

procedure TfFormulario.btnAddPessoaClick(Sender: TObject);
begin
   if TCloudController.New.AddPessoa(FListaFuncionarios) then
   begin
      TCloudController.PreencherDataSet<TCloudPessoa>(CDS_PESSOAS,FListaFuncionarios);
   end;
end;

procedure TfFormulario.btnDelPessoaClick(Sender: TObject);
begin
   if FListaFuncionarios[Pred(CDS_PESSOAS.RecNo)].ID > 0 then
   begin
      if TCloudController.New.DeletePessoa(FListaFuncionarios,FListaFuncionarios[Pred(CDS_PESSOAS.RecNo)].ID) then
      begin
         TCloudController.PreencherDataSet<TCloudPessoa>(CDS_PESSOAS,FListaFuncionarios);
      end;

   end;
end;

procedure TfFormulario.btnEnvioEmailClick(Sender: TObject);
begin
   if edtEmailDestino.Text = '' then
   begin
      ShowMessage('Por favor insira um e-mail v�lido');
      Exit;
   end;

   if FListaFuncionarios[Pred(CDS_PESSOAS.RecNo)].ID > 0 then
   begin
      ShowMessage(TCloudController.
                              New.
                              EnviarEmail(FListaFuncionarios[Pred(CDS_PESSOAS.RecNo)],
                                        edtEmailDestino.Text));

   end;
end;

procedure TfFormulario.btnAtualizarPessoaClick(Sender: TObject);
begin
   if TCloudController.New.UpdatePessoa(FListaFuncionarios,FListaFuncionarios[Pred(CDS_PESSOAS.RecNo)].ID) then
   begin
      TCloudController.PreencherDataSet<TCloudPessoa>(CDS_PESSOAS,FListaFuncionarios);
   end;
end;

procedure TfFormulario.btnCadEnderecoClick(Sender: TObject);
begin
   if TCloudController.New.CadastrarEndereco(FListaFuncionarios,FListaFuncionarios[Pred(CDS_PESSOAS.RecNo)].ID) then
   begin
      TCloudController.PreencherDataSet<TCloudPessoa>(CDS_PESSOAS,FListaFuncionarios);
   end;
end;

procedure TfFormulario.CDS_ENDERECOSAfterScroll(DataSet: TDataSet);
begin
//
end;

procedure TfFormulario.CDS_PESSOASAfterScroll(DataSet: TDataSet);
begin
  // Chama o m�todo para preencher os controles visuais da tela,
  // informando o objeto posicionado no �ndice "RecNo - 1" do ClientDataSet
  PreencherCampos(FListaFuncionarios[Pred(CDS_PESSOAS.RecNo)]);
end;

procedure TfFormulario.FormCreate(Sender: TObject);
begin
   TCloudController.New.CriarCliente(FListaFuncionarios);

  // Popula o ClientDataSet com os funcion�rios cadastrados
   TCloudController.PreencherDataSet<TCloudPessoa>(CDS_PESSOAS,FListaFuncionarios);
end;

procedure TfFormulario.FormDestroy(Sender: TObject);
begin
  FListaFuncionarios.Free;
end;

procedure TfFormulario.PreencherCampos(Funcionario: TCloudPessoa);
var
  Contexto: TRttiContext;
  Tipo: TRttiType;
  Propriedade: TRttiProperty;
  Valor: variant;
  Componente: TComponent;
begin
  // Cria o contexto do RTTI
  Contexto := TRttiContext.Create;

  // Obt�m as informa��es de RTTI da classe TFuncionario
  Tipo := Contexto.GetType(TCloudPessoa.ClassInfo);

  try
    // Faz uma itera��o nas propriedades do objeto
    for Propriedade in Tipo.GetProperties do
    begin
      // Obt�m o valor da propriedade
      Valor := Propriedade.GetValue(Funcionario).AsVariant;

      // Encontra o componente relacionado, como, por exemplo, "CampoNome"
      Componente := FindComponent('Campo' + Propriedade.Name);

      // (C�digo e nome)
      // Testa se o componente � da classe "TEdit" para acessar a propriedade "Text"
      if Componente is TEdit then
        (Componente as TEdit).Text := Valor;

      // (Estado Civil)
      // Testa se o componente � da classe "TComboBox" para acessar a propriedade "ItemIndex"
      if Componente is TComboBox then
        (Componente as TComboBox).ItemIndex := (Componente as TComboBox).Items.IndexOf(Valor);

      // (Sexo)
      // Testa se o componente � da classe "TRadioGroup" para acessar a propriedade "ItemIndex"
      if Componente is TRadioGroup then
        (Componente as TRadioGroup).ItemIndex := (Componente as TRadioGroup).Items.IndexOf(Valor);

//      // (Plano de Sa�de)
//      // Testa se o componente � da classe "TCheckBox" para acessar a propriedade "Checked"
      if Componente is TCheckBox then
        (Componente as TCheckBox).Checked := Valor;

      // (Senioridade)
      // Testa se o componente � da classe "TTrackBar" para acessar a propriedade "Position"
      if Componente is TTrackBar then
        (Componente as TTrackBar).Position := Valor;

      // (Data de Nascimento)
      // Testa se o componente � da classe "TDateTimePicker" para acessar a propriedade "Date"
      if Componente is TDateTimePicker then
        (Componente as TDateTimePicker).Date := Valor;

//      // (Cor do Uniforme)
//      // Testa se o componente � da classe "TShape" para acessar a propriedade "Brush.Color"
      if Componente is TShape then
        (Componente as TShape).Brush.Color := Valor;
    end;
  finally
    Contexto.Free;
  end;
end;


end.
