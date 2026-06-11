package com.sebastian.qa.week2;
public class Greeter {
    public String hello(String name){
        if (name == null || name.isBlank()) {
            throw new IllegalArgumentException("Name cannot be blank");
        }

        return "Hello, " + name;
    }
}
