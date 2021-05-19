/**************************************************************
* Title: Sort baby Names
* Author: Brogan Avery
* Created: 2019
***************************************************************/
import java.io.*;
import java.util.Scanner;
import java.net.URL;

public class SortBabyNamesAvery {

	public static void main(String[] args) {
		
		//File inputFile = new File("https://bbmedia.dmacc.edu/CIS/CIS171/babynames2014.txt ");
		
		//Scanner in = new Scanner(inputFile);
		
		try {
		String address = "https://bbmedia.dmacc.edu/CIS/CIS171/babynames2014.txt";
				 URL pageLocation = new URL(address);
				 Scanner input = new Scanner(pageLocation.openStream());
				
				 PrintWriter output_to_girls = new PrintWriter("girls.txt");
				 PrintWriter output_to_boys = new PrintWriter("boys.txt");
				 
				 input.useDelimiter("");
				 while(input.hasNextLine()){
				 String baby_name = input.nextLine();
				 String just_the_name = baby_name.substring(5);
				 	if (baby_name.contains("girl")) {
				 		output_to_girls.println(just_the_name);
				 	}
				 	else if (baby_name.contains("boy")) {
				 		output_to_boys.println(just_the_name);
				 	}
				 }
				
				 input.close();
				 output_to_girls.close();
				 output_to_boys.close();
		}
		catch (IOException e) {
			System.out.print("File not found.");
		}
				 
	}

}
