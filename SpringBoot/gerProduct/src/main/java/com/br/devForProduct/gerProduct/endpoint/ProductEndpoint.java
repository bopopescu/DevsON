package com.br.devForProduct.gerProduct.endpoint;

import com.br.devForProduct.gerProduct.error.CustomErrorType;
import com.br.devForProduct.gerProduct.model.Product;
import com.br.devForProduct.gerProduct.util.DateUtil;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("products")
public class ProductEndpoint {
    private final DateUtil dateUtil;

    @Autowired
    public ProductEndpoint(DateUtil dateUtil) {
        this.dateUtil = dateUtil;
    }

    @RequestMapping(method = RequestMethod.GET)
    public ResponseEntity<?> listAll() {
        return new ResponseEntity<>(Product.productList, HttpStatus.OK);
    }

    @RequestMapping(method = RequestMethod.GET, path = "/{id}")
    public ResponseEntity<?> getProductById(@PathVariable("id") int id) {
        Product product = new Product();
        product.setId(id);
        int index = Product.productList.indexOf(product);
        if(index == -1)
            return new ResponseEntity<>(new CustomErrorType("Produto Não Encontrado"), HttpStatus.NOT_FOUND);
        return new ResponseEntity<>(Product.productList.get(index),HttpStatus.OK);
    }

    @RequestMapping(method = RequestMethod.POST)
    public ResponseEntity<?> save(@RequestBody Product product) {
        Product.productList.add(product);
        return new ResponseEntity<>(product,HttpStatus.OK);
    }

    @RequestMapping(method = RequestMethod.DELETE)
    public ResponseEntity<?> delete(@RequestBody Product product) {
        Product.productList.remove(product);
        return new ResponseEntity<>(HttpStatus.OK);
    }
}
