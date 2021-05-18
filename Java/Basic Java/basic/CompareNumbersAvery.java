/**************************************************************
* Title: Compare Numbers
* Author: Brogan Avery
* Created : 2019
***************************************************************/

import java.util.Scanner; 
public class CompareNumbersAvery {
	public static void main(String[] args) {
		double number1;
		double number2;
		
		System.out.println("Use this to check if one number is equal to, greater than, or less than another number");
		
		Scanner input = new Scanner(System.in); //scan for input
		 
		System.out.println("Enter 1st number");
		number1 = input.nextDouble();
		
		System.out.println("Enter 2nd number");
		number2 = input.nextDouble();
				
		input.close(); //scanner close 
		
		if (number1 == number2) {
			  System.out.print(number1 + " and " + number2 + " are equal");
		}
		else if (number1 > number2){
			  System.out.print(number1 + " is greater than " + number2);
		}
		else if (number1 < number2){
			  System.out.print(number1 + " is less than " + number2);
		}
		
	
		
	}
}
