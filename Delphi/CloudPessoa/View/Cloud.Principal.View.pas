unit Cloud.Principal.View;

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
  Cloud.Dto.Pessoa,
  Cloud.Dto.Tabela;

type
  TCloudPrincipalView = class(TForm)
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
    CEP: TStringField;
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
    CampoCep: TEdit;
    Label1: TLabel;
    Panel2: TPanel;
    Label2: TLabel;
    Label3: TLabel;
    btnDelEnd: TButton;
    btnAtuEnd: TButton;
    procedure FormCreate(Sender: TObject);
    procedure CDS_PESSOASAfterScroll(DataSet: TDataSet);
    procedure FormDestroy(Sender: TObject);
    procedure btnAddPessoaClick(Sender: TObject);
    procedure btnDelPessoaClick(Sender: TObject);
    procedure btnAtualizarPessoaClick(Sender: TObject);
    procedure btnCadEnderecoClick(Sender: TObject);
    procedure btnEnvioEmailClick(Sender: TObject);
    procedure CDS_ENDERECOSAfterScroll(DataSet: TDataSet);
    procedure btnDelEndClick(Sender: TObject);
    procedure btnAtuEndClick(Sender: TObject);

  private
    FListaPessoas: TObjectList<TCloudPessoa>;
    procedure PreencherCampos<T : TCloudTabela>(objeto: TCloudTabela);

  end;

var
  CloudPrincipalView: TCloudPrincipalView;

implementation

uses
  System.RTTI, System.TypInfo, Cloud.Dto.Pessoa.Endereco;

{$R *.dfm}

procedure TCloudPrincipalView.btnAddPessoaClick(Sender: TObject);
begin
   if TCloudController.New.AddPessoa(FListaPessoas) then
   begin
      TCloudController.PreencherDataSet<TCloudPessoa>(CDS_PESSOAS,FListaPessoas);
   end;
end;

procedure TCloudPrincipalView.btnDelPessoaClick(Sender: TObject);
begin
   if FListaPessoas[Pred(CDS_PESSOAS.RecNo)].ID > 0 then
   begin
      if TCloudController.New.DeletePessoa(FListaPessoas,Pred(CDS_PESSOAS.RecNo)) then
      begin
         TCloudController.PreencherDataSet<TCloudPessoa>(CDS_PESSOAS,FListaPessoas);
      end;

   end;
end;

procedure TCloudPrincipalView.btnEnvioEmailClick(Sender: TObject);
begin
   if edtEmailDestino.Text = '' then
   begin
      ShowMessage('Por favor insira um e-mail v�lido');
      Exit;
   end;

   if FListaPessoas[Pred(CDS_PESSOAS.RecNo)].ID > 0 then
   begin
      ShowMessage(TCloudController.
                              New.
                              EnviarEmail(FListaPessoas[Pred(CDS_PESSOAS.RecNo)],
                                        edtEmailDestino.Text));

   end;
end;

procedure TCloudPrincipalView.btnDelEndClick(Sender: TObject);
begin
//
end;

procedure TCloudPrincipalView.btnAtuEndClick(Sender: TObject);
begin
 //
end;

procedure TCloudPrincipalView.btnAtualizarPessoaClick(Sender: TObject);
begin
   if TCloudController.New.UpdatePessoa(FListaPessoas,FListaPessoas[Pred(CDS_PESSOAS.RecNo)].ID) then
   begin
      TCloudController.PreencherDataSet<TCloudPessoa>(CDS_PESSOAS,FListaPessoas);
   end;
end;

procedure TCloudPrincipalView.btnCadEnderecoClick(Sender: TObject);
var
   iIdRegistro : Integer;

begin
   iIdRegistro := Pred(CDS_PESSOAS.RecNo);
   if TCloudController.New.CadastrarEndereco(FListaPessoas,iIdRegistro) then
   begin
      TCloudController.PreencherDataSet<TCloudEndereco>(CDS_ENDERECOS,FListaPessoas[iIdRegistro].Endereco,'CEP');
   end;
