//Brogan Avery
package model;

public class Instructor {
//vars
	private String firstName;
	private String lastName;
	private String email;
	
//constructors
	public Instructor() {
		setFirstName(null);
		setLastName(null);
		setEmail(null);
	}
	
	public Instructor(String firstName, String lastName, String email){
		setFirstName(firstName);
		setLastName(lastName);
		setEmail(email);
	}
	
	public Instructor(String firstName, String lastName){
		setFirstName(firstName);
		setLastName(lastName);
		email = makeEmailAddress(firstName , lastName);
		setEmail(email);
	}
	
//getters
	public String getFirstName() {
		return firstName;
	}
	public String getLastName() {
		return lastName;
	}
	public String getEmail() {
		return email;
	}
	
//setters
	public void setFirstName(String firstName) {
		this.firstName = firstName;
	}
	public void setLastName(String lastName) {
		this.lastName = lastName;
	}
	public void setEmail(String email) {
		this.email = email;
	}

//methods
	@Override
	public String toString() {
		return "Instructor [firstName=" + firstName + ", lastName=" + lastName + ", email=" + email + "]";
	}
	

	public String makeEmailAddress(String firstName , String lastName){
		firstName = firstName.toLowerCase();
		lastName = lastName.toLowerCase();
		String letter = firstName.substring(0,1);
		String email = letter + lastName + "@dmacc.edu"; 
		return email;
	}
	

}
