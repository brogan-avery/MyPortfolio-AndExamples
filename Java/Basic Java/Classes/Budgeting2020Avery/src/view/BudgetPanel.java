//Brogan Avery
/**
 * Creates and adds all of the buttons, labels, textfields, and graphics(creates new instance of the bar graph) to a JPanel which will be added to the JFrame
 * Contains two inner classes that are action listeners to be used with the buttons.
 */
package view;

import javax.swing.JPanel;
import javax.swing.JButton;
import javax.swing.JLabel;
import javax.swing.JTextField;
import java.awt.Dimension;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.ArrayList;
import model.Budget;
import java.text.DecimalFormat;

public class BudgetPanel extends JPanel {

	BudgetBarGraph bar = new BudgetBarGraph();

	final int BOXSIZE = 8;
	private JTextField monthlyIncomeTextBox = new JTextField(BOXSIZE); // these need to be globally accessible
	private JTextField housingTextBox = new JTextField(BOXSIZE);
	private JTextField insuranceAndUtilitiesTextBox = new JTextField(BOXSIZE);
	private JTextField restaurantsAndFoodTextBox = new JTextField(BOXSIZE);
	private JTextField autoTextBox = new JTextField(BOXSIZE);
	private JLabel message = new JLabel("Click submit to see your updated budget");

	Budget myBudget;

//constructor
	public BudgetPanel(Budget b) {
		myBudget = b;

		JLabel monthlyIncome = new JLabel("Monthly Income: ");
		JLabel housing = new JLabel("Housing Expenses: ");
		JLabel insuranceAndUtilities = new JLabel("Insurance and Utilities: ");
		JLabel restaurantsAndFood = new JLabel("Restaurants and Food: ");
		JLabel auto = new JLabel("Automobile Expenses: ");

		JButton submit = new JButton("Submit");
		JButton clear = new JButton("Clear");

		bar.setPreferredSize(new Dimension(275, 40));

		submitButtonListener submitButtonListener = new submitButtonListener(); // a thing to do
		submit.addActionListener(submitButtonListener); // tells button it will do thing

		clearButtonListener clearButtonListener = new clearButtonListener(); // a thing to do
		clear.addActionListener(clearButtonListener); // tells button it will do thing

		// add things to panel
		add(monthlyIncome);
		add(monthlyIncomeTextBox);
		add(housing);
		add(housingTextBox);
		add(insuranceAndUtilities);
		add(insuranceAndUtilitiesTextBox);
		add(restaurantsAndFood);
		add(restaurantsAndFoodTextBox);
		add(auto);
		add(autoTextBox);
		add(submit);
		add(clear);
		add(bar);
		add(message);
	}

//listener classes
	/**
	 * Creates an event listener for the submit button and then performs the
	 * action(s) specified in the method.
	 */
	class submitButtonListener implements ActionListener {

		/**
		 * Attempts to take user entered values in and cast as double to set for the
		 * values of the Budget class's instance variables. 
		 * Creates a message to display calculatedBudget method. 
		 * Message tells user how much they are over or under budget.
		 */
		@Override
		public void actionPerformed(ActionEvent e) {
			String dec_pattern = "###,###,###.00";
			DecimalFormat decimalFormat = new DecimalFormat(dec_pattern);

			ArrayList<Double> currentObjectVarsList = new ArrayList<Double>();
			currentObjectVarsList.add(myBudget.getMonthlyIncome());
			currentObjectVarsList.add(myBudget.getHousing());
			currentObjectVarsList.add(myBudget.getInsuranceAndUtilities());
			currentObjectVarsList.add(myBudget.getRestaurantsAndFood());
			currentObjectVarsList.add(myBudget.getAuto());

			ArrayList<String> textBoxValues = new ArrayList<String>();
			textBoxValues.add(monthlyIncomeTextBox.getText());
			textBoxValues.add(housingTextBox.getText());
			textBoxValues.add(insuranceAndUtilitiesTextBox.getText());
			textBoxValues.add(restaurantsAndFoodTextBox.getText());
			textBoxValues.add(autoTextBox.getText());

			ArrayList<Double> UpdatedObjectVarsList = new ArrayList<Double>();

			for (int i = 0; i < currentObjectVarsList.size(); i++) {
				double item = currentObjectVarsList.get(i);
				String boxItem = textBoxValues.get(i);

				try {
					item = Double.parseDouble(boxItem);
				} 
				catch (Exception E) {
					item = 0;       //any text field that isn't a number is treated as an empty box or as a 0.
				}

				finally {
					UpdatedObjectVarsList.add(item);
				}
			}

			myBudget.setMonthlyIncome(UpdatedObjectVarsList.get(0));
			myBudget.setHousing(UpdatedObjectVarsList.get(1));
			myBudget.setInsuranceAndUtilities(UpdatedObjectVarsList.get(2));
			myBudget.setRestaurantsAndFood(UpdatedObjectVarsList.get(3));
			myBudget.setAuto(UpdatedObjectVarsList.get(4));

			if (myBudget.calculateBudget() > 0) {
				message.setText("$" + decimalFormat.format(myBudget.calculateBudget()) + " remaining in budget");
			} 
			else if (myBudget.calculateBudget() <= 0) {
				double overAmount = myBudget.calculateBudget() * -1;
				message.setText("$" + decimalFormat.format(overAmount) + " OVER budget");
			}

			bar.adjustFill(myBudget.updateBudget());
		}
	}

	/**
	 * Creates an event listener for the clear button and then performs the
	 * action(s) specified in the method.
	 */
	class clearButtonListener implements ActionListener {

		/**
		 * Does not create a new object but sets all instance variables back to 0 for this object, 
		 * empties budget bar, resets message to default, and clears the text boxes.
		 */
		@Override
		public void actionPerformed(ActionEvent e) {
			myBudget.setMonthlyIncome(0);
			myBudget.setHousing(0);
			myBudget.setInsuranceAndUtilities(0);
			myBudget.setRestaurantsAndFood(0);
			myBudget.setAuto(0);
			
			message.setText("Click submit to see your updated budget");
			
			monthlyIncomeTextBox.setText("");
			housingTextBox.setText("");
			insuranceAndUtilitiesTextBox.setText("");
			restaurantsAndFoodTextBox.setText("");
			autoTextBox.setText("");
			
			bar.adjustFill(myBudget.updateBudget());


		}

	}

}
