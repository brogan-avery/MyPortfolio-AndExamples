import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

class PasswordValidationAveryTest {

	@Test
	void testValidatePassword() {
		//good password
		assertTrue(PasswordValidationAvery.validatePassword("1Turtle2", "1Turtle2"));
		
		//doesn't match
		assertFalse(PasswordValidationAvery.validatePassword("1Penguin", "2Penguin"));
		
		//match but too short
		assertFalse(PasswordValidationAvery.validatePassword("CATs123", "CATs123"));
		
		//match but no lowercase
		assertFalse(PasswordValidationAvery.validatePassword("DOGS1234", "DOGS1234"));
		
		//match but no uppercase
		assertFalse(PasswordValidationAvery.validatePassword("pigs1234", "pigs1234"));
		
		//match but no digits
		assertFalse(PasswordValidationAvery.validatePassword("HAMSTEr", "HAMSTEr"));
		
		//first password is too short
		assertFalse(PasswordValidationAvery.validatePassword("Frog123", "Frog1234"));
		
		//extra long good password
		assertTrue(PasswordValidationAvery.validatePassword("123ClownFish456", "123ClownFish456"));
		
		
	}

}