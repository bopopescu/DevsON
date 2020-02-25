package br.com.devForProduct.awesome;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.EnableAutoConfiguration;
import org.springframework.context.annotation.ComponentScan;

@EnableAutoConfiguration
@ComponentScan(basePackages = "br.com.devForProduct.awesome.endpoint")
public class AplicationStarter {
    public static void main(String[] args) {
        SpringApplication.run(AplicationStarter.class,args);
    }
}
