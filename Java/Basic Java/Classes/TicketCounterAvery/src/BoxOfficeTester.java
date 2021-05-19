//Brogan Avery
import java.util.Scanner;

public class BoxOfficeTester {

	public static void main(String[] args) {
		
		int ticketsRequested;
		BoxOffice show = new BoxOffice();
		
		Scanner input = new Scanner(System.in); 

		while (show.getTicketsLeft() >0) {
	
		System.out.println("There are " + show.getTicketsLeft() + " ticket(s) available \n-");
		System.out.println("How many tickets would you like to buy? ");
		ticketsRequested = input.nextInt(); 
		
		
		System.out.println("-----\n" + show.attemptSale(ticketsRequested, show.getTicketsLeft(), show.getBuyerCount()) + "\n-----");
		
		}
		
		input.close(); //closes the scanner
		
		if (show.getTicketsLeft() == 0) {
			String finalSalesReport;
			finalSalesReport = ("__Sales report for this show__\n" + "Unsold tickets: " + show.getTicketsLeft() + "\n Buyer count: " + show.getBuyerCount());
			System.out.println(finalSalesReport);
		}
		
	}
}

