//Brogan Avery
package tests;

import java.time.LocalTime;
import java.util.ArrayList;

import controller.ClassroomFileHelper;
import controller.CourseFileHelper;
import controller.InstructorFileHelper;
import model.Classroom;
import model.Course;
import model.Instructor;

public class CourseFileHelperTest {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
//Create classrooms first
		ClassroomFileHelper cfh = new ClassroomFileHelper();
		
		Classroom CompSciLab = new Classroom("8", "17", "Ankeny", "Computer Lab", 25);
		Classroom BioLab = new Classroom("3", "17", "Ankeny", "Science Lab", 22);
		Classroom LitRoom = new Classroom("2", "12", "Urban", "Classroom", 18);
			
		ArrayList<Classroom> allClassrooms = new ArrayList<Classroom>();
		allClassrooms.add(BioLab);
		allClassrooms.add(LitRoom);
		allClassrooms.add(CompSciLab);
		
		System.out.println("Does a Classroom file exist? " + cfh.doesAFileExist());
		System.out.println("Writing classrooms to file is successful: " +cfh.writeFile(allClassrooms));
		System.out.println("Does a Classroom file exist after writing to it? " + cfh.doesAFileExist());
		
		ArrayList<Classroom> all = (ArrayList<Classroom>)cfh.readFile();
		System.out.println("Printing all items in the Classroom file");
		for(Classroom a: all){
		System.out.println(a.toString());
		}
		System.out.println("---------------");
		System.out.println();
		
		
		//Then instructors
		Instructor wsmith = new Instructor("Wanda Jean", "Smith");
		Instructor wfitz = new Instructor("Wilma", "Fitz");
		Instructor etheo = new Instructor("Emily", "Theo");
		
		ArrayList<Instructor> allInstructors = new ArrayList<Instructor>();
		allInstructors.add(wsmith);
		allInstructors.add(wfitz);
		allInstructors.add(etheo);
		
		InstructorFileHelper ifh = new InstructorFileHelper();
		System.out.println("Does an Instructor file exist? " + ifh.doesAFileExist());
		System.out.println("Writing instructors to file is successful: " + ifh.writeFile(allInstructors));
		System.out.println("Does an Instructor file exist after writing to it? " + ifh.doesAFileExist());
		ArrayList<Instructor> addedInstr = (ArrayList<Instructor>)ifh.readFile();
		System.out.println("Printing all items in the Instructor file");
		for(Instructor a: addedInstr){
			System.out.println(a.toString());
		}
		System.out.println("---------------");
		System.out.println();
		
		
		//Now courses
		Course bio101 = new Course("12345", "BIO101", LocalTime.of(11, 15), LocalTime.of(12, 55), wsmith, BioLab);
		Course cis171 = new Course("23456", "CIS171", LocalTime.of(10, 10), LocalTime.of(12, 20), wfitz, CompSciLab);
		Course lit105 = new Course("29876", "LIT105", LocalTime.of(15, 15), LocalTime.of(16, 30), etheo, LitRoom);
		
		ArrayList<Course> allCourses = new ArrayList<Course>();
		allCourses.add(bio101);
		allCourses.add(cis171);
		allCourses.add(lit105);
		CourseFileHelper cofh = new CourseFileHelper();
		System.out.println("Does a Courses file exist? " + cofh.doesAFileExist());
		System.out.println("Writing course to file is successful: " + cofh.writeFile(allCourses));
		System.out.println("Does a Courses file exist after writing to it? " + cofh.doesAFileExist());
		ArrayList<Course> readCoursesFromFile = (ArrayList<Course>) cofh.readFile();
		System.out.println("Printing all items in the Course file");
		for(Course a: readCoursesFromFile){
			System.out.println(a.toString());
		}
		

	}

}