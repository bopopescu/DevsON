unit UN_PRINCIPAL;

interface

uses
  Winapi.Windows, Winapi.Messages, System.SysUtils, System.Variants,
  System.Classes, Vcl.Graphics,
  Vcl.Controls, Vcl.Forms, Vcl.Dialogs, Vcl.Menus, UN_PRODUTOS, Vcl.StdCtrls,
  Vcl.ComCtrls, Vcl.ExtCtrls, UN_CATEGORIAS,
  UN_MANUTENCAO_PRODUTOS,
  UN_USUARIOS, UN_REL_PRODUTOS, Vcl.CategoryButtons, Vcl.WinXCtrls,
  Vcl.Imaging.pngimage, System.ImageList, Vcl.ImgList, Vcl.Imaging.jpeg;

type
  TFRM_PRINCIPAL = class(TForm)
    MainMenu1: TMainMenu;
    Cadastrar1: TMenuItem;
    Produtos1: TMenuItem;
    StatusBar1: TStatusBar;
    Timer1: TTimer;
    Categorias1: TMenuItem;
    Usurios1: TMenuItem;
    Gerencial1: TMenuItem;
    ManutenoemProdutos1: TMenuItem;
    Relatrios1: TMenuItem;
    RelatriodeProdutos1: TMenuItem;
    Sistema1: TMenuItem;
    Sair1: TMenuItem;
    Panel1: TPanel;
    Image3: TImage;

    procedure Produtos1Click(Sender: TObject);
    procedure Timer1Timer(Sender: TObject);
    procedure Sair1Click(Sender: TObject);
    procedure Categorias1Click(Sender: TObject);
    procedure Usurios1Click(Sender: TObject);
    procedure ManutenoemProdutos1Click(Sender: TObject);
    procedure RelatriodeProdutos1Click(Sender: TObject);
    procedure CategoryButtons2Categories0Items0Click(Sender: TObject);
  private
    { Private declarations }
  public
    procedure AbrirProdutos;
    procedure AbrirCategorias;
    procedure AbrirUsuarios;
    procedure AbrirManutencaoProdutos;
    procedure AbrirRelatorio;

  end;

var
  FRM_PRINCIPAL: TFRM_PRINCIPAL;

implementation

{$R *.dfm}

procedure TFRM_PRINCIPAL.AbrirCategorias;

begin
  Application.CreateForm(TFRM_CATEGORIAS, FRM_CATEGORIAS);
  try
    FRM_CATEGORIAS.ShowModal;
  finally
    FRM_CATEGORIAS.Release;

  end;
end;

procedure TFRM_PRINCIPAL.AbrirManutencaoProdutos;

begin
  FRM_MANUTENCAO_PRODUTOS := TFRM_MANUTENCAO_PRODUTOS.Create(Self);
  try
    FRM_MANUTENCAO_PRODUTOS.ShowModal;
  finally
    FreeAndNil(FRM_MANUTENCAO_PRODUTOS);
  end;
end;

procedure TFRM_PRINCIPAL.AbrirProdutos;

begin
  FRM_PRODUTOS := TFRM_PRODUTOS.Create(Self);
  try
    FRM_PRODUTOS.ShowModal;
  finally
    FreeAndNil(FRM_PRODUTOS);
  end;
end;

procedure TFRM_PRINCIPAL.AbrirRelatorio;

begin
  FRM_REL_PRODUTOS := TFRM_REL_PRODUTOS.Create(Self);
  try
    // FRM_REL_PRODUTOS.RLReport1.Preview();
    FRM_REL_PRODUTOS.ShowModal;
  finally
    FreeAndNil(FRM_REL_PRODUTOS);
  end;
end;

procedure TFRM_PRINCIPAL.AbrirUsuarios;

begin
  FRM_USUARIOS := TFRM_USUARIOS.Create(Self);
  try
    FRM_USUARIOS.ShowModal;
  finally
    FreeAndNil(FRM_USUARIOS);
  end;
end;

procedure TFRM_PRINCIPAL.Categorias1Click(Sender: TObject);
begin
  AbrirCategorias;
end;

procedure TFRM_PRINCIPAL.CategoryButtons2Categories0Items0Click
  (Sender: TObject);
begin
  Close;
end;

procedure TFRM_PRINCIPAL.ManutenoemProdutos1Click(Sender: TObject);
begin
  AbrirManutencaoProdutos;
end;

procedure TFRM_PRINCIPAL.Produtos1Click(Sender: TObject);
begin
  AbrirProdutos;
end;

procedure TFRM_PRINCIPAL.RelatriodeProdutos1Click(Sender: TObject);
begin
  AbrirRelatorio;
end;

procedure TFRM_PRINCIPAL.Sair1Click(Sender: TObject);
begin
  Close;
end;

procedure TFRM_PRINCIPAL.Timer1Timer(Sender: TObject);
begin

  StatusBar1.Panels[3].Text := FormatDateTime('dddd , dd " de " mmmm "de" yyyy', Now);
  StatusBar1.Panels[4].Text := 'Hora: ' + FormatDateTime('hh:mm:ss', Now);
end;

procedure TFRM_PRINCIPAL.Usurios1Click(Sender: TObject);
begin
  AbrirUsuarios;
end;

end.
