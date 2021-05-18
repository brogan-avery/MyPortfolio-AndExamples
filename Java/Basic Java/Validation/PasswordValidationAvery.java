
/**************************************************************
* Title: Password Validation
* Author: Brogan Avery
* Created: 2019 
***************************************************************/
import java.util.Scanner;

public class PasswordValidationAvery {

	public static void main(String[] args) {
		String password;
		String check_password;

		Scanner input = new Scanner(System.in); // scan for input

		System.out.println("Enter new password:");
		password = input.nextLine();

		System.out.println("Re-enter password to confirm:");
		check_password = input.nextLine();
		input.close(); // closes the scanner

		System.out.println(validatePassword(password, check_password));

	}

	public static boolean validatePassword(String password, String check_password) {

		if (!password.contentEquals(check_password)) {
			return false;
		}
		if (password.length() < 8) {
			return false;
		}

		char c;
		boolean has_digit = false;
		boolean has_upper = false;
		boolean has_lower = false;
		for (int i = 0; i <= password.length() - 1; i++) {
			c = password.charAt(i);

			if (Character.isDigit(c)) {
				has_digit = true;
			}
			if (Character.isUpperCase(c)) {
				has_upper = true;
			}
			if (Character.isLowerCase(c)) {
				has_lower = true;
			}
		}
		if (has_digit == false) {
            return false;
		}
		if (has_upper == false) {
            return false;
		}
		if (has_lower == false) {
            return false;
		}
		else {
			return true;
		}

	}

}// class
