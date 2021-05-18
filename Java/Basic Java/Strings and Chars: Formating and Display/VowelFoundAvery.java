
/**************************************************************
* Title: Vowel Found 
* Author: Brogan Avery
* Created: 2019 
***************************************************************/
import java.util.Scanner;

public class VowelFoundAvery {
	public static void main(String[] args) {

		// String message;
		String in_word = "";
		Scanner input = new Scanner(System.in); // scan for input

		// System.out.println("Enter a word: ");
		// in_word = input.nextLine();

		while (!in_word.equalsIgnoreCase("exit")) {
			System.out.println("Enter a word or type exit to leave the program: ");
			in_word = input.nextLine();

			boolean has_vowel = checkForVowel(in_word);

			if (has_vowel == true && !in_word.equalsIgnoreCase("exit")) {
				System.out.println("Good job, you entered a word with a vowel. Keep checking words!!!");
				continue;
			} else if (in_word.equalsIgnoreCase("exit")) {
				System.out.println("ok,bye");
				continue;
			}

			System.out.println("Nope, there are no vowels ");

		}

		input.close(); // closes the scanner
		// }

	}// END MAIN

	public static boolean checkForVowel(String in_word) {
		boolean has_vowel = false;

		if (in_word.toLowerCase().contains("a")) {
			has_vowel = true;
		}
		if (in_word.toLowerCase().contains("e")) {
			has_vowel = true;
		}
		if (in_word.toLowerCase().contains("i")) {
			has_vowel = true;
		}
		if (in_word.toLowerCase().contains("o")) {
			has_vowel = true;
		}
		if (in_word.toLowerCase().contains("u")) {
			has_vowel = true;
		}

		return has_vowel;
	}

}
