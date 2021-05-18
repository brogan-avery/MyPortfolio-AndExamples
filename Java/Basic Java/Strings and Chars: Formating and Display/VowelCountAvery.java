
/**************************************************************
* Title: Vowel Count
* Author: Brogan Avery
* Created: 2019 
***************************************************************/
import java.util.Scanner;

public class VowelCountAvery {
	public static void main(String[] args) {
		int vowel_count;
		String message;
		Scanner input = new Scanner(System.in); // scan for input

		System.out.println("Enter a word: ");
		String in_word = input.nextLine();
		
		input.close(); // closes the scanner

		vowel_count = checkForVowel(in_word.toLowerCase());

		if (vowel_count > 0) {
			message = ("the vowel count is " + vowel_count);
		} 
		else {
			vowel_count = checkForY(in_word.toLowerCase());
			if (vowel_count > 0) {
				message = ("the vowel count is " + vowel_count);
			} 
			else {
				message = ("You must have made a spelling error");
			}
		}
		System.out.println(message);
	}// END MAIN

	public static int checkForVowel(String in_word) {
		int vowel_count = 0;
		char ch = ' ';
		for (int i = 0; i <= in_word.length() - 1; i++) {
			ch = in_word.charAt(i);

			if (ch == 'a' || ch == 'e'  || ch == 'i'  || ch == 'o' || ch == 'u' ) {
				vowel_count++;
			}
		}
		return vowel_count;
	}

	public static int checkForY(String in_word) {
		int vowel_count = 0;
		char ch = ' ';
		for (int i = 0; i <= in_word.length() - 1; i++) {
			ch = in_word.charAt(i);

			if (ch == 'y' ){
				vowel_count++;
			}
		}
		return vowel_count;
	}
}
