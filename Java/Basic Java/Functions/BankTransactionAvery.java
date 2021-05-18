//Brogan Avery 
//Craig, Amber, Cassandra, Travis
import java.util.ArrayList;
import java.util.Scanner;
import java.text.DecimalFormat;
public class BankTransactionAvery {

	public static void main(String[] args) {
		double balance = -1;
		String again = "yes";
		boolean go_again = true;
		
		String choice = "idk";

		ArrayList<String> transaction_options = new ArrayList<String>();
		transaction_options.add("withdraw");
		transaction_options.add("deposit");
		
		
		String dec_pattern = "###,###,###.##";
		DecimalFormat decimalFormat = new DecimalFormat(dec_pattern);

		Scanner input = new Scanner(System.in); //scan for input
		
		 
		while (balance < 0){
		 System.out.println("Enter your current balance:");
		 balance = input.nextDouble();
		 
		}
		
		while (go_again = true) {
			
			choice = "idk";
		double amount = balance + 1;
		 while (!transaction_options.contains(choice)) {
			 System.out.println("Enter which option you would like to do. withdraw or deposit:");
			 choice = input.nextLine();
		 }
		 
		 if (choice.contentEquals("withdraw")){
			 while(amount > balance) {
				 System.out.println("Enter amount to withdraw:");
				 amount = input.nextDouble(); 
			 }
			 balance = withdraw(balance,amount);
		 }
		 
		 else {
			 System.out.println("Enter amount to deposit:");
			 amount = input.nextDouble();
			 balance = deposit(balance,amount);
		 }
		 
		 
		 System.out.println("Your new balance: $" + decimalFormat.format(balance));
		 
		
		 System.out.println("Do you want to make another transaction? yes or no");
		 again = input.nextLine();
		 
		 if (again.contains("n")){
			 go_again = false; 
		 }
		 
		  
		}// and big while
		
		 input.close(); //closes the scanner
		 
		 System.out.println("ok, bye");
		
		
		
		
		
		
	}//END MAIN
	
	public static double deposit(double balance,double amount){
		balance = amount + balance;
		return balance;
	}
	
	public static double withdraw(double balance,double amount){
		balance = balance - amount;
		return balance;
	}

}
