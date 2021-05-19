//Brogan Avery
package model;
import java.text.DecimalFormat;

public class Blanket {

	private String size;
	private String color;
	private String material;
	protected double price;
//constructors
	public Blanket() {
		this.price = 25;
		this.color = "blue";
		setSize("twin");
		setMaterial("wool");
		
	}
	
	public Blanket(String size, String color, String material) {
		this.price = 25;
		this.color = color;
		setSize(size);
		setMaterial(material);
	}
//getters

	public String getSize() {
		return size;
	}

	public String getColor() {
		return color;
	}

	public String getMaterial() {
		return material;
	}

	public double getPrice() {
		return price;
	}
	
//setters
	public void setSize(String size) {
		if(size.equals("twin")){
		this.size = size;
		}
		else if (size.equals("queen")){
			this.size = size;
			this.price = this.price + 25;
			}
		else if (size.equals("king")){
			this.size = size;
			this.price = getPrice() + 40;
			}
		else {
			throw new IllegalArgumentException("The only size options are twin, queen, or king");
		}
	}

	public void setColor(String color) {
		this.color = color;
	}

	public void setMaterial(String material) {
		if(material.equals("wool")){
			this.material = material;
			this.price = this.price + 20;
			}
			else if (material.equals("chenille")){
				this.material = material;
				this.price = this.price + 30;
				}
			else if (material.equals("cashmere")){
				this.material = material;
				this.price = this.price + 45;
				}
			else {
				throw new IllegalArgumentException("The only material options are wool, chenille, or cashmere");
			}
			
	}
	
	//methods
	@Override
	public String toString() {
		return "Blanket [size=" + size + ", color=" + color + ", material=" + material + ", price=" + price + "]";
	}
	
	public String  featureReport() {
		String dec_pattern = "###,###,###.00";
		DecimalFormat decimalFormat = new DecimalFormat(dec_pattern);
		
		 String formatedString = color + " " + size + " blanket made from " +  material + ", total price: $" + decimalFormat.format(price);
		 return formatedString;
	}

}
