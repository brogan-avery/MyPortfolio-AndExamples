/**************************************************************
* Title: Timed responce 
* Author: Brogan Avery
* Created: 2019
***************************************************************/
import java.time.*;
import javax.swing.JOptionPane;
public class TimedResponseAvery {

	public static void main(String[] args) {
		int min_to_secs = 60;
		
		LocalDateTime time1 = LocalDateTime.now();
		int sec1 = time1.getSecond();
		int min1 = time1.getMinute();
		int hour1 = time1.getHour();
		String start_time = hour1 + ":" + min1 + ":" + sec1; 
		
		JOptionPane.showConfirmDialog(null, "Are you a closet Taylor Swift fan?");
		
		LocalDateTime time2 = LocalDateTime.now();
		int sec2 = time2.getSecond();
		int min2 = time2.getMinute();
		int hour2 = time2.getHour();
		String end_time = hour2 + ":" + min2 + ":" + sec2; 
		
		int total_sec1 = (min1 * min_to_secs) + sec1; 
		
		int total_sec2 = (min2 * min_to_secs) + sec2;
		
		int difference = total_sec2 - total_sec1;
		
		 
		JOptionPane.showMessageDialog(null, "Start time: " + start_time + "\nEnd time: " + end_time + "\nIt took " + difference + " seconds for you to answer.\nWas it a difficult decision?");
	}

}
