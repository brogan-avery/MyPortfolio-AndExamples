
/**************************************************************
* Title: Book Order
* Author: Brogan Avery
* Created: 2019 
***************************************************************/
import java.util.Scanner; 
import java.text.DecimalFormat;

public class BookOrderAvery {
	public static void main(String[] args) {
		int num_of_books;
		double price;
		double subtotal = 0;
		
		
		
		String dec_pattern = "###,###,###.##";
		DecimalFormat decimalFormat = new DecimalFormat(dec_pattern);
		
		Scanner input = new Scanner(System.in); //scan for input
		 
		

        System.out.println("Enter number of books:");
        num_of_books = input.nextInt(); 
        
        
        
        for(int i = 0; i < num_of_books; i++) {
        	 System.out.println("Enter book price:");
             price = input.nextDouble(); 
             
        
             subtotal = subtotal + price;
             System.out.println("--------------");
             System.out.println("Running total: $" + decimalFormat.format(subtotal));
             System.out.println("--------------");
        }

        
        input.close(); //closes the scanner
        
        double book_qty = num_of_books;
        
        double grandtotal = calcTotal(subtotal,book_qty);
        
        
        System.out.println("Number of books purchased: " + num_of_books);
        System.out.println("Book Subtotal: " + "$"+decimalFormat.format(subtotal));
        System.out.println("--------------");
        System.out.println("Order Total: " + "$"+decimalFormat.format(grandtotal));
        
	}

	public static double calcTotal(double subtotal,double book_qty){
		double tax;
		final double tax_rate = 0.055;
		double shipping;
		final double shipping_rate=1.5;
		double order_total;
		tax= tax_rate * subtotal;
        shipping = book_qty * shipping_rate;
        order_total = subtotal + shipping + tax;
        return order_total;
	}
}
