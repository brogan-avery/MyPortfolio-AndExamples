//Brogan Avery
public class House extends Rental{
private boolean hasYard;

//constructors
public House() {
	super();
}





public House(double rentAmount, String address, int bedrooms, int bathrooms, boolean isADAAccessible, boolean hasYard) {
	super(rentAmount, address, bedrooms, bathrooms, isADAAccessible);
	this.hasYard = hasYard;
}





//getters
public boolean isHasYard() {
	return hasYard;
}

//setters
public void setHasYard(boolean hasYard) {
	this.hasYard = hasYard;
}




//methods
@Override
public String toString() {
	return "House [hasYard=" + hasYard + ", toString()=" + super.toString() + "]";
}

}


