package mainPackage.beans;

import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import lombok.Data;
import lombok.NoArgsConstructor;


import org.springframework.beans.factory.annotation.Autowired;

@Data
@NoArgsConstructor
@Entity
public class Location {
	@Id
	@GeneratedValue(strategy = GenerationType.IDENTITY)
	private long id; //used in repo file!!!
	private int location; //resort area code
	private String phone;    // phone of resort
	private double price;       // all inclusive price for 1 person for 1 week 
	private boolean pets;    // are pets allowed
	@Autowired
	private Excursion excursion;  // one free excursion included in resort price
	
	public Location(int location) {
		super();
		this.location = location;
	}

	public Location(int location, String phone, double price, boolean pets) {
		super();
		this.location = location;
		this.phone = phone;
		this.price = price;
		this.pets = pets;
	}
	public Location(long id, int location, String phone, double price, boolean pets) {
		super();
		this.id = id;
		this.location = location;
		this.phone = phone;
		this.price = price;
		this.pets = pets;
	}
	
}