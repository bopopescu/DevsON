package com.br.devForProduct.gerProduct.repository;


import com.br.devForProduct.gerProduct.model.Product;
import org.springframework.data.repository.CrudRepository;
import org.springframework.data.repository.PagingAndSortingRepository;

import java.util.List;

public interface ProductRepository extends PagingAndSortingRepository<Product, Long> {
    List<Product> findByNameIgnoreCaseContaining(String descricao);
}
