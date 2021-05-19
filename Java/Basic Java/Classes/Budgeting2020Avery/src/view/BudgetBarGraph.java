//Brogan Avery
/**
 * Creates and updates the bar representing the total monthly income as a whole and the monthly expenses as a part of the whole.
 */
package view;

import java.awt.Color;
import java.awt.Graphics;
import javax.swing.JComponent;

public class BudgetBarGraph extends JComponent {
	private int x = 0;
	private int y = 0;
	private int barLength = 270;
	private int height = 30;
	private int budgetSpent = 0;

	Color budgetSpentColor;

	public void paintComponent(Graphics g) {
		g.setColor(Color.gray);
		g.fillRect(x, y, barLength, height);

		g.setColor(budgetSpentColor);
		g.fillRect(x, y, budgetSpent, height);
	}
/**
 *Gets the percent of the budget that is unspent from the updateBudget method.
 * Uses it to calculate how much is spent and then represents that in the graph. 
 * 
 */
	public void adjustFill(double budgetRemaining) {
		double fill = barLength - (barLength * budgetRemaining);
		budgetSpent = (int) fill;
		budgetSpentColor = Color.green;

		if (budgetSpent >= (0.7 * barLength)) {
			budgetSpentColor = Color.blue;
		}

		if (budgetSpent >= barLength) {
			budgetSpent = barLength;
			budgetSpentColor = Color.red;
		}

		repaint();
	}
}
