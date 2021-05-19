//Brogan Avery

public class PlayerTesterAvery {

	public static void main(String[] args) {
		FootballPlayer Arron = new FootballPlayer("Arron Rogers", "12", "Quarterback", 10);
		FootballPlayer Gronk = new FootballPlayer("Rob Gronkowski", "87", "Tight end", 20);
		
		HockeyPlayer Wayne = new HockeyPlayer("Wayne Gretzky", "99", "Centerman", 1);
		HockeyPlayer Toe = new HockeyPlayer ("Toe Blake", "6", "Winger", 2);
	
		System.out.println(Arron.formatPlayerInformation());
		System.out.println(Gronk.formatPlayerInformation());
		System.out.println(Wayne.formatPlayerInformation());
		System.out.println(Toe.formatPlayerInformation());
		
		Roster footballRoster = new Roster("Titans");
		footballRoster.addToTeam(Arron);
		footballRoster.addToTeam(Gronk);
		
		Roster hockeyRoster = new Roster("Toranto");
		hockeyRoster.addToTeam(Wayne);
		hockeyRoster.addToTeam(Toe);
		
		System.out.println(" ");
		System.out.println("Roster for: " + hockeyRoster.displayRoster());
		
		System.out.println("Roster for: " + footballRoster.displayRoster());
	}
}
