//Brogan Avery
package model;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.Table;

@Entity
@Table(name="dogs")
public class DogEntry {
	@Id
	@GeneratedValue(strategy=GenerationType.IDENTITY)
	@Column(name="ID")
	private int id;
	
	@Column(name="breed")
	private String breed;
	
	@Column(name="name")
	private String name;
	
	@Column(name="age")
	private int age;
	
	
//constructors
	public DogEntry(){
		super();
	}
	
	public DogEntry(String breed, String name, int age){
		this.breed = breed;
		this.name = name;
		this.age = age;
	}
	
//getters

	public int getId() {
		return id;
	}

	public String getBreed() {
		return breed;
	}

	public int getAge() {
		return age;
	}
	
	public String getName() {
		return name;
	}

//setters
	public void setId(int id) {
		this.id = id;
	}

	public void setBreed(String breed) {
		this.breed = breed;
	}

	public void setName(String name) {
		this.name = name;
	}
	
	public void setAge(int age) {
		this.age = age;
	}
	
//otra methods
	public String returnDogEntryDetails(){
		return name + ": "	+ "breed- " + breed + ", age- "  + age;
	}
	
}

