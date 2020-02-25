package br.com.devForProduct.awesome.endpoint;

import br.com.devForProduct.awesome.model.Product;
import br.com.devForProduct.awesome.util.DateUtil;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

import static java.util.Arrays.asList;

@RestController
@RequestMapping("product")
public class ProductEndpoint {
    @Autowired
    private DateUtil dateUtil;

    @RequestMapping(method = RequestMethod.GET, path = "/list")

    public List<Product> listAll() {
        return asList(new Product(0), new Product(2));
    }
}
