//Brogan Avery
package controller;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.PrintWriter;
import java.time.LocalTime;
import java.util.ArrayList;
import java.util.Scanner;

import model.Classroom;
import model.Course;
import model.Instructor;

public class InstructorFileHelper implements FileHelper {
	String nameOfFile = "instructors.txt";
	File instructorList = new File(nameOfFile);

	@Override
	public boolean doesAFileExist() {
		if (instructorList.exists()) {
			return true;
		} else {
			return false;
		}
	}

	@Override
	public ArrayList<?> readFile() {
		ArrayList<Instructor> allInstructors = new ArrayList<Instructor>();
		Scanner fileIn;
		try {
			fileIn = new Scanner(instructorList);
			while (fileIn.hasNextLine()) {
				String value = fileIn.nextLine();
				String[] parts = value.split(",");
				Instructor currentInstructor = new Instructor(parts[0], parts[1], parts[2]);
				allInstructors.add(currentInstructor);
			}
			fileIn.close();
		} catch (FileNotFoundException e) {
//	TODO	Auto-generated	catch	block
		}
		return allInstructors;
	}

//continued	on	next	page
	@Override
	public boolean writeFile(ArrayList<?> list) {
		ArrayList<Instructor> instructorsToWrite = (ArrayList<Instructor>) (list);
		try {
			PrintWriter instructorFile = new PrintWriter(nameOfFile);
			for (Instructor i : instructorsToWrite) {
				StringBuilder sb = new StringBuilder();
				sb.append(i.getFirstName() + "," + i.getLastName() + "," + i.getEmail());
				instructorFile.println(sb.toString());
			}
			instructorFile.close();
		} catch (FileNotFoundException e) {
			return false;
		}
		return true;
	}
}