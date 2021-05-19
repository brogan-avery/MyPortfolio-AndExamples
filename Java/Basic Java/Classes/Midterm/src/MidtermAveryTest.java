//Brogan Avery
import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

class MidtermAveryTest {

	@Test
	void testbonus() {
		assertEquals(27.14, MidtermAvery.bonus(1356.77 , false),0.1);
		assertEquals(437.07, MidtermAvery.bonus(14568.98  , true),0.1);
		assertEquals(197.53, MidtermAvery.bonus(9876.55 , false),0.1);
	}

}
