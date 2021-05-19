//Brogan Avery
package model;
import java.util.ArrayList;

public class ElectricBlanket extends Blanket {
	private int numOfHeatSettings;
	private boolean hasAutoShutOff;
	
//constructors
	public ElectricBlanket() {
		super();
		this.numOfHeatSettings = 1;
		this.hasAutoShutOff = false;
	}
	
	public ElectricBlanket(String size, String color, String material, int numOfHeatSettings, boolean hasAutoShutOff) {
		super(size, color, material);
		this.numOfHeatSettings = numOfHeatSettings;
		this.hasAutoShutOff = hasAutoShutOff;
	}
//getters
	public int getNumOfHeatSettings() {
		return numOfHeatSettings;
	}
	
	public boolean isHasAutoShutOff() {
		return hasAutoShutOff;
	}
	
//setters
	public void setNumOfHeatSettings(int numOfHeatSettings) {
		if(numOfHeatSettings > 0 ||numOfHeatSettings <= 5) {
			this.numOfHeatSettings = numOfHeatSettings;
		}
		
	}
	public void setHasAutoShutOff(boolean hasAutoShutOff) {
		if (hasAutoShutOff == true) {
		super.price = getPrice()+ 5.75;
		}
		this.hasAutoShutOff = hasAutoShutOff;
	}

	
//methods
	@Override
	public String toString() {
		return "ElectricBlanket [numOfHeatSettings=" + numOfHeatSettings + ", hasAutoShutOff=" + hasAutoShutOff
				+ ", toString()=" + super.toString() + "]";
	}
	@Override
	public String  featureReport() {
		String autoOff = "with";
		if(this.hasAutoShutOff == false) {
			autoOff = "without";
		}
		
		String formatedString = super.featureReport() + " including " +  numOfHeatSettings + " setting(s) " + autoOff + " auto shut off" ;
		return formatedString;
	}
}
