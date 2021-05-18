import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

class taxBracketAveryTest {

	@Test
	void testfedTaxBracket() {
		assertEquals(765, taxBracket.fedTaxBracket(7654), 1);

		assertEquals(198000, taxBracket.fedTaxBracket(500000), 1);
	}

	@Test
	void testiowaTaxBracket() {
		assertEquals(186, taxBracket.iowaTaxBracket(7654), 1);
		assertEquals(44900, taxBracket.iowaTaxBracket(500000), 1);
	}

}
