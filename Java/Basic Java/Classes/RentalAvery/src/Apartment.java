//Brogan Avery
public class Apartment extends Rental{
private String unitNumber;
private int parkingSpaces;
private Building building;

//constructors
public Apartment() {
	super();
}

public Apartment(double rentAmount, String address, int bedrooms, int bathrooms, boolean isADAAccessible,
		String unitNumber, int parkingSpaces, Building building) {
	super(rentAmount, address, bedrooms, bathrooms, isADAAccessible);
	this.unitNumber = unitNumber;
	this.parkingSpaces = parkingSpaces;
	this.building = building;
}

//getters
public String getUnitNumber() {
	return unitNumber;
}
public int getParkingSpaces() {
	return parkingSpaces;
}
public Building getBuilding() {
	return building;
}

//setters
public void setUnitNumber(String unitNumber) {
	this.unitNumber = unitNumber;
}
public void setParkingSpaces(int parkingSpaces) {
	this.parkingSpaces = parkingSpaces;
}
public void setBuilding(Building building) {
	this.building = building;
	
}
//methods
@Override
public String toString() {
	return "Apartment [unitNumber=" + unitNumber + ", parkingSpaces=" + parkingSpaces + ", toString()="
			+ super.toString() + "]";
}


}
