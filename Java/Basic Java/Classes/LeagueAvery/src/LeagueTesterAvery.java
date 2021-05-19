//Brogan Avery
import java.util.ArrayList;
public class LeagueTesterAvery {

	public static void main(String[] args) {
		
		Team team1 = new Team(8,"John Adams", "Tigers");
		Team team2 = new Team(7,"James Madison", "Bears");
		Team team3 = new Team(13,"Andrew Jackson", "Lions");
		Team team4 = new Team(12,"Woodrow Wilson", "Whales");
		Team team5 = new Team(9,"Herbert Hoover", "Snails");
		
		System.out.println(team1.displayTeamInfo());
		System.out.println("--------");
		System.out.println(team2.displayTeamInfo());
		System.out.println("--------");
		System.out.println(team3.displayTeamInfo());
		System.out.println("--------");
		System.out.println(team4.displayTeamInfo());
		System.out.println("--------");
		System.out.println(team5.displayTeamInfo());
	
		ArrayList<Team> teamslist = new ArrayList<Team>();
		teamslist.add(team1);
		teamslist.add(team2);
		teamslist.add(team3);
		teamslist.add(team4);
		teamslist.add(team5);
		
		System.out.println("\n_____From ArrayList____");
		for (Team object : teamslist) {
			System.out.print(object.displayTeamInfo() + "\n ------ \n ");
		}
		
		System.out.println("\n_____TEAMS FOR NEXT YEAR____");
//		System.out.println(team1.createSameTeamForNextSession().displayTeamInfo());
		
		Team team1_2021 = team1.createSameTeamForNextSession();
		System.out.println(team1_2021.displayTeamInfo());
		System.out.println("--------");
		
		Team team2_2021 = team2.createSameTeamForNextSession();
		System.out.println(team2_2021.displayTeamInfo());
		System.out.println("--------");
		
		Team team3_2021 = team3.createSameTeamForNextSession();
		System.out.println(team3_2021.displayTeamInfo());
		
	}
	
	
}
