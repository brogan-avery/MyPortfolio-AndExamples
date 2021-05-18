//Brogan Avery
import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

class CompoundInterestAveryTest {

	@Test
	void testcomputeBalance() {
		assertEquals(1141.17, CompoundInterestAvery.computeBalance(1000, .045, 3), 0.01);
		assertEquals(2318.55, CompoundInterestAvery.computeBalance(2000, .03, 5), 0.01);
		assertEquals(3313.87, CompoundInterestAvery.computeBalance(3000, .01, 10), 0.01);
	}

}
