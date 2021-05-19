//Brogan Avery
public class Pizza extends MenuItem {

// object (instance) variable
	private String topping;
	private String size;
	private double price;
	private int orderNumber;
	private static int nextOrderNumber = 1001;

//constructors

	public Pizza(String topping, String size, double price) {
		setTopping(topping);
		setSize(size);
		setPrice(price);
		nextOrderNumber++;
		orderNumber = nextOrderNumber;

		if (getSize() == null) {
			throw new IllegalArgumentException("Object not created");
		}

	}

//getters
	public String getTopping() {
		return topping;
	}

	public String getSize() {
		return size;
	}

	public double getPrice() {
		return price;
	}

	public int getOrderNumber() {
		return orderNumber;
	}

//setters
	public void setTopping(String topping) {
		this.topping = topping;

	}

	public void setSize(String size) {
		size.toLowerCase();
		if (size.contentEquals("small") || size.contentEquals("medium") || size.contentEquals("large")
				|| size.contentEquals("extra large")) {
			this.size = size;
		}
	}

	public void setPrice(double price) {
		this.price = price;
	}

//methods
	public String repeatOrder() {
		return ("___Review order___ \n " + super.getDescription() + "Order Number:" + orderNumber + "\n topping: "
				+ topping + "\n size:" + size + "\n price: $" + price);
	}

	@Override
	public String toString() {
		return "Pizza [topping=" + topping + ", size=" + size + ", price=" + price + ", orderNumber=" + orderNumber
				+ "]";
	}

	public static Pizza quickOrder(String topping) {

		Pizza p = new Pizza(topping, "large", 9.99);

		return p;

	}

}// END CLASS
