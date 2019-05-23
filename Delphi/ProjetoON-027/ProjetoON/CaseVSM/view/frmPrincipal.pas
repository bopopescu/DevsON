unit frmPrincipal;
//
interface

uses
  Winapi.Windows, Winapi.Messages, System.SysUtils, System.Variants,
  System.Classes, Vcl.Graphics, buscacep,
  Vcl.Controls, Vcl.Forms, Vcl.Dialogs, Data.DB, Data.FMTBcd, Data.SqlExpr,
  Vcl.Grids, Vcl.DBGrids, Vcl.StdCtrls, Data.DBXMySQL, Vcl.ExtCtrls,
  Vcl.DBCtrls, Datasnap.DBClient, Datasnap.Provider, Vcl.ComCtrls,
  frmDataModulo, uEndereco, ConfirmarExclusao,  Data_Relatorios,
  Vcl.Mask, Vcl.Buttons, frxClass,
  Cliente;
// frxClass;

type
  TCaseVSM = class(TForm)

    grdDados: TDBGrid;
    grdEndcli: TDBGrid;
    grdTelcli: TDBGrid;
    Listagem: TTabSheet;
    Manutencao: TTabSheet;
    Sistema: TTabSheet;
    PageControl1: TPageControl;
    Panel1: TPanel;
    btnInsereEnd: TButton;
    btnDeleteEndereco: TButton;
    btnInsereFone: TButton;
    btnDeleteFone: TButton;
    btnSalvar: TButton;
    btnCancelar: TButton;
    btnNovaSenha: TButton;
    edtSenhaNova: TEdit;
    edtSenhaConfirmar: TEdit;

    dtClientes: TDataSource;
    dtEndcli: TDataSource;
    dtTelcli: TDataSource;
    btnExcluir: TBitBtn;
    RG: TStaticText;
    Nome: TStaticText;
    StaticText1: TStaticText;
    StaticText2: TStaticText;
    StaticText6: TStaticText;
    btnSair: TBitBtn;
    BitIncluir: TBitBtn;
    btnEditar: TBitBtn;
    edtNome: TDBEdit;
    edtRG: TDBEdit;
    DBRadioGroup1: TDBRadioGroup;
    Senha: TStaticText;
    edtUsuario: TEdit;
    edtSenhaAtual: TEdit;
    StaticText7: TStaticText;
    StaticText8: TStaticText;
    btnReport: TBitBtn;
    RadioGroup1: TRadioGroup;
    edtCPF: TDBEdit;
    edtCNPJ: TDBEdit;
    Button1: TButton;
    // frxReport1: TfrxReport;

    procedure btnExcluirClick(Sender: TObject);
    procedure btnSalvarClick(Sender: TObject);
    procedure btnNovaSenhaClick(Sender: TObject);
    procedure btnSairClick(Sender: TObject);
    procedure FormShow(Sender: TObject);
    procedure btnCancelarClick(Sender: TObject);
    procedure BitIncluirClick(Sender: TObject);
    procedure btnEditarClick(Sender: TObject);
    procedure ManutencaoShow(Sender: TObject);
    procedure btnInsereEndClick(Sender: TObject);
    procedure btnInsereFoneClick(Sender: TObject);
    procedure btnDeleteEnderecoClick(Sender: TObject);
    procedure btnDeleteFoneClick(Sender: TObject);
    procedure FormClose(Sender: TObject; var Action: TCloseAction);
    procedure btnReportClick(Sender: TObject);

    procedure RadioGroup1Click(Sender: TObject);
    procedure edtCPFChange(Sender: TObject);
    procedure Button1Click(Sender: TObject);
    procedure DBRadioGroup1Change(Sender: TObject);
  private
    function loginValido(const usuario, Senha: String): Boolean;
    function ultimoCodcli: Integer;
    { Private declarations }
  public
    { Public declarations }
  end;

var
  CaseVSM: TCaseVSM;
  Cliente: TCliente;
  ultCodcli : Integer;
  ConsultaCep : TForm1;

implementation

{$R *.dfm}
// Listar Clientes na Grid principal

