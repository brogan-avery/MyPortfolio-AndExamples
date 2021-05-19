//Brogan Avery
public class HockeyPlayer extends Player {
//vars	
	private int  goals;
	
//constructors
	public HockeyPlayer(){
		setGoals(0);
	}
	
	public HockeyPlayer(String name, String number , String position ,int goals){
		super(name,number,position);
		setGoals(goals);
	}
//getters
	public int getGoals() {
		return goals;
	}
//setters
	public void setGoals(int goals) {
		this.goals = goals;
	}
//methods
	@Override
	public String toString() {
		return "HockeyPlayer [goals=" + goals + ", toString()=" + super.toString() + "]";
	}
	
	@Override
	public String formatPlayerInformation(){
		return "#" + super.getNumber() + ": " + super.getName() + ", " + super.getPosition() + ", Goals ~ " + goals;
	}
}
