package mainPackage.beans;

import javax.persistence.Embeddable;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@NoArgsConstructor
@Embeddable
public class Excursion {
	private String activity;
	private String level; //level of difficulty from 1- being anyone can do to 5- being you need to be very fit
	private int hours; //number of hours the activity takes
	
	
	public Excursion(String activity, String level, int hours) {
		super();
		this.activity = activity;
		this.level = level;
		this.hours = hours;
	}
}