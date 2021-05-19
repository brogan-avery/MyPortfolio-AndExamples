//Brogan Avery
/** 
 * This class holds the values entered by the user and keeps track of them. 
 * It is used to calculated and update the dollar amount and percentage that represents the money spent as compared to the budget amount or income amount.
 */

package model;

import java.text.DecimalFormat;

public class Budget {
//Instance Variables
	private double monthlyIncome;
	private double housing;
	private double insuranceAndUtilities;
	private double restaurantsAndFood;
	private double auto;
//constructors

	// default constructor
	public Budget() {
		this.monthlyIncome = 0;
		this.housing = 0;
		this.insuranceAndUtilities = 0;
		this.restaurantsAndFood = 0;
		this.auto = 0;
	}

	// non default constructor
	public Budget(double monthlyIncome, double housing, double insuranceAndUtilities, double restaurantsAndFood,
			double auto) {
		this.monthlyIncome = monthlyIncome;
		this.housing = housing;
		this.insuranceAndUtilities = insuranceAndUtilities;
		this.restaurantsAndFood = restaurantsAndFood;
		this.auto = auto;
	}

//getters
	public double getMonthlyIncome() {
		return monthlyIncome;
	}

	public double getHousing() {
		return housing;
	}

	public double getInsuranceAndUtilities() {
		return insuranceAndUtilities;
	}

	public double getRestaurantsAndFood() {
		return restaurantsAndFood;
	}

	public double getAuto() {
		return auto;
	}

//setters
	public void setMonthlyIncome(double monthlyIncome) {
		this.monthlyIncome = monthlyIncome;
	}

	public void setHousing(double housing) {
		this.housing = housing;
	}

	public void setInsuranceAndUtilities(double insuranceAndUtilities) {
		this.insuranceAndUtilities = insuranceAndUtilities;
	}

	public void setRestaurantsAndFood(double restaurantsAndFood) {
		this.restaurantsAndFood = restaurantsAndFood;
	}

	public void setAuto(double auto) {
		this.auto = auto;
	}

//methods
	/**
	 * toString: Not used in program but used for testing.
	 */
	@Override
	public String toString() {
		return "Budget [monthlyIncome=" + monthlyIncome + ", housing=" + housing + ", insuranceAndUtilities="
				+ insuranceAndUtilities + ", restaurantsAndFood=" + restaurantsAndFood + ", auto=" + auto + "]";
	}

	/**
	 * calculateBudget: Totals up all expenses for the month. Calculates what dollar
	 * amount is left in the budget after subtracting the estimated spending amount.
	 * Returns the amount left in the budget.
	 */
	public double calculateBudget() {
		double totalExpenses = housing + insuranceAndUtilities + restaurantsAndFood + auto;
		double remainingBudgetAmount = monthlyIncome - totalExpenses;
		return remainingBudgetAmount;
	}

	/**
	 * updateBudget: Takes the returned amount from the calculateBudget method and
	 * returns it as a percentage of the monthly income. Returns the percentage of
	 * the budget to update the GUI graphics.
	 */
	public double updateBudget() {
		double remainingBudgetAmount = calculateBudget();
		double remainingBudgetPecentage = (remainingBudgetAmount / monthlyIncome);
		return remainingBudgetPecentage;
	}

}
