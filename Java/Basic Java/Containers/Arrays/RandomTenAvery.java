/**************************************************************
* Title: Random 10 Array
* Author: Brogan Avery
* Created: 2019
***************************************************************/
import java.lang.Math;
import java.util.*;
public class RandomTenAvery {

	public static void main(String[] args) {

//============== DECLARE ARRAY / STRING==================		
		
		Random random_number = new Random(); 
		int min = 1;
		int max = 20;
		int[] random_array;
		random_array = new int[10];
		for (int i = 0; i < random_array.length; i++) {
			random_array[i] = random_number.nextInt((max - min) + min) + min;
		
	}
		//for (int i = 0; i < random_array.length; i++) {
			//random_array[i] = 1 + (int) (Math.random() * 20);
		//}
		
		System.out.println("\nString of original array: " + Arrays.toString(random_array));

//==============EACH ITEM==================		
		System.out.print("All array items: ");
		for (int item : random_array) {
			System.out.print(item + " ");
		}

//=============EVEN INDECIES===================
		System.out.print("\nEven index items: ");
		for (int i = 0; i < random_array.length; i += 2) {
			System.out.print(random_array[i] + " ");

		}

//===============EVEN NUMBERS=================
		System.out.print("\nEven elements: ");
		for (int i = 0; i < random_array.length; i++) {
			if (random_array[i] % 2 == 0) {
				System.out.print(random_array[i] + " ");
			}
		}

//==============REVERSED and BACK?==================
		int count = 0;
		int times_through = 2;

		while (count < times_through) {
			int other_i, temp_place;
			for (int i = 0; i < random_array.length / 2; i++) {
				temp_place = random_array[i];
				random_array[i] = random_array[random_array.length - i - 1];
				random_array[random_array.length - i - 1] = temp_place;
			}

			System.out.print("\nReversed array: ");
			for (other_i = 0; other_i < random_array.length; other_i++) {
				System.out.print(random_array[other_i] + " ");
			}
			count++;
		}

//==============FIRST==================
		int first_int = random_array[0];
		System.out.println("\nFirst element: " + first_int);

//=================LAST===============
		int last_int = random_array[random_array.length - 1];
		System.out.println("Last element: " + last_int);

//================HIGHEST================		
		int highest = random_array[0];
		for (int i = 0; i < random_array.length; i++) {
			if (random_array[i] > highest) {
				highest = random_array[i];
			}
		}

		System.out.println("Highest number in array: " + highest);

//================LOWEST================
		int lowest = random_array[0];
		for (int i = 0; i < random_array.length; i++) {
			if (random_array[i] < lowest) {
				lowest = random_array[i];
			}
		}

		System.out.println("Lowest number in array: " + lowest);

	}// END MAIN

}
