import java.util.Scanner;

public class WeatherCheckAvery {

	public static Scanner in;

	public static void main(String[] args) {
		// declare variables
		String userSeason, tempTemp;
		double userTemp;
		double userNumber = 5;
		in = new Scanner(System.in);

		System.out.println("Please enter a season:");
		userSeason = in.next();
		System.out.println("Please enter a temperature:");
		tempTemp = in.next();

		// keeps running loop until tempTemp is a number
		while (tryParseDouble(tempTemp) == false) {
			System.out.println("Temperature must be a number. Please enter a temperature:");
			tempTemp = in.next();
		}

		// convert the temp temperature from a string to a double
		userTemp = Double.parseDouble(tempTemp);

		// make season lowercase
		userSeason = userSeason.toLowerCase();

		// outputs return String getWeatherAdvice
		System.out.println(getWeatherAdvice(userSeason, userTemp));
		
		// close the scanner
		in.close();
	}

	public static String getWeatherAdvice(String season, double temp) {
		final double SPRING_MIN = 60, SUMMER_MIN = 90, FALL_MIN = 50, WINTER_MAX = 10;

		String message = "No advice from me";

		if (season.equals("spring") && temp > SPRING_MIN) {
			message = "No jacket needed";
		} else if (season.equals("summer") && temp > SUMMER_MIN) {
			message = "Drink lots of water";
		} else if (season.equals("fall") && temp > FALL_MIN) {
			message = "Enjoy the leaves";
		} else if (season.equals("winter") && temp < WINTER_MAX) {
			message = "Brrr... Bundle Up";
		}

		return message;
	}

	// a methods for trying to parse an integer
	static boolean tryParseDouble(String value) {
		try {
			Double.parseDouble(value);
			return true;
		} catch (NumberFormatException e) {
			return false;
		}
	}
	
	public static boolean isEvenNumber(double userNumber) {
		if (userNumber % 2 == 0) {
			return true;
		}
			return false;
	}
	
	public static double addFive(double userNumber) {
		double result;
		result = userNumber + 5;
		return result;
	}

}
