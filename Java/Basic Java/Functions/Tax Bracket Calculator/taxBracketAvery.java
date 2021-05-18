
/**************************************************************
* Title: Tax bracket
* Author: Brogan Avery
* Created: 2019 
***************************************************************/
import java.text.DecimalFormat;
import java.util.Scanner;
public class taxBracketAvery {

	public static void main(String[] args) {
		Scanner input = new Scanner(System.in); // scan for input
		
		String no_dec_pattern = "###,###,###";
		DecimalFormat decimalFormat_0 = new DecimalFormat(no_dec_pattern);
		
		System.out.println("Enter income ");
		double income = input.nextDouble();
		
		while (income > 0){
		
			System.out.println("---- Your tax bill ----\n" 
					+ "Your income: $" 
					+ decimalFormat_0.format(income) 
					+ "\n"
					+ "Your federal tax: $"
					+ decimalFormat_0.format(fedTaxBracket(income))
					+ "\n**************\n"
					+ "Your state tax: $"
					+ decimalFormat_0.format(iowaTaxBracket(income))
					+ "\n");
			System.out.println("Enter income ");
			income = input.nextDouble();
		}
		input.close();
	}
			
	public static double fedTaxBracket(double income) {
		final double BRACKET_39 = 418400;
		final double BRACKET_33 = 191651;
		final double BRACKET_25 = 33951;
		double applicableBracket = 0.1; //so it will default to lowest
		if (income > BRACKET_39) {
			applicableBracket = 0.396;
		} 
		else if(income > BRACKET_33) {
			applicableBracket = 0.33;
		} 
		else if(income > BRACKET_25) {
				applicableBracket = 0.25;
		} 
		
		return applicableBracket * income;
	}
	
	public static double iowaTaxBracket(double income) {
		final double BRACKET_898 = 69930;
		final double BRACKET_68 = 22896;
		final double BRACKET_243 = 1555;
		double applicableBracket = 0.0036; //so it will default to lowest
		if (income > BRACKET_898) {
			applicableBracket = 0.0898;
		} 
		else if(income > BRACKET_68) {
			applicableBracket = 0.068;
		}
		else if(income > BRACKET_243) {
				applicableBracket = 0.0243;
		}
		
		return applicableBracket * income;
	}
}
