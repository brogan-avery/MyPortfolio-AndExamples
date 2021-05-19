package view;
//Brogan Avery
/**
 * This class is used to set up the JFrame and add the JPanel to it.
 * It creates a new Budget object to use throughout the program.
 * Inherits from the JFrame class.
 * 
 */

import javax.swing.JFrame;
import javax.swing.JPanel;
import java.awt.BorderLayout;
import model.Budget;

public class BudgetFrame extends JFrame {

	Budget newBudget = new Budget();
		
//constructor
public BudgetFrame() {				
				JPanel panel = new BudgetPanel(newBudget); // makes the panel object
				add(panel); 

				// set frame size
				final int FRAME_WIDTH = 290;
				final int FRAME_HEIGHT = 500;
				setSize(FRAME_WIDTH, FRAME_HEIGHT);

				// title
				setTitle("Monthly Budget");

				// set close
				setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

				
				// make visible
				setVisible(true);

	}

}
