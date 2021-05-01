//Brogan Avery 
import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

class WeatherCheckAveryTest {

	@Test
	void testGetWeatherAdvice() {
		assertEquals("No advice from me", WeatherCheckAvery.getWeatherAdvice("winter", 70));
		assertEquals("No jacket needed", WeatherCheckAvery.getWeatherAdvice("spring", 61));
		assertEquals("Drink lots of water", WeatherCheckAvery.getWeatherAdvice("summer", 98));
		assertEquals("Enjoy the leaves", WeatherCheckAvery.getWeatherAdvice("fall", 55));
		assertEquals("Brrr... Bundle Up", WeatherCheckAvery.getWeatherAdvice("winter", 6));
		assertEquals("No advice from me", WeatherCheckAvery.getWeatherAdvice("winter", 50));
		assertEquals("No advice from me", WeatherCheckAvery.getWeatherAdvice("summer", 0));
		assertEquals("No advice from me", WeatherCheckAvery.getWeatherAdvice("summer", 80));
	}
	@Test
	void IsEvenNumber(){
		assertFalse(WeatherCheckAvery.isEvenNumber((5)));
		assertTrue(WeatherCheckAvery.isEvenNumber((4)));
		assertFalse(WeatherCheckAvery.isEvenNumber((-3)));
		assertTrue(WeatherCheckAvery.isEvenNumber((-10)));
		assertFalse(WeatherCheckAvery.isEvenNumber((1001)));
		
	}
	
	@Test
	void testAddFive(){
		assertEquals(10.22, WeatherCheckAvery.addFive(5.2145), 0.1);
		assertEquals(-12.4, WeatherCheckAvery.addFive(-17.4), 0.00001);
		assertEquals(10, WeatherCheckAvery.addFive(5), 0.00001);
	}	
}
