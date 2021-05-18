/**************************************************************
* Title: Compound interest rates
* Author: Brogan Avery
* Created: 2019
* Description: calculates the interest rates on a users account balance  
***************************************************************/
import java.util.Scanner; 
public class CompoundInterestAvery {

	public static void main(String[] args) {
		
		double current_amount; //P
		double rate_of_growth; //R
		double time_in_bank;   //T
		int future_year;
		int this_year = 2020;
		
		Scanner input = new Scanner(System.in); //scan for input
		
		System.out.println("Enter your starting account balence:");
        current_amount = input.nextDouble(); //finds next input
        
        System.out.println("Enter the interest growth rate:");
        rate_of_growth = input.nextDouble(); //finds next input
        
        System.out.println("Enter what year you want to see the future balance for:");
        future_year = input.nextInt(); //finds next input
        
        input.close();
        
        time_in_bank = future_year - this_year;
        
        System.out.printf("Your total is $%.2f", computeBalance(current_amount, rate_of_growth, time_in_bank));
		
		
        System.out.printf("Your total is $%.2f", computeBalance(5000, .05, 10));

     // should return $8144.47

     System.out.printf("\nYour total is $%.2f", computeBalance(2000, .03, 5));

     // should return $2318.55

     System.out.printf("\nYour total is $%.2f", computeBalance(3000, .01, 10));

     // should return $3313.87
	}
	
	public static double computeBalance(double current_amount, double rate_of_growth, double time_in_bank){
		double step1 = (1+ rate_of_growth);
		double step2 = Math.pow(step1, time_in_bank);
		double answer = current_amount * step2;
		return answer;
	}
}
