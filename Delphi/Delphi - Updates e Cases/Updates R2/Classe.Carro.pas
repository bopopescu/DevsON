unit Classe.Carro;

interface
  type
  TCarro = class
    type
      TRoda = class
      public
        Tipo : String;
        Tamanho : String;
      end;
    private
        Marca : String;
        Modelo : String;
        Roda : TRoda;
        procedure MontarCarro;


  end;
implementation
  procedure TCarro.MontarCarro;
  begin
  Marca := 'Hibrida';
  Modelo := 'Toyota';
  Roda.Tipo := 'Liga Natural';
  Roda.Tamanho := '13';
  end;

end.
