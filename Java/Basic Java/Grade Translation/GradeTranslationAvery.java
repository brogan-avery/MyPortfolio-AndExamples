/**************************************************************
* Title: Grade Translation
* Author: Brogan Avery
* Created: 2019
***************************************************************/

import java.util.Scanner;
import java.util.Arrays;
public class GradeTranslationAvery {

	
	public static void main(String[] args) {
		
		Scanner input = new Scanner(System.in); 
		
		System.out.println("How many scores do you want to enter?");
		int array_length = input.nextInt(); 
		
		int[] score_array;
		score_array = new int[array_length];
		
		System.out.println("Enter scores");
		
		
			for (int i = 0; i < score_array.length; i++){
				score_array[i] = input.nextInt(); 
				}
		
		input.close(); //closes the scanner
		
		String[] grade_array = getLetterGrade(score_array);
		System.out.println("Score --------- Grade");
		for (int i = 0; i < score_array.length; i++){
			System.out.println(score_array[i] + "----------" + grade_array[i]);
		}
		
	}//END MAIN
	
public static String[] getLetterGrade (int[] score_array) {
		String[] grade_array;
		grade_array = new String[score_array.length];
		
		String letter_grade = "G";
		
		for (int i = 0; i < score_array.length; i++){
			if (score_array[i] < 59) {
				letter_grade = "F";
			}
			
			if (score_array[i] >= 59 && score_array[i] < 69  ) {
				letter_grade = "D";
			}
			
			if (score_array[i] >= 69 && score_array[i] < 79  ) {
				letter_grade = "C";
			}
			
			if (score_array[i] >= 79 && score_array[i] < 89  ) {
				letter_grade = "B";
			}
			
			if (score_array[i] >= 89 ) {
				letter_grade = "A";
			}
			
			grade_array[i] = letter_grade;
			
			}//END FOR
		
		return grade_array;
		
		
	}//END METHOD

}
