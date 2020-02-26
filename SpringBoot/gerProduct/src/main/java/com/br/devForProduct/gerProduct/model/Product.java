package com.br.devForProduct.gerProduct.model;

import java.util.ArrayList;
import java.util.List;
import java.util.Objects;

import static java.util.Arrays.asList;

public class Product {
    private int id;
    private String descricao;
    private String marca;
    private String numeroPatrimonio;
    public static List<Product> productList;
    static {
        productRepository();
    }


    public Product(int id, String descricao) {
        this.descricao = descricao;
        this.id = id;
    }

    public Product(int id) {
        this.id = id;
    }

    private static void productRepository(){
        productList = new ArrayList<>(asList(new Product(1,"Dorflex"), new Product(2,"ANADOR")));
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Product product = (Product) o;
        return id == product.id;
    }

    @Override
    public int hashCode() {
        return Objects.hash(id);
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
