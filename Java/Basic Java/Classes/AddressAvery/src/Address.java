//Brogan Avery
public class Address {
	private String house_number;
	private String street;
	private String apartment_number;
	private String  city;
	private String state;
	private String postal_code;
	
	//constructors
	public Address(String house_number, String street, String city, String state, String postal_code) {
		setHouse_number(house_number);
		setStreet(street);
		setApartment_number("");
		setCity(city);
		setState(state);
		setPostal_code(postal_code);
		
		if (getState() == null || getPostal_code() == null) {
			throw new IllegalArgumentException("Object not created");
		}
	}
	
public Address(String house_number, String street,String apartment_number, String city, String state, String postal_code) {
	setHouse_number(house_number);
	setStreet(street);
	setApartment_number(apartment_number);
	setCity(city);
	setState(state);
	setPostal_code(postal_code);
	

	if (getState() == null || getPostal_code() == null) {
		throw new IllegalArgumentException("Object not created");
	}
	
	}
	//getters
	public String getHouse_number() {
		return house_number;
	}
	public String getStreet() {
		return street;
	}
	public String getApartment_number() {
		return apartment_number;
	}
	public String getCity() {
		return city;
	}
	public String getState() {
		return state;
	}
	public String getPostal_code() {
		return postal_code;
	}
	
	
	//setters
	public void setHouse_number(String house_number) {
		this.house_number = house_number;
	}
	public void setStreet(String street) {
		this.street = street;
	}
	public void setApartment_number(String apartment_number) {
		this.apartment_number = apartment_number;
	}
	public void setCity(String city) {
		this.city = city;
	}
	public void setState(String state) {
		if (state.length() < 3) {
			this.state = state;
		}
		
	}
	public void setPostal_code(String postal_code) {
		if (postal_code.length() == 5) {
		this.postal_code = postal_code;
		}
	}
	
	
	//helpers
	public  void print() {
		System.out.print(house_number + " " + street+ " " + apartment_number + "\n" + city+ ", " + state+ " " + postal_code + "\n");
	}
	
	
}
