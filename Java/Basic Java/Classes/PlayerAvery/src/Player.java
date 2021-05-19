//Brogan Avery
public class Player {
//vars	
	private String number;
	private String name;
	private String position;
	
//constructors
	public Player(){
		setName(null);
		setNumber(null);
		setPosition(null);
	}
	
	public Player(String name, String number, String position){
		setName(name);
		setNumber(number);
		setPosition(position);
	}
	
//getters
	public String getNumber() {
		return number;
	}
	public String getName() {
		return name;
	}
	public String getPosition() {
		return position;
	}
	
//setters
	public void setNumber(String number) {
		this.number = number;
	}
	public void setName(String name) {
		this.name = name;
	}
	public void setPosition(String position) {
		this.position = position;
	}
//methods
	@Override
	public String toString() {
		return "Player [number=" + number + ", name=" + name + ", position=" + position + "]";
	}
	
	public String formatPlayerInformation(){
		return "#" + getNumber() + ": " + getName() + ", " + getPosition();
	}
	
}
