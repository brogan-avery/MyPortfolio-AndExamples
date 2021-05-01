//Brogan Avery
import java.text.DecimalFormat;
import java.util.Scanner;
public class ShopperRewardsAvery {

	public static void main(String[] args) {
		double grocery_bill;
		double gas_discount;
		double discount_percentage;
		
		String two_dec_pattern = "###,###,###.00";
		String no_dec_pattern = "###,###,###";
		DecimalFormat decimalFormat_2 = new DecimalFormat(two_dec_pattern);
		DecimalFormat decimalFormat_0 = new DecimalFormat(no_dec_pattern);
		
//input section		
		Scanner input = new Scanner(System.in);
		
		System.out.println("Enter grocery bill:");
        grocery_bill = input.nextDouble(); //finds next input
          
        input.close();
        
//output section
        discount_percentage = calcDiscount(grocery_bill);
        gas_discount = calcGasDiscount(grocery_bill);
        System.out.println("Thank you for your purchase of $" + grocery_bill + ". " +  "\n" + "You received a discount coupon of $" + decimalFormat_2.format(grocery_bill * discount_percentage) + "." + "\n" +  "(" + decimalFormat_0.format(discount_percentage * 100) +"% of your purchace" + ")" + "\n" + "You have earned a " + decimalFormat_0.format(gas_discount) + "¢ discount per gallon of gas." );
	
	}//END MAIN-----------------------
	
//**CALC DISCOUNT**
	public static double calcDiscount(double grocery_bill) {
		double discount_percentage = 0;
		final double L1_DISCOUNT = 0 ; // = discount level/range
		final double L2_DISCOUNT = 0.04;
		final double L3_DISCOUNT = 0.07;
		final double L4_DISCOUNT = 0.1;
		final double L5_DISCOUNT = 0.15;
		final int L1_MAX = 10 ;
		final int L2_MAX =  70;
		final int L3_MAX =  150;
		final int L4_MAX =  250;
		final int L5_MIN =  250;
		
		if (grocery_bill <= L1_MAX){
			discount_percentage = L1_DISCOUNT;	
		}
		
		else if (grocery_bill <= L2_MAX){
			discount_percentage = L2_DISCOUNT;
		}
		
		else if (grocery_bill <= L3_MAX){
			discount_percentage = L3_DISCOUNT;
		}
		
		else if (grocery_bill <= L4_MAX){
			discount_percentage = L4_DISCOUNT;
		}
		
		else if (grocery_bill > L5_MIN){
			discount_percentage = L5_DISCOUNT;
		}
		
		return discount_percentage;
	}

//** GAS DISCOUNT**
	public static double calcGasDiscount(double grocery_bill) {	
		double cents_off = 0;
		final double L0_DISCOUNT = 0;
		final double L1_DISCOUNT = 1; // = discount level/range
		final double L2_DISCOUNT = 2;
		final double L3_DISCOUNT = 3;
		final int L0_MAX = 1;
		final int L1_MIN = 1 ;
		final int L1_MAX =  49;
		final int L2_MAX =  100;
		final int L3_MIN =  100;
		
		if(grocery_bill < L0_MAX) {
			cents_off = L0_DISCOUNT;
		}
		
		else if (grocery_bill >= L1_MIN && grocery_bill <=  L1_MAX){
			cents_off = L1_DISCOUNT;	
		}
		
		else if (grocery_bill <= L2_MAX){
			cents_off = L2_DISCOUNT;
		}
		
		else if (grocery_bill > L3_MIN){
			cents_off = L3_DISCOUNT;
		}
		return cents_off;
	}
}
