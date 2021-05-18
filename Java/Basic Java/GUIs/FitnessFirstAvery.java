/**************************************************************
* Title: Fitness First
* Author: Brogan Avery
* Created: 2019
* Description: Uses Jpane to let user schedule a massage 
***************************************************************/
import javax.swing.JOptionPane;

public class FitnessFirstAvery {
	public static void main(String[] args) {
		String userID;
		String min_input;
		
		// get input for User ID and time via JPane
		userID= JOptionPane.showInputDialog("Enter User ID");
		min_input= JOptionPane.showInputDialog("Enter desired length of massage in minutes");
		
		// formats string of User ID
		String sub1 = userID.substring(0,2);
		String sub2 = userID.substring(2,5);
		String sub3 = userID.substring(5);
		String userID_formatted = sub1 + "-" + sub2 + "-" + sub3;
		
		// calls function to convert mins to hours
		String length = min_to_hours(min_input);
		
		JOptionPane.showMessageDialog(null,"Thank you member " + userID_formatted.toUpperCase() + " for your reservation of " + length);
		
		System.exit(0);	
	}
	
	// Converts mins to hours
	public static  String min_to_hours(String min_input) {
		int min = Integer.parseInt(min_input);
		final int MIN_IN_HOUR = 60;
		int hour = (min / MIN_IN_HOUR);
		int hour_remainder = (min % MIN_IN_HOUR);
		String length = (hour + " hour(s) and " + hour_remainder + " minute(s).");
		return length;
	}
	
}
	
	

