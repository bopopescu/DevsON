package com.br.devForProduct.gerProduct.endpoint;

import com.br.devForProduct.gerProduct.error.CustomErrorType;
import com.br.devForProduct.gerProduct.model.Product;
import com.br.devForProduct.gerProduct.repository.ProductRepository;
import com.br.devForProduct.gerProduct.util.DateUtil;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("products")
public class ProductEndpoint {
    private final ProductRepository productDao;
    @Autowired
    public ProductEndpoint(ProductRepository productDao) {
        this.productDao = productDao;
    }

    @GetMapping
    public ResponseEntity<?> listAll() {
        return new ResponseEntity<>(productDao.findAll(), HttpStatus.OK);
    }

    @GetMapping(path = "/{id}")
    public ResponseEntity<?> getProductById(@PathVariable("id") Long id) {
        Product product = productDao.findOne(id);
        if(product == null)
            return new ResponseEntity<>(new CustomErrorType("Produto Não Encontrado"), HttpStatus.NOT_FOUND);
        return new ResponseEntity<>(product,HttpStatus.OK);
    }

    @PostMapping
    public ResponseEntity<?> save(@RequestBody Product product) {
        return new ResponseEntity<>(productDao.save(product),HttpStatus.CREATED);
    }

    @DeleteMapping(path = "admin/products/{id}")
    public ResponseEntity<?> delete(@PathVariable Long id) {
        productDao.delete(id);
        return new ResponseEntity<>(HttpStatus.OK);
    }

    @PutMapping
    public ResponseEntity<?> update(@RequestBody Product product) {
        productDao.save(product);
        return new ResponseEntity<>(HttpStatus.OK);
    }
}
