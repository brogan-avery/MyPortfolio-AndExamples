//Brogan Avery
/**
 * This tests the methods for the budget class.
 */
package tests;
import model.Budget;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

class BudgetTest {
	private final double DELTA = 0.1;
	
	Budget testBudget = new Budget(1200,500,150,250,100);
	Budget testOverSpending = new Budget(800,475,300,200,250);

	@Test
	void testCalculateBudget() {
		assertEquals(200, testBudget.calculateBudget());
		assertEquals(-425, testOverSpending.calculateBudget());   //Over spending will be handled in GUI classes
	}
	
	@Test
	void testUpdateBudget() {
		assertEquals(0.166, testBudget.updateBudget(),DELTA);
		assertEquals(-0.53, testOverSpending.updateBudget(),DELTA);	//this looks weird right now to consider -53% as a valid option, but it can represent how much over budget they are(the total expenses are 53% more than what the budget is or they plan to spend 153% of the budget, which helps the user to see how much they need to alter their estimated spending by.  
	}

}
