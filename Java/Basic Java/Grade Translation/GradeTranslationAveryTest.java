//Brogan Avery 
import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

class GradeTranslationAveryTest {

	@Test
	void testgetLetterGrade() {
		
		//String[] grade_array = {"A"};
		//int [] score_array = {90};
		//assertArrayEquals(grade_array, GradeTranslationAvery.getLetterGrade(score_array));
		
		//OR
		
		assertArrayEquals(new String[] {"A"}, GradeTranslationAvery.getLetterGrade(new int[] {90}));
		assertArrayEquals(new String[] {"B"}, GradeTranslationAvery.getLetterGrade(new int[] {80}));
		assertArrayEquals(new String[] {"C"}, GradeTranslationAvery.getLetterGrade(new int[] {70}));
		assertArrayEquals(new String[] {"D"}, GradeTranslationAvery.getLetterGrade(new int[] {60}));
		assertArrayEquals(new String[] {"F"}, GradeTranslationAvery.getLetterGrade(new int[] {50}));
	
		assertArrayEquals(new String[] {"A", "B", "C"}, GradeTranslationAvery.getLetterGrade(new int[] {90,80,70}));
		assertArrayEquals(new String[] {"F", "C", "B"}, GradeTranslationAvery.getLetterGrade(new int[] {40,76,88}));
	}

}
