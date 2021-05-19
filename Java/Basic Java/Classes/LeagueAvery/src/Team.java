//Brogan Avery
public class Team {

	//vars
	private int teamId;
	private static int nextTeamId = 1000;
	private int numberOfPlayers;
	private String captain;
	private String teamName;
	
	//constructors
	public Team() {
		setTeamName(null);
		setNumberOfPlayers(0);
		setcaptain(null);
		nextTeamId++;
		teamId = nextTeamId;
		
		
	}
	
	public Team(int numberOfPlayers, String captain, String teamName) {
		setTeamName(teamName);
		setNumberOfPlayers(numberOfPlayers);
		setcaptain(captain);
		nextTeamId++;
		teamId = nextTeamId;
		
		if (getTeamName() == null) {
			throw new IllegalArgumentException("Object not created");
		}
		
		if (getNumberOfPlayers() == 0) {
			throw new IllegalArgumentException("Object not created");
		}
	}
	
	
	//getters
	public String getTeamName() {
		return teamName;
	}
	public int getTeamId() {
		return teamId;
	}
	public int getNumberOfPlayers() {
		return numberOfPlayers;
	}
	public String getcaptain() {
		return captain;
	}
	
	//setters
	public void setTeamName(String teamName) {
		teamName = teamName.trim();
		if (!teamName.contentEquals("")) {
		this.teamName = teamName;
		}
	}
	
	public void setNumberOfPlayers(int numberOfPlayers) {
		if (numberOfPlayers > 6 && numberOfPlayers < 14) {
			this.numberOfPlayers = numberOfPlayers;
		}
		
	}
	public void setcaptain(String captain) {
		this.captain = captain;
	}
	
//methods

	@Override
	public String toString() {
		return "Team [teamId=" + teamId + ", numberOfPlayers=" + numberOfPlayers + ", captain=" + captain
				+ ", teamName=" + teamName + "]";
	}
	
	public String displayTeamInfo() {
		
		return " team ID: " + teamId + "\n number of players: " + numberOfPlayers + "\n team captain: " + captain + "\n team name: " + teamName ;
	}
	
	public Team createSameTeamForNextSession() {
		Team t =  new Team(this.numberOfPlayers, this.captain, this.teamName);
		return t;
	}
}
