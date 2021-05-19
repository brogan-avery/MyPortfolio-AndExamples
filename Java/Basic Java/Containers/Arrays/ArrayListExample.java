//Brogan Avery
import java.util.ArrayList;

public class ArrayListExamplesAvery {

	public static void main(String[] args) {

//     think of declaring and initializing ArrayLists like variable declarations 
//       data type |  variable name | setting new value for variable
//      [⭣⭣⭣⭣⭣⭣⭣⭣]  [⭣⭣]    [⭣⭣⭣⭣⭣⭣⭣⭣⭣⭣⭣⭣]
		ArrayList<String> names = new ArrayList<String>();
		System.out.println("Original emptly ArrayList: " + names);

		names.add("Andy");
		names.add("Angela");
		names.add("Dwight");
		names.add("Erin");
		names.add("Jim");
		names.add("Michael");
		names.add("Pam");
		names.add("Toby");
		System.out.println("After names are added: " + names);

		System.out.print("Each Array item: ");
		for (int i = 0; i < names.size(); i++) {
			String item = names.get(i);
			System.out.print(item + " | ");
		}
		System.out.println("\nSize of Arraylist: " + names.size());

		names.set(0, "Andy Bernard");
		System.out.println("After using set: " + names);

		names.add(5, "Kelly");
		System.out.println("Other way to add: " + names);

		System.out.print("Each Array item using enhanced for loop: ");
		for (String item : names) {
			System.out.print(item + " | ");
		}

		ArrayList<String> names2 = new ArrayList<String>(names);
		System.out.println("\nSecond Arraylist:" + names2);

		names.remove(0);

		System.out.println("Remove index 0 from names but not names2:" + "\n NAMES:" + names + "\n NAMES2:" + names2);

	}// END MAIN

}
