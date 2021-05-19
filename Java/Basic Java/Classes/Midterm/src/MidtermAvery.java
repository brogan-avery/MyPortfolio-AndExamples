
//Brogan Avery
import java.util.Scanner;
import java.text.DecimalFormat;

public class MidtermAvery {
	public static void main(String[] args) {
		String name = "";
		double total_sales;
		String yes_or_no = "";
		boolean is_senior = false;

		String dec_pattern = "###,###,###.##";
		DecimalFormat decimalFormat = new DecimalFormat(dec_pattern);

		Scanner input = new Scanner(System.in); // scan for input

		while (!name.equalsIgnoreCase("exit")) {
			
		System.out.println("Enter name or enter exit to quit:");
		name = input.nextLine();

		String first_name = name.substring(0, 1).toUpperCase() + name.substring(1);

		System.out.println("Enter yes is the salesperson is part of the senior sales group. If not, enter no :");
		yes_or_no = input.nextLine();

		if (yes_or_no.equalsIgnoreCase("yes")) {
			is_senior = true;
		} else {
			is_senior = false;
		}

		System.out.println("Enter total sales:");
		total_sales = input.nextDouble();

		System.out.println(first_name + "-" + decimalFormat.format(bonus(total_sales, is_senior)));

		
		}
		input.close(); // closes the scanner
	}

	public static double bonus(double total_sales, boolean is_senior) {
		double bonus_percentage;
		double senior_bonus = 0.03;
		double not_senior_bonus = 0.02;
		double bonus_amount;
		if (is_senior == true) {
			bonus_percentage = senior_bonus;
		} else {
			bonus_percentage = not_senior_bonus;
		}
		bonus_amount = total_sales * bonus_percentage;
		return bonus_amount;
	}
}
