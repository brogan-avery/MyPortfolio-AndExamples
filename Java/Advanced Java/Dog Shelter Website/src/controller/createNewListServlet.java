//Brogan Avery
package controller;

import java.io.IOException;
import java.time.LocalDate;
import java.util.ArrayList;
import java.util.List;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import model.DogEntry;
import model.Worker; 
import model.ListDetails; 

/**
 * Servlet implementation class createNewListServlet
 */
@WebServlet("/createNewListServlet") 
public class createNewListServlet extends HttpServlet { 
	private static final long serialVersionUID = 1L;
       
    /**
     * @see HttpServlet#HttpServlet()
     */
    public createNewListServlet() { 
        super();
    }

	/**
	 * @see HttpServlet#doGet(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		DogEntryHelper helperObj = new DogEntryHelper();
		String listName = request.getParameter("listName"); 
		System.out.println("List Name: "+ listName);
		
		String month = request.getParameter("month");
		String day = request.getParameter("day");
		String year = request.getParameter("year");
		String workerName = request.getParameter("workerName"); 
		LocalDate ld;
		try {
			ld = LocalDate.of(Integer.parseInt(year), Integer.parseInt(month), Integer.parseInt(day));
		}catch(NumberFormatException ex) {
			ld = LocalDate.now();
		}
		
		String[] selectedDogEntries = request.getParameterValues("allDogEntriesToAdd");
		List<DogEntry> selectedDogEntriesInList = new ArrayList<DogEntry>();
		
		for(int i = 0; i<selectedDogEntries.length; i++) {
			System.out.println(selectedDogEntries[i]);
			DogEntry dogEntryObj = helperObj.searchForDogEntryById(Integer.parseInt(selectedDogEntries[i]));
			selectedDogEntriesInList.add(dogEntryObj);
			
		}
		
		Worker worker = new Worker(workerName);
		ListDetails listDetailsObj = new ListDetails(listName, ld, worker);
		listDetailsObj.setListOfDogEntries(selectedDogEntriesInList);
		ListDetailsHelper listDetailsHelperObj = new ListDetailsHelper();
		listDetailsHelperObj.insertNewListDetails(listDetailsObj);
		
		System.out.println("Success!");
		System.out.println(listDetailsObj.toString());
		
		getServletContext().getRequestDispatcher("/viewAllListsServlet").forward(request, response);
		
	
	}

	/**
	 * @see HttpServlet#doPost(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		doGet(request, response);
	}

}