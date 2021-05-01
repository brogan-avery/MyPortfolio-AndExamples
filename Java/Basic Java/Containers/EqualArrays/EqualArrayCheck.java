
//Brogan Avery
import java.util.Arrays;

public class EqualArrayCheckAvery {

	public static void main(String[] args) {

//Make some arrays
		int[] array1 = { 1, 2, 3, 4, 10, 11, 12 };
		int[] array2 = { 13, 14, 15, 16, 17, 18, 19 };
		int[] array3 = { 1, 2, 3, 4, 10, 11, 12 };
		int[] array4 = { 13, 14, 15 };

		boolean[] array_of_answers = { areArraysEqual(array1, array2), areArraysEqual(array1, array3),
				areArraysEqual(array1, array4) };
		String result;
		int array_count = 1;

		for (int i = 0; i < array_of_answers.length; i++) {
			if (array_of_answers[i] == true) {
				result = "are equal";
			} else {
				result = "are not equal";
			}
			array_count++;
			System.out.println("Array 1 and " + array_count + " " + result);
		}

	}// END MAIN

	public static boolean areArraysEqual(int[] one_array, int[] another_array) {

		if (one_array.length != another_array.length) {
			return false;
		}

		for (int i = 0; i < one_array.length; i++) {
			if (one_array[i] != another_array[i]) {
				return false;
			}
		}

		return true;

	}

}// END CLASS
