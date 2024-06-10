package com.testingdevin;

import org.springframework.context.annotation.Configuration;
import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.config.annotation.web.configuration.EnableWebSecurity;
import org.springframework.security.config.annotation.web.configuration.WebSecurityConfigurerAdapter;

@Configuration
@EnableWebSecurity
public class SecurityConfig extends WebSecurityConfigurerAdapter {

    @Override
    protected void configure(HttpSecurity http) throws Exception {
        http
            .authorizeRequests()
                .antMatchers("/oob/**").permitAll() // Allow unauthenticated access to the OOB endpoint
                .antMatchers("/OpenRedirect").permitAll() // Allow unauthenticated access to the OpenRedirect endpoint
                .anyRequest().authenticated()
            .and()
            .csrf().disable(); // Disable CSRF for simplicity
    }
}
