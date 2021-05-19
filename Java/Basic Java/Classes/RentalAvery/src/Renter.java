//Brogan Avery
public class Renter {
private String firstName;
private String lastName;
private String phoneNumber;
private String ssn;

public Renter() {
	super();
}


public Renter(String firstName, String lastName, String phoneNumber) {
	super();
	this.firstName = firstName;
	this.lastName = lastName;
	this.phoneNumber = phoneNumber;
}


public String getFirstName() {
	return firstName;
}
public String getLastName() {
	return lastName;
}
public String getPhoneNumber() {
	return phoneNumber;
}

public String getSsn() {
	return ssn;
}
public void setFirstName(String firstName) {
	this.firstName = firstName;
}
public void setLastName(String lastName) {
	this.lastName = lastName;
}
public void setPhoneNumber(String phoneNumber) {
	this.phoneNumber = phoneNumber;
}
public void setSsn(String ssn) {
	this.ssn = ssn;
}


@Override
public String toString() {
	return "Renter [firstName=" + firstName + ", lastName=" + lastName + ", phoneNumber=" + phoneNumber + ", ssn=" + ssn
			+ "]";
}









}