procedure TCaseVSM.BitIncluirClick(Sender: TObject);
begin
  DBRadioGroup1.Value := 'Masculino';
  frmDataModulo.DataModule1.cdsEndcli.close;
  frmDataModulo.DataModule1.cdsEndcli.ParamByName('CODCLIENTE').AsInteger := -1;
  frmDataModulo.DataModule1.cdsEndcli.open;

  frmDataModulo.DataModule1.cdsTelcli.close;
  frmDataModulo.DataModule1.cdsTelcli.ParamByName('CODCLIENTE').AsInteger := -1;
  frmDataModulo.DataModule1.cdsTelcli.open;

  frmDataModulo.DataModule1.cdsClientes.Append;

  PageControl1.ActivePage := Manutencao;
  //edtCPFMask.Text := edtCPF.Text;
  //edtCNPJMask.Text := edtCNPJ.Text;
  // setando na Mascara os valores do banco
end;

procedure TCaseVSM.btnCancelarClick(Sender: TObject);
begin
  frmDataModulo.DataModule1.cdsClientes.Cancel;
  PageControl1.ActivePage := Listagem;
end;

procedure TCaseVSM.btnDeleteEnderecoClick(Sender: TObject);
begin
  frmDataModulo.DataModule1.cdsEndcli.Delete;
  frmDataModulo.DataModule1.cdsEndcli.ApplyUpdates(0);
end;

procedure TCaseVSM.btnDeleteFoneClick(Sender: TObject);
begin
  frmDataModulo.DataModule1.cdsTelcli.Delete;
  frmDataModulo.DataModule1.cdsTelcli.ApplyUpdates(0);
end;

procedure TCaseVSM.btnEditarClick(Sender: TObject);
begin

  frmDataModulo.DataModule1.cdsEndcli.close;
  frmDataModulo.DataModule1.cdsEndcli.ParamByName('CODCLIENTE').AsInteger :=
    frmDataModulo.DataModule1.cdsClientesCODCLI.AsInteger;
  frmDataModulo.DataModule1.cdsEndcli.open;

  frmDataModulo.DataModule1.cdsTelcli.close;
  frmDataModulo.DataModule1.cdsTelcli.ParamByName('CODCLIENTE').AsInteger :=
    frmDataModulo.DataModule1.cdsClientesCODCLI.AsInteger;
  frmDataModulo.DataModule1.cdsTelcli.open;

  frmDataModulo.DataModule1.cdsClientes.Edit;
  PageControl1.ActivePage := Manutencao;


end;

procedure TCaseVSM.btnExcluirClick(Sender: TObject);
begin
  ExcluirCliente.ShowModal;
  ShowMessage('Cliente exclu�do com sucesso');
end;



function TCaseVSM.ultimoCodcli: Integer;
begin

  frmDataModulo.DataModule1.SQL.close;
  frmDataModulo.DataModule1.SQL.open;
  Result := frmDataModulo.DataModule1.SQL.FieldByName('CODCLI').AsInteger;
end;

procedure TCaseVSM.btnInsereEndClick(Sender: TObject);
var
  codCliente: Integer;
begin

  if frmDataModulo.DataModule1.cdsClientesCODCLI.AsString.IsEmpty then
  begin

    if not(frmDataModulo.DataModule1.cdsEndcli.State in dsEditModes) then
    begin
      frmDataModulo.DataModule1.cdsEndcli.close;
      frmDataModulo.DataModule1.cdsEndcli.Params.ParamByName('CODCLIENTE')
        .AsInteger := -1;
      frmDataModulo.DataModule1.cdsEndcli.open;
    end;

    frmDataModulo.DataModule1.cdsEndcli.Append;
  end
  else
  begin

    frmDataModulo.DataModule1.cdsEndcli.Append;
  end;

end;

procedure TCaseVSM.btnInsereFoneClick(Sender: TObject);

var
  codCliente: Integer;
begin
  //codCliente := Cliente.SetPersisteCliente;
  if frmDataModulo.DataModule1.cdsClientesCODCLI.AsString.IsEmpty then
  begin

    if not(frmDataModulo.DataModule1.cdsTelcli.State in dsEditModes) then
    begin
      frmDataModulo.DataModule1.cdsTelcli.close;
      frmDataModulo.DataModule1.cdsTelcli.Params.ParamByName('CODCLIENTE')
        .AsInteger := -1;
      frmDataModulo.DataModule1.cdsTelcli.open;
    end;

    frmDataModulo.DataModule1.cdsTelcli.Append;
  end
  else
  begin

    frmDataModulo.DataModule1.cdsTelcli.Append;
  end;

