package br.com.devForProduct.awesome.model;

public class Product {
    private int id;
    private String descricao;
    private String marca;
    private String numeroPatrimonio;

    public Product(int id) {
        this.id = id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public void setDescricao(String descricao) {
        this.descricao = descricao;
    }

    public void setMarca(String marca) {
        this.marca = marca;
    }

    public void setNumeroPatrimonio(String numeroPatrimonio) {
        this.numeroPatrimonio = numeroPatrimonio;
    }

    public String getDescricao() {
        return descricao;
    }

    public String getMarca() {
        return marca;
    }

    public String getNumeroPatrimonio() {
        return numeroPatrimonio;
    }

    public int getId() {
        return id;
    }

    public Product() {
    }


}
