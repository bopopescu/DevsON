package com.br.devForProduct.gerProduct.model;

import java.util.ArrayList;
import java.util.List;
import java.util.Objects;

import static java.util.Arrays.asList;

public class Product extends AbstractEntity {
    private String descricao;
    private String marca;
    private String numeroPatrimonio;
    public static List<Product> productList;
    static {
        productRepository();
    }

    public Product(String descricao) {
        this.descricao = descricao;
    }


    private static void productRepository(){
        productList = new ArrayList<>(asList(new Product("Dorflex"), new Product("ANADOR")));
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

//    public int getId() {
//        return id;
//    }

    public Product() {
    }


}