end;

procedure TCaseVSM.btnSalvarClick(Sender: TObject);
var
  codCliente: Integer;
  registroSelecionado: Integer;
  bInsercao: Boolean;
  // Cliente : TCliente;
begin
  Cliente := TCliente.Create;
  bInsercao := Cliente.StateCliente;
  // Chama da function cliente para checar o status

  // Valida��o dos campos
  begin
    if (edtNome.Text = '') then // Verifica se o campo "Nome" foi preenchido
    begin
      Messagedlg('O campo "Nome Completo" deve ser preenchido!', mtInformation,
        [mbOk], 0);

      if edtNome.CanFocus then
        edtNome.SetFocus;

      Exit;
    end;
    // ***************** VALIDAR COM MASCARAS

    if ((edtCPF.Text = '   .   .   -  ') AND (edtCNPJ.Text = '  .   .   /    -  ')) then // Verifica se o campo "CPF" foi preenchido
    begin
      Messagedlg('O campo "CPF/CNPJ" deve ser preenchido!', mtInformation,
        [mbOk], 0);

      if edtCPF.CanFocus then
        edtCPF.SetFocus;

      Exit;
    end;

    if (edtRG.Text = '') then // Verifica se o campo "RG" foi preenchido
    begin
      Messagedlg('O campo "RG" deve ser preenchido!', mtInformation, [mbOk], 0);

      if edtRG.CanFocus then
        edtRG.SetFocus;

      Exit;
    end;

    if frmDataModulo.DataModule1.cdsClientes.State in dsEditModes then
    begin
      // Alterando e retornando o codigo Cliente para inserir na EndCli e TelCli
       codCliente := Cliente.SetPersisteCliente;
    end;
    // Encapsulado na classe Cliente
    Cliente.SetPersisteEndcli(codCliente);
    Cliente.SetPersisteTelcli(codCliente);

    frmDataModulo.DataModule1.cdsClientes.Refresh;

    if bInsercao then
    begin
      frmDataModulo.DataModule1.cdsClientes.First;
    end;

    PageControl1.ActivePage := Listagem;
  end;
end;

procedure TCaseVSM.Button1Click(Sender: TObject);
var
  // Buscar CEP - IMPLEMENTAR
  TEndereco1: TEndereco;
  CEP: String;
begin
    Application.CreateForm(TForm1, ConsultaCEP);
    try
      ConsultaCEP.ShowModal;
    finally
      ConsultaCEP.Release;
    end;

  // ConsultaCEP.Create;
  //TEndereco1.Create('19803240');
  //ShowMessage(TEndereco1.CEP);
end;

procedure TCaseVSM.DBRadioGroup1Change(Sender: TObject);
begin
     DBRadioGroup1.ItemIndex := 0;
end;

procedure TCaseVSM.edtCPFChange(Sender: TObject);
begin

  // ADO_Cliente.FieldByName('cnpj').AsString := MaskEdit1.Text;

  // muitos utilizam um DBedit e um MaskEdit1

  // fazendo da seguinte forma:

  // DBEdit.Text := MaskEdit1.Text;
end;

procedure TCaseVSM.FormClose(Sender: TObject; var Action: TCloseAction);
begin
  Application.Terminate;
end;

procedure TCaseVSM.FormShow(Sender: TObject);
begin
  frmDataModulo.DataModule1.cdsClientes.close;
  frmDataModulo.DataModule1.cdsClientes.open;
  frmDataModulo.DataModule1.cdsEndcli.close;
  frmDataModulo.DataModule1.cdsEndcli.open;
  frmDataModulo.DataModule1.cdsTelcli.close;
  frmDataModulo.DataModule1.cdsTelcli.open;
  PageControl1.ActivePage := Listagem;
// Fechando e abrindo o Datamodulo para voltar para Listagem

end;

// Validando o campo Senha da aba Sistema

