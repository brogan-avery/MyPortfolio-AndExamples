package model;
//Brogan Avery
public class Classroom {
//variable
	private String building;
	private String roomNumber;
	private String campus;
	private String type;
	private int capacity;
	
//constructors
	
//      default ↓
	public Classroom() {
		setBuilding("not assigned");
		setroomNumber("not assigned");
		setCampus("not assigned");
		setType("not assigned");
		setCapacity(0);
	}
//     with values ↓
	public Classroom(String building,String roomNumber,String campus,String type,int capacity) {
		setBuilding(building);
		setroomNumber(roomNumber);
		setCampus(campus);
		setType(type);
		setCapacity(capacity);
	}
	
//getters	
	public String getBuilding() {
		return building;
	}
	public String getRoomNumber() {
		return roomNumber;
	}
	public String getCampus() {
		return campus;
	}
	public String getType() {
		return type;
	}
	public int getCapacity() {
		return capacity;
	}
	
//setters
	public void setBuilding(String building) {
		this.building = building;
	}
	public void setroomNumber(String roomNumber) {
		this.roomNumber = roomNumber;
	}
	public void setCampus(String campus) {
		this.campus = campus;
	}
	public void setType(String type) {
		this.type = type;
	}
	public void setCapacity(int capacity) {
		this.capacity = capacity;
	}
	
//methods	
	@Override
	public String toString() {
		return "Classroom [building=" + building + ", roomNumber=" + roomNumber + ", campus=" + campus + ", type="
				+ type + ", capacity=" + capacity + "]";
	}
	
	
}
