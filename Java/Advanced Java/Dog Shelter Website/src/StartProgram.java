//Brogan Avery

import java.util.List;
import java.util.Scanner;

import controller.DogEntryHelper;
import model.DogEntry;

public class StartProgram {

		static Scanner in = new Scanner(System.in);
		static DogEntryHelper DogEntryHelperObj = new DogEntryHelper();

		private static void addDogEntry() {
			System.out.print("Enter the breed: ");
			String breed = in.nextLine();
			System.out.print("Enter the name: ");
			String name = in.nextLine();
			System.out.print("Enter the age: ");
			int age = in.nextInt();
			
			DogEntry newEntry = new DogEntry(breed, name, age);
			DogEntryHelperObj.insertDogEntry(newEntry);

		}

		private static void deleteDogEntry() {
			System.out.print("Enter the breed of the dog to delete: ");
			String breed = in.nextLine();
			System.out.print("Enter the name of the dog to delete: ");
			String name = in.nextLine();
			System.out.print("Enter the age of the dog to delete: ");
			int age = in.nextInt();
			
			DogEntry toDelete =	new	DogEntry(breed, name, age);
			DogEntryHelperObj.deleteDogEntry(toDelete);

		}

		private static void editDogEntry() {
			System.out.println("How would you like to search? ");
			System.out.println("1 : Search by dog's breed");
			System.out.println("2 : Search by dog's name");
			System.out.println("3 : Search by dog's age");
			int searchBy = in.nextInt();
			in.nextLine();
			
			List<DogEntry> foundDogEntry;
			if (searchBy == 1) {
				System.out.print("Enter the dog's breed: ");
				String breed = in.nextLine();
				foundDogEntry = DogEntryHelperObj.searchForDogEntryByBreed(breed);
				
			} 
			
			else if (searchBy == 2) {
				System.out.print("Enter the dog's name: ");
				String name = in.nextLine();
				foundDogEntry = DogEntryHelperObj.searchForDogEntryByName(name);

			}
			
			else {
				System.out.print("Enter the dog's age: ");
				int age = in.nextInt();
				foundDogEntry = DogEntryHelperObj.searchForDogEntryByAge(age);

			}
			
			
			
			if (!foundDogEntry.isEmpty()) {
				System.out.println("Found Results.");
				for (DogEntry e : foundDogEntry) {
					System.out.println(e.getId() + " : " + e.returnDogEntryDetails());
				}
				System.out.print("Which ID to edit: ");
				int idToEdit = in.nextInt();

				DogEntry toEdit = DogEntryHelperObj.searchForDogEntryById(idToEdit);
				System.out.println("Retrieved: Breed - " + toEdit.getBreed() + ", Name -  " + toEdit.getName() + ", Age - " + toEdit.getAge());
				System.out.println("1 : Update breed");
				System.out.println("2 : Update name");
				System.out.println("3 : Update age");
				int update = in.nextInt();
				in.nextLine();

				if (update == 1) {
					System.out.print("New breed: ");
					String newBreed = in.nextLine();
					toEdit.setBreed(newBreed);
				} 
				
				else if (update == 2) {
					System.out.print("New Name: ");
					String newName = in.nextLine();
					toEdit.setName(newName);
				}
				
				else if (update == 3) {
					System.out.print("New Age: ");
					int newAge = in.nextInt();
					toEdit.setAge(newAge);
				}

				DogEntryHelperObj.updateDogEntry(toEdit);

			} 
			
			else {
				System.out.println("---- No results found");
			}

		}

		public static void main(String[] args) {
			runMenu();
			
		}

		public static void runMenu() {
			boolean goAgain = true;
			
			System.out.println("--- Welcome to our awesome Dog Rescue Index! ---");
			
			while (goAgain) {
				System.out.println("*  Select an option:");
				System.out.println("*  1 -- Add a dog entry");
				System.out.println("*  2 -- Edit a dog entry");
				System.out.println("*  3 -- Delete a dog entry");
				System.out.println("*  4 -- View the list of dog entries");
				System.out.println("*  5 -- Exit the awesome program");
				System.out.print("*  Your selection: ");
				int selection = in.nextInt();
				in.nextLine();

				if (selection == 1) {
					addDogEntry();
				} else if (selection == 2) {
					editDogEntry();
				} else if (selection == 3) {
					deleteDogEntry();
				} else if (selection == 4) {
					viewAllEntries();
				} else {
					DogEntryHelperObj.cleanUp();
					System.out.println("   Goodbye!   ");
					goAgain = false;
				}

			}

		}

		private static void viewAllEntries() {
			List<DogEntry>	allDogEntries = DogEntryHelperObj.showAllDogEntries();
			for(DogEntry entry : allDogEntries){
				System.out.println(entry.returnDogEntryDetails());
			}

		}

	}