procedure TCaseVSM.btnNovaSenhaClick(Sender: TObject);
begin

  if (edtSenhaNova.Text = '') then // Verifica se o campo "Senha" foi preenchido
  begin
    ShowMessage('O campo "Nova Senha" deve ser preenchido!');

    if edtSenhaNova.CanFocus then
      edtSenhaNova.SetFocus;

    Exit;
  end;
  if (edtSenhaAtual.Text = '') then
  begin
    ShowMessage('O campo "Nova Senha" deve ser preenchido!');

    if edtSenhaAtual.CanFocus then
      edtSenhaAtual.SetFocus;

    Exit;
  end;
  if (edtUsuario.Text = '') then
  begin
    ShowMessage('O campo "Nova Senha" deve ser preenchido!');

    if edtUsuario.CanFocus then
      edtUsuario.SetFocus;

    Exit;
  end;
  if (edtSenhaConfirmar.Text = '') then
  begin
    ShowMessage('O campo "Nova Senha" deve ser preenchido!');

    if edtSenhaConfirmar.CanFocus then
      edtSenhaConfirmar.SetFocus;

    Exit;
  end;
  // Verifica se o login � v�lido
  if loginValido(edtUsuario.Text, edtSenhaAtual.Text) then
  begin

    if edtSenhaNova.Text = edtSenhaConfirmar.Text then
    begin

      frmDataModulo.DataModule1.cdsVendedores.Edit;
      frmDataModulo.DataModule1.cdsVendedoresSENHAVEND.AsString :=
        edtSenhaNova.Text;
      frmDataModulo.DataModule1.cdsVendedores.Post;

      frmDataModulo.DataModule1.cdsVendedores.ApplyUpdates(0);

      ShowMessage('Senha do usu�rio: ' + edtUsuario.Text + ' alteradara!');
      edtSenhaNova.Text := '';
      edtSenhaAtual.Text := '';
      edtUsuario.Text := '';
      edtSenhaConfirmar.Text := '';

    end
    else
    begin

      ShowMessage('Nova senha informada n�o confere');
    end;
  end
  else
  begin
    ShowMessage('Usu�rio ou senha Inv�lido(s)');
  end;
end;

procedure TCaseVSM.btnReportClick(Sender: TObject);
var
    DM_Relatorio: TDM_Relatorio;
begin
      Application.CreateForm(TDM_Relatorio, DM_Relatorio);
    DM_Relatorio.frxR_Clientes.ShowReport();
end;


procedure TCaseVSM.btnSairClick(Sender: TObject);
begin
  close;

end;

// Validar se a Senha esta em branco ou se a senha � valida*** Checar
function TCaseVSM.loginValido(const usuario, Senha: String): Boolean;
begin
  // Caso o componente ConLOGIN n�o esteja conectado ao BD
  frmDataModulo.DataModule1.cdsVendedores.close;
  frmDataModulo.DataModule1.cdsVendedores.ParamByName('nome').AsString :=
    AnsiUpperCase(Trim(usuario));
  // frmDataModulo.DataModule1.cdsClientes.ParamByName('senha').AsString := '');
  frmDataModulo.DataModule1.cdsVendedores.ParamByName('senha').AsString :=
    Trim(Senha);
  frmDataModulo.DataModule1.cdsVendedores.open;

  if not frmDataModulo.DataModule1.cdsVendedores.IsEmpty then
    Result := True;
end;

procedure TCaseVSM.ManutencaoShow(Sender: TObject);
begin

  edtNome.SetFocus;
end;

procedure TCaseVSM.RadioGroup1Click(Sender: TObject);
var
  Valor: Integer;
begin
  Valor := RadioGroup1.ItemIndex;
  // ShowMessage(IntToStr(RadioGroup1.ItemIndex));
  if Valor = 1 then
  begin
    edtCNPJ.Visible := True;
    edtCPF.Visible := false;
    // ShowMessage(BoolToStr(edtCPF.Visible));
    // Visualizando os valores
  end;
  // ShowMessage(IntToStr(RadioGroup1.ItemIndex));
  if Valor = 0 then
  begin
    edtCNPJ.Visible := false;
    edtCPF.Visible := True;
  end;
  //edtCPF.Text := edtCPFMask.Text;
  //edtCNPJ.Text := edtCNPJMask.Text;
  // if rdCNPJ.Action = 'true' then
  // edtCNPJ.Visible=true;
end;

end.
