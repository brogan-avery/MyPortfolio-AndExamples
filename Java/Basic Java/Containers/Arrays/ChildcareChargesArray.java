
//Brogan Avery
import java.util.Scanner;
import java.text.DecimalFormat;

public class ChildcareChargesAvery {

	public static void main(String[] args) {
		int age = 0;
		int days_in_attendance = 0;
		int total = 0;

		String dec_pattern = "###,###,###.00";
		DecimalFormat decimalFormat = new DecimalFormat(dec_pattern);

		Scanner input = new Scanner(System.in);

		while (age != 999) {
			System.out
					.println("Enter Child's age (as a year) or enter 999 to see total for all children you entered: ");
			age = input.nextInt();

			if (age != 999) {
				System.out.println("Enter how many days a week your child will attend: ");
				days_in_attendance = input.nextInt();

				System.out.println("----------\nWeekly rate for THIS child: $"
						+ decimalFormat.format(determineChildcareCharges(age, days_in_attendance)) + "\n----------");
				total = total + determineChildcareCharges(age, days_in_attendance);
			}
		}
		input.close(); // closes the scanner

		System.out.println("==========\nYour TOTAL weekly charge: $" + decimalFormat.format(total));

	}// END MAIN

	public static int determineChildcareCharges(int age, int days) {
		int rates[][] = { { 30, 60, 88, 115, 140 }, { 26, 52, 70, 96, 120 }, { 24, 46, 67, 89, 110 },
				{ 22, 40, 60, 75, 88 }, { 20, 35, 50, 66, 84 } };

		int weekly_rate = rates[age][days - 1];

		return weekly_rate;

	}// END DETERMINE CHARGES

}// END CLASS
