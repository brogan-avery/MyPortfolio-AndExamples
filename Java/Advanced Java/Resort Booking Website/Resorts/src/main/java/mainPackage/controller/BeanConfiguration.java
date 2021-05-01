package mainPackage.controller;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

import mainPackage.beans.Excursion;
import mainPackage.beans.Location;

@Configuration
public class BeanConfiguration {
	
	@Bean
	public Location contact() {
		Location bean = new Location();
		return bean;
	}

	@Bean
	public Excursion address() {
		Excursion bean = new Excursion();
		return bean;
	}
}
