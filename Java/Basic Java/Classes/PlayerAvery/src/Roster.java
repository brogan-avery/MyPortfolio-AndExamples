//Brogan Avery
import java.util.ArrayList;

public class Roster {
//vars
	private String teamName;
	private ArrayList<Player> playersList = new ArrayList<Player>();
//constructors
	public Roster(String teamName) {
		setTeamName(teamName);
	}
//getters
	public String getTeamName() {
		return teamName;
	}
	public ArrayList<Player> getPlayersList() {
		return playersList;
	}
//setters

	public void setTeamName(String teamName) {
		this.teamName = teamName;
	}


	public void setPlayersList(ArrayList<Player> playersList) {
		this.playersList = playersList;
	}
//methods
	public void addToTeam(Player p) {
		this.playersList.add(p);
	}
	
	public String displayRoster() {
		StringBuilder str  = new StringBuilder(teamName + "\n"); 
			for (Player item : playersList) {
				str.append(item.formatPlayerInformation() +"\n");
			}	
		return str.toString();
		}
	}

	
	
	

