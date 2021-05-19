import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

class EqualArrayCheckAveryTest {
	
	int[] arr1 = { 1, 2, 3, 4, 5, 6, 7, 8, 9 };
	int[] arr2 = { 1, 2, 3, 4, 5, 6, 7, 8, 9 };
	int[] arr3 = { 7, 6, 5, 6 };
	int[] arr4 = { 5, 8, 3, 0, 1, 4, 7, 2 };
	int[] arr5 = { 5, 8, 3, 0, 1, 4, 7, 2, 9 };
	
		@Test
		void testAreArraysEqual() {
			assertTrue(EqualArrayCheckAvery.areArraysEqual(arr1, arr2));
			assertFalse(EqualArrayCheckAvery.areArraysEqual(arr2, arr3));
			assertFalse(EqualArrayCheckAvery.areArraysEqual(arr3, arr4));
			assertFalse(EqualArrayCheckAvery.areArraysEqual(arr4, arr5));
			assertFalse(EqualArrayCheckAvery.areArraysEqual(arr4, arr1));
			
			
		}

	
	}