end;

procedure TCloudPrincipalView.CDS_ENDERECOSAfterScroll(DataSet: TDataSet);
begin
   PreencherCampos<TCloudEndereco>(FListaPessoas[Pred(CDS_PESSOAS.RecNo)].Endereco[Pred(CDS_ENDERECOS.RecNo)]);
end;

procedure TCloudPrincipalView.CDS_PESSOASAfterScroll(DataSet: TDataSet);
begin
  // Chama o m�todo para preencher os controles visuais da tela,
  // informando o objeto posicionado no �ndice "RecNo - 1" do ClientDataSet
  PreencherCampos<TCloudPessoa>(FListaPessoas[Pred(CDS_PESSOAS.RecNo)]);
  PreencherCampos<TCloudEndereco>(FListaPessoas[Pred(CDS_PESSOAS.RecNo)].Endereco[Pred(CDS_ENDERECOS.RecNo)]);
end;

procedure TCloudPrincipalView.FormCreate(Sender: TObject);
begin
   TCloudController.New.CriarCliente(FListaPessoas);

  // Popula o ClientDataSet com o objeto
   TCloudController.PreencherDataSet<TCloudPessoa>(CDS_PESSOAS,FListaPessoas);
end;

procedure TCloudPrincipalView.FormDestroy(Sender: TObject);
begin
  FListaPessoas.Free;
end;

procedure TCloudPrincipalView.PreencherCampos<T>(objeto: TCloudTabela);
var
  Contexto: TRttiContext;
  TipoRtti: TRttiType;
  Propriedade: TRttiProperty;
  Valor: variant;
  Componente: TComponent;
  AuxValue: TValue;
begin
  // Cria o contexto do RTTI
  Contexto := TRttiContext.Create;

  // Obt�m as informa��es de RTTI da classe Gen�rica
   AuxValue := GetTypeData(PTypeInfo(TypeInfo(T)))^.ClassType.Create;
   TipoRtti := Contexto.GetType(AuxValue.AsObject.ClassInfo);
  try
    // Faz uma itera��o nas propriedades do objeto
    for Propriedade in TipoRtti.GetProperties do
    begin
      // Obt�m o valor da propriedade
      Valor := Propriedade.GetValue(objeto).AsVariant;

      // Encontra o componente relacionado, como, por exemplo, "CampoNome"
      Componente := FindComponent('Campo' + Propriedade.Name);

      // Testa se o componente � da classe "TEdit" para acessar a propriedade "Text"
      if Componente is TEdit then
        (Componente as TEdit).Text := Valor;

      // Testa se o componente � da classe "TComboBox" para acessar a propriedade "ItemIndex"
      if Componente is TComboBox then
        (Componente as TComboBox).ItemIndex := (Componente as TComboBox).Items.IndexOf(Valor);

      // Testa se o componente � da classe "TRadioGroup" para acessar a propriedade "ItemIndex"
      if Componente is TRadioGroup then
        (Componente as TRadioGroup).ItemIndex := (Componente as TRadioGroup).Items.IndexOf(Valor);

//      // Testa se o componente � da classe "TCheckBox" para acessar a propriedade "Checked"
      if Componente is TCheckBox then
        (Componente as TCheckBox).Checked := Valor;

      // Testa se o componente � da classe "TTrackBar" para acessar a propriedade "Position"
      if Componente is TTrackBar then
        (Componente as TTrackBar).Position := Valor;

      // Testa se o componente � da classe "TDateTimePicker" para acessar a propriedade "Date"
      if Componente is TDateTimePicker then
        (Componente as TDateTimePicker).Date := Valor;


     // Testa se o componente � da classe "TShape" para acessar a propriedade "Brush.Color"
      if Componente is TShape then
        (Componente as TShape).Brush.Color := Valor;
    end;
  finally
    Contexto.Free;
  end;
end;


end.
