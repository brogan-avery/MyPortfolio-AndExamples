/**************************************************************
* Title: Array Error handling 
* Author: Brogan Avery
* Created: 2019
***************************************************************/
import java.util.Scanner;
public class BadArrayIndexAvery {

	public static void main(String[] args) {
		String[] names = { "Joe", "Mark", "John", "Kevin", "Paul", "Rocky", "Sam", "Fin","Jake","Tom"};
		
		Scanner input = new Scanner(System.in); 
		 
		System.out.println("Enter a number to see the associated name in that location");
		 int number = input.nextInt(); 
		 
		input.close(); //closes the scanner
		
		try {
		String some_name = names[number-1];
		System.out.print(some_name);
		}
		
		catch(Exception e) {
			System.out.print("Sorry, that location does not exist.");
			}
	}
		

}
