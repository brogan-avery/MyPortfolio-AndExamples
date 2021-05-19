//Brogan Avery
public class FootballPlayer extends Player{
//vars	
	private int totalYards;
	
//constructors
	public FootballPlayer(){
		setTotalYards(0);
	}
	
	public FootballPlayer(String name, String number , String position ,int totalYards){
		super(name,number,position);
		setTotalYards(totalYards);
	}
//getters
	public int getTotalYards() {
		return totalYards;
	}
//setters
	public void setTotalYards(int totalYards) {
		this.totalYards = totalYards;
	}
//methods
	@Override
	public String toString() {
		return "FootballPlayer [totalYards=" + totalYards + ", toString()=" + super.toString() + "]";
	}
	
	public String formatPlayerInformation(){
		return "#" + super.getNumber() + ": " + super.getName() + ", " + super.getPosition() +  ", Total yards ~ " + totalYards;
	}
}
