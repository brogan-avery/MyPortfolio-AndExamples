
/**************************************************************
* Title: Rock, Paper, Scissors, Lizard, Spock
* Author: Brogan Avery
* Created: 2019 
***************************************************************/
import java.util.Scanner;

public class RPSLSAvery {
	public static void main(String[] args) {

		Scanner input = new Scanner(System.in); // scan for input

		// player 1 input

		System.out.println("Player1: Rock, paper, scissors, lizard, or spock? ");
		String player1_input = input.nextLine();
		player1_input = player1_input.toUpperCase();

		// player 2 input

		System.out.println("Player2: Rock, paper, scissors, lizard, or spock? ");
		String player2_input = input.nextLine();
		player2_input = player2_input.toUpperCase();

		input.close();

		String result = getWinner(player1_input, player2_input);

		System.out.println(result);
	}

	public static String getWinner(String player1_input, String player2_input) {
		// if player choices are equal
		String result = "";
		if (player1_input.contentEquals(player2_input)) {
			result = "TIE";
		}

		// if player choices are not equal
		else {
			switch (player1_input) {

			// if p1 = ROCK
			case "ROCK":

				if (player2_input.contentEquals("SCISSORS")) {
					result = "PLAYER1 WINS";
				}

				else if (player2_input.contentEquals("PAPER")) {
					result = "PLAYER2 WINS";

				}

				else if (player2_input.contentEquals("LIZARD")) {
					result = "PLAYER1 WINS";
				}

				else if (player2_input.contentEquals("SPOCK")) {
					result = "PLAYER2 WINS";
				}

				// if p1 = PAPER
			case "PAPER":

				if (player2_input.contentEquals("SCISSORS")) {
					result = "PLAYER2 WINS";
				}

				else if (player2_input.contentEquals("ROCK")) {
					result = "PLAYER1 WINS";

				}

				else if (player2_input.contentEquals("LIZARD")) {
					result = "PLAYER2 WINS";
				}

				else if (player2_input.contentEquals("SPOCK")) {
					result = "PLAYER1 WINS";
				}

				// if p1 = SCISSORS
			case "SCISSORS":

				if (player2_input.contentEquals("ROCK")) {
					result = "PLAYER2 WINS";
				}

				else if (player2_input.contentEquals("PAPER")) {
					result = "PLAYER1 WINS";

				}

				else if (player2_input.contentEquals("LIZARD")) {
					result = "PLAYER1 WINS";
				}

				else if (player2_input.contentEquals("SPOCK")) {
					result = "PLAYER2 WINS";
				}

				// if p1 = LIZARD
			case "LIZARD":

				if (player2_input.contentEquals("ROCK")) {
					result = "PLAYER2 WINS";
				}

				else if (player2_input.contentEquals("PAPER")) {
					result = "PLAYER1 WINS";
				} 
				else if (player2_input.contentEquals("SCISSORS")) {
					result = "PLAYER2 WINS";
				} 
				else if (player2_input.contentEquals("SPOCK")) {
					result = "PLAYER1 WINS";
				}

				// if p1 = SPOCK
			case "SPOCK":

				if (player2_input.contentEquals("ROCK")) {
					result = "PLAYER1 WINS";
				}

				else if (player2_input.contentEquals("PAPER")) {
					result = "PLAYER2 WINS";
				} 
				else if (player2_input.contentEquals("SCISSORS")) {
					result = "PLAYER1 WINS";
				} 
				else if (player2_input.contentEquals("LIZARD")) {
					result = "PLAYER2 WINS";
				}

			}
		}

		return result;

	}

}
