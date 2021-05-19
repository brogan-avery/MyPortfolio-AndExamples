//Brogan Avery
package model;
import java.time.LocalTime;
public class Course {
//vars
	private String CRN;
	private String courseName;
	private LocalTime startTime;
	private LocalTime endTime;
	private Instructor teacher;
	private Classroom location;
	
	
//constructors
	public Course() {
		setCRN(null);
		setCourseName(null);
		setStartTime(null);
		setEndTime(null);
		setTeacher(null);
		setLocation(null);
		
	}
	
	public Course(String CRN, String courseName, LocalTime startTime,  LocalTime endTime, Instructor teacher, Classroom location) {
		setCRN(CRN);
		setCourseName(courseName);
		setStartTime(startTime);
		setEndTime(endTime);
		setTeacher(teacher);
		setLocation(location);
		
	}
	
//getters	
	public String getCRN() {
		return CRN;
	}
	public String getCourseName() {
		return courseName;
	}
	public LocalTime getStartTime() {
		return startTime;
	}
	public LocalTime getEndTime() {
		return endTime;
	}
	public Instructor getTeacher() {
		return teacher;
	}
	public Classroom getLocation() {
		return location;
	}
//setters
	public void setCRN(String CRN) {
		this.CRN = CRN;
	}
	public void setCourseName(String courseName) {
		this.courseName = courseName;
	}
	public void setStartTime(LocalTime startTime) {
		this.startTime = startTime;
	}
	public void setEndTime(LocalTime endTime) {
		this.endTime = endTime;
	}
	public void setTeacher(Instructor teacher) {
		this.teacher = teacher;
	}
	public void setLocation(Classroom location) {
		this.location = location;
	}
//methods	
	@Override
	public String toString() {
		return "Course [CRN=" + CRN + ", courseName=" + courseName + ", startTime=" + startTime + ", endTime=" + endTime
				+ ", teacher=" + teacher + ", location=" + location + "]";
	}
	
	
	
	
}
