//Brogan Avery

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

class ShopperRewardsAveryTest {

	@Test
	void testCalcDiscount() {
		// test format: assertEquals(discount_percentage, ShopperRewardsAvery.calcDiscount(grocery_bill));
		
		assertEquals(0, ShopperRewardsAvery.calcDiscount(8.55));
		assertEquals(0.04, ShopperRewardsAvery.calcDiscount(50.6));
		assertEquals(0.07, ShopperRewardsAvery.calcDiscount(101.01));
		assertEquals(0.1, ShopperRewardsAvery.calcDiscount(190));
		assertEquals(0.15, ShopperRewardsAvery.calcDiscount(400.99));
		
	}
	
	@Test
	void testCalcGasDiscount() {
		assertEquals(0, ShopperRewardsAvery.calcGasDiscount(0.88));
		assertEquals(1, ShopperRewardsAvery.calcGasDiscount(25));
		assertEquals(2, ShopperRewardsAvery.calcGasDiscount(95.54));
		assertEquals(3, ShopperRewardsAvery.calcGasDiscount(101.01));
	
		
	}

}
