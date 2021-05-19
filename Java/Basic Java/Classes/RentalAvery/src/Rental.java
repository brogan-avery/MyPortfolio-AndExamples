//Brogan Avery
public class Rental {
	private double rentAmount;
	private String address;
	private int bedrooms;
	private int bathrooms;
	private boolean isADAAccessible;
	
//constructors
public Rental() {
	super();
}
public Rental(double rentAmount, String address, int bedrooms, int bathrooms, boolean isADAAccessible) {
	super();
	this.rentAmount = rentAmount;
	this.address = address;
	this.bedrooms = bedrooms;
	this.bathrooms = bathrooms;
	this.isADAAccessible = isADAAccessible;
}
public Rental(double rentAmount, int bedrooms, int bathrooms, boolean isADAAccessible) {
	super();
	this.rentAmount = rentAmount;
	this.bedrooms = bedrooms;
	this.bathrooms = bathrooms;
	this.isADAAccessible = isADAAccessible;
}
//getters
public double getRentAmount() {
	return rentAmount;
}
public String getAddress() {
	return address;
}
public int getBedrooms() {
	return bedrooms;
}
public int getBathrooms() {
	return bathrooms;
}
public boolean isADAAccessible() {
	return isADAAccessible;
}
//setters
public void setRentAmount(double rentAmount) {
	this.rentAmount = rentAmount;
}
public void setAddress(String address) {
	this.address = address;
}
public void setBedrooms(int bedrooms) {
	this.bedrooms = bedrooms;
}
public void setBathrooms(int bathrooms) {
	this.bathrooms = bathrooms;
}
public void setADAAccessible(boolean isADAAccessible) {
	this.isADAAccessible = isADAAccessible;
}
//methods
@Override
public String toString() {
	return "Rental [rentAmount=" + rentAmount + ", address=" + address + ", bedrooms=" + bedrooms + ", bathrooms="
			+ bathrooms + ", isADAAccessible=" + isADAAccessible + "]";
}

}

