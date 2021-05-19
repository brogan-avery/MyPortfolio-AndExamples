//Brogan Avery
public class PizzaTesterAvery implements PizzaConstants{

	public static void main(String[] args) {
		System.out.println("Welcome to " + COMPANY);
		System.out.println(PizzaConstants.getSpecial());
		Pizza myPizza = new Pizza("cheese","large",9.99);
		System.out.print(myPizza.toString());
		System.out.println("\n--------------");
		myPizza.setTopping("mushroom");
		myPizza.setPrice(9.99);
		
		Pizza yourPizza = new Pizza( "pepperoni" ,"extra large", 13.99 );
		System.out.print(yourPizza.toString());
		System.out.println("\n--------------");
		yourPizza.setTopping("mushroom");
		yourPizza.setPrice(12.99);
		
	//	Pizza thirdPizza = new Pizza("pepperoni","extra small", 7.99);
	//	System.out.print(thirdPizza.toString());
	//	System.out.println("\n--------------");
		
		System.out.print(yourPizza.toString());
		System.out.println("\n--------------");
		System.out.print(myPizza.repeatOrder());
		System.out.println("\n--------------");
		System.out.print(yourPizza.repeatOrder());
	//	System.out.println("\n--------------");
	//	System.out.print(thirdPizza.repeatOrder());
		
		System.out.println("\n--------------");
		Pizza mikePizza = Pizza.quickOrder("mushroom");
		System.out.println("\n Mike's pizza: \n " + mikePizza.repeatOrder());
		
		System.out.println("\n--------------");
		Order brogan = new Order();
		brogan.addToOrder(myPizza);
		brogan.addToOrder(yourPizza);
		System.out.println(brogan.getTotalPrice());
	
	}//end main

}//end class
