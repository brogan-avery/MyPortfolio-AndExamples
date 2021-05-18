//Brogan Avery
import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

class BookOrderAveryTest {

	@Test
	void test_calc_total() {
		assertEquals(79.71, BookOrderAvery.calc_total(68.45, 5),0.1);
		assertEquals(144.27, BookOrderAvery.calc_total(125.37, 8),0.1);
		assertEquals(61.61, BookOrderAvery.calc_total(55.55, 2),0.1);
	}

}
