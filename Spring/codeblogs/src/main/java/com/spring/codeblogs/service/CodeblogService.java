package com.spring.codeblogs.service;

import com.spring.codeblogs.model.Post;
import org.springframework.beans.factory.annotation.Autowired;

import java.util.List;

public class CodeblogService implements CodeblogServiceInterface {
    //Ponto de Injeção do Repository
    @Autowired

    @Override
    public List<Post> findAll() {
        return null;
    }

    @Override
    public Post findById(long id) {
        return null;
    }

    @Override
    public Post save(Post post) {
        return null;
    }
}
