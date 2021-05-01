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

import model.ListDetails;
import model.DogEntry;
import model.Worker;

/**
 * Servlet implementation class editListDetailsServlet
 */
@WebServlet("/editListDetailsServlet")
public class editListDetailsServlet extends HttpServlet {
	private static final long serialVersionUID = 1L;

	/**
	 * @see HttpServlet#HttpServlet()
	 */
	public editListDetailsServlet() {
		super();
	}

	/**
	 * @see HttpServlet#doGet(HttpServletRequest request, HttpServletResponse
	 *      response)
	 */
	protected void doGet(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException {
		response.getWriter().append("Served at: ").append(request.getContextPath());
	}

	/**
	 * @see HttpServlet#doPost(HttpServletRequest request, HttpServletResponse
	 *      response)
	 */
	protected void doPost(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException {
		ListDetailsHelper listDetailsHelperObj = new ListDetailsHelper();
		DogEntryHelper dogEntryHelperObj = new DogEntryHelper();
		WorkerHelper workerHelperObj = new WorkerHelper();
		
		
		Integer tempId = Integer.parseInt(request.getParameter("id"));
		ListDetails listToUpdate = listDetailsHelperObj.searchForListDetailsById(tempId);

		String newListName = request.getParameter("listName");

		String month = request.getParameter("month");
		String day = request.getParameter("day");
		String year = request.getParameter("year");
		
		String workerName = request.getParameter("workerName");
		//find our add the new shopper
		Worker newWorker = workerHelperObj.findWorker(workerName);

		LocalDate ld;
		try {
			ld = LocalDate.of(Integer.parseInt(year), Integer.parseInt(month), Integer.parseInt(day));
		} catch (NumberFormatException ex) {
			ld = LocalDate.now();
		}

		try {
			//items are selected in list to add
			String[] selectedDogEntries = request.getParameterValues("allDogEntriesToAdd");
			List<DogEntry> selectedDogEntriesInList = new ArrayList<DogEntry>();

			for (int i = 0; i < selectedDogEntries.length; i++) {
				System.out.println(selectedDogEntries[i]);
				DogEntry dogEntryObj = dogEntryHelperObj.searchForDogEntryById(Integer.parseInt(selectedDogEntries[i]));
				selectedDogEntriesInList.add(dogEntryObj);

			}
			listToUpdate.setListOfDogEntries(selectedDogEntriesInList);
		} catch (NullPointerException ex) {
			// no items selected in list - set to an empty list
			List<DogEntry> selectedDogEntriesInList = new ArrayList<DogEntry>();
			listToUpdate.setListOfDogEntries(selectedDogEntriesInList);
		}

		listToUpdate.setListName(newListName);
		listToUpdate.setVacDate(ld);
		listToUpdate.setWorker(newWorker);

		listDetailsHelperObj.updateList(listToUpdate);

		getServletContext().getRequestDispatcher("/viewAllListsServlet").forward(request, response);
	}

}