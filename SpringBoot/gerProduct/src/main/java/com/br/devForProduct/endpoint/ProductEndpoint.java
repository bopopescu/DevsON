package com.br.devForProduct.endpoint;

import com.br.devForProduct.model.Product;
import com.br.devForProduct.util.DateUtil;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

import static java.util.Arrays.asList;

@RestController
@RequestMapping("products")
public class ProductEndpoint {
    private final DateUtil dateUtil;

    @Autowired
    public ProductEndpoint(DateUtil dateUtil) {
        this.dateUtil = dateUtil;
    }




    @RequestMapping(method = RequestMethod.GET)

    public List<Product> listAll() {
        return asList(new Product(0), new Product(2));
    }
}
