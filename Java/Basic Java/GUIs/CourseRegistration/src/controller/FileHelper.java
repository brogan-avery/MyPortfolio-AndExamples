package controller;
//Brogan Avery
import java.util.ArrayList;

public interface FileHelper {
	public	boolean	doesAFileExist();
	public	ArrayList<?>	readFile();
	public	boolean	writeFile(ArrayList<?>	list);
}
