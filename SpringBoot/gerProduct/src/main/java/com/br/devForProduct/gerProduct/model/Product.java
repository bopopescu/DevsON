package com.br.devForProduct.gerProduct.model;

import javax.persistence.Entity;

@Entity
public class Product extends AbstractEntity {
    private String descricao;
    private String marca;
    private String numeroPatrimonio;

    public Product(String descricao) {
        this.descricao = descricao;
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

    public Product() {
    }


}
