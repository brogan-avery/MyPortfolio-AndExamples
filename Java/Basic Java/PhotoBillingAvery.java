/**************************************************************
* Title: Photo billing 
* Author: Brogan Avery
* Created: 2019
* Description: calculates the final price of orders based on different cases  
***************************************************************/
//Brogan Avery

import java.util.Scanner;

public class PhotoBillingAvery {

	public static void main(String[] args) {
//main variables
		double price;
		int input_qty;
		double discount;
		double grandtotal = 1;

//MAIN
		
//input section
		Scanner input = new Scanner(System.in);
		
		System.out.println("Enter price:");
        price = input.nextDouble(); //finds next input
          
        System.out.println("Enter quantity:");
        input_qty = input.nextInt(); //finds next input
        double qty = input_qty;
        
        System.out.println("Enter coupon discount percentage as decimal. If no discount, enter 0:");
        discount = input.nextDouble(); //finds next input

		input.close();
		
//Decision section 
		if (discount == 0){
			if (qty == 1) {
				grandtotal = computePhotoBill(price); //method1
			}
			else if (qty > 1) {
					grandtotal = computePhotoBill(price, qty); //method2
			}
		}
		else {
			grandtotal = computePhotoBill(price, qty, discount); //method3
		}
			
		
//output section
		
		System.out.printf("%5.2f%n", grandtotal);
		
//TESTS	
		System.out.printf("'%5.2f'%n", computePhotoBill(19.99));	
		System.out.printf("'%5.2f'%n", computePhotoBill(19.99, 2));
		System.out.printf("'%5.2f'%n", computePhotoBill(19.22, 2, 0.1));
		
	}
	
//method 1: price of one photo book ordered
	public static double computePhotoBill(double price){
		final double TAX_RATE = 0.06;
		double tax;
		double total;
		
		tax = price * TAX_RATE;
		total = price + tax;
		return total;
	}
	
//method 2:	price of a photo book and the quantity ordered (int)
	public static double computePhotoBill( double price, double qty){
		final double TAX_RATE = 0.06;
		double tax;
		double total;
		double subtotal;
		
		subtotal = price * qty;
		tax = subtotal * TAX_RATE;
		total = subtotal + tax;
		return total;
	}
	
//method 3: price of a photo book, the quantity ordered, and a coupon value
	public static double computePhotoBill(double price, double qty, double discount){
		final double TAX_RATE = 0.06;
		double tax;
		double total;
		double subtotal;
		double discount_amount;
		double discounted_subtotal;
		
		subtotal = price * qty;
		discount_amount = subtotal * discount;
		discounted_subtotal = subtotal - discount_amount;
		tax = discounted_subtotal * TAX_RATE;
		total = discounted_subtotal + tax;
		return total;
		
	}
}